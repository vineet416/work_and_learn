
import os
from contextlib import asynccontextmanager

import psycopg
from psycopg.rows import dict_row
from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel, Field


DATABASE_URL = os.environ["DATABASE_URL"]


def get_connection():
    return psycopg.connect(DATABASE_URL, row_factory=dict_row)


@asynccontextmanager
async def lifespan(app: FastAPI):
    with get_connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS students (
                    id SERIAL PRIMARY KEY,
                    name VARCHAR(100) NOT NULL,
                    email VARCHAR(150) UNIQUE NOT NULL,
                    course VARCHAR(100) NOT NULL
                )
            """)
    yield


app = FastAPI(
    title="Task 23 - Student Management System",
    lifespan=lifespan,
)


class StudentCreate(BaseModel):
    name: str = Field(min_length=1, max_length=100)
    email: str = Field(min_length=3, max_length=150)
    course: str = Field(min_length=1, max_length=100)


class StudentUpdate(BaseModel):
    name: str = Field(min_length=1, max_length=100)
    email: str = Field(min_length=3, max_length=150)
    course: str = Field(min_length=1, max_length=100)


@app.get("/")
def home():
    return {
        "message": "Student Management API is running",
        "task": 23,
    }


@app.get("/health")
def health():
    try:
        with get_connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute("SELECT 1")

        return {"status": "healthy", "database": "connected"}

    except psycopg.Error as error:
        raise HTTPException(
            status_code=503,
            detail="Database connection failed",
        ) from error


@app.post("/students", status_code=201)
def create_student(student: StudentCreate):
    try:
        with get_connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    """
                    INSERT INTO students (name, email, course)
                    VALUES (%s, %s, %s)
                    RETURNING id, name, email, course
                    """,
                    (student.name, student.email, student.course),
                )
                return cursor.fetchone()

    except psycopg.errors.UniqueViolation as error:
        raise HTTPException(
            status_code=409,
            detail="A student with this email already exists",
        ) from error


@app.get("/students")
def list_students(search: str | None = Query(default=None)):
    with get_connection() as connection:
        with connection.cursor() as cursor:
            if search:
                cursor.execute(
                    """
                    SELECT id, name, email, course
                    FROM students
                    WHERE name ILIKE %s
                       OR email ILIKE %s
                       OR course ILIKE %s
                    ORDER BY id
                    """,
                    (f"%{search}%", f"%{search}%", f"%{search}%"),
                )
            else:
                cursor.execute(
                    """
                    SELECT id, name, email, course
                    FROM students
                    ORDER BY id
                    """
                )

            return cursor.fetchall()


@app.get("/students/{student_id}")
def get_student(student_id: int):
    with get_connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute(
                """
                SELECT id, name, email, course
                FROM students
                WHERE id = %s
                """,
                (student_id,),
            )
            student = cursor.fetchone()

    if student is None:
        raise HTTPException(status_code=404, detail="Student not found")

    return student


@app.put("/students/{student_id}")
def update_student(student_id: int, student: StudentUpdate):
    try:
        with get_connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    """
                    UPDATE students
                    SET name = %s, email = %s, course = %s
                    WHERE id = %s
                    RETURNING id, name, email, course
                    """,
                    (student.name, student.email, student.course, student_id),
                )
                updated = cursor.fetchone()

    except psycopg.errors.UniqueViolation as error:
        raise HTTPException(
            status_code=409,
            detail="A student with this email already exists",
        ) from error

    if updated is None:
        raise HTTPException(status_code=404, detail="Student not found")

    return updated


@app.delete("/students/{student_id}")
def delete_student(student_id: int):
    with get_connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute(
                """
                DELETE FROM students
                WHERE id = %s
                RETURNING id, name, email, course
                """,
                (student_id,),
            )
            deleted = cursor.fetchone()

    if deleted is None:
        raise HTTPException(status_code=404, detail="Student not found")

    return {
        "message": "Student deleted successfully",
        "student": deleted,
    }
