import os
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from fastapi import FastAPI
from dotenv import load_dotenv


# Load environment variables from .env file for database connection
load_dotenv()
db_url = os.getenv("NEON_DB_URL")

# Create a SQLAlchemy engine and session
engine = create_engine(db_url)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# Create a FastAPI app
app = FastAPI()

# API endpoint to get all students from the database
@app.get("/students")
def get_students():
    session = SessionLocal()
    try:
        result = session.execute(text("SELECT * FROM students"))
        students = result.fetchall()
        print(students)
        return [dict(row._mapping) for row in students]
    finally:
        session.close()


# API endpoint to get a student by ID from the database
@app.get("/students/{student_id}")
def get_student_by_id(student_id: int):
    session = SessionLocal()
    try:
        result = session.execute(text("SELECT * FROM students WHERE id = :id"), {"id": student_id})
        student = result.fetchone()
        print(student)
        return dict(student._mapping) if student else None
    finally:
        session.close()



# API endpoint to create a new student in the database
# Create a Pydantic model for student creation validation
from pydantic import BaseModel, EmailStr
class StudentCreate(BaseModel):
    name: str
    email: EmailStr
    age: int | None
    city: str | None


@app.post("/students")
def create_student(student: StudentCreate):
    session = SessionLocal()
    try:
        session.execute(
            text("INSERT INTO students (name, email, age, city) VALUES (:name, :email, :age, :city)"),
            {"name": student.name, "email": student.email, "age": student.age, "city": student.city}
        )
        session.commit()
        return {"message": "Student created successfully"}
    finally:
        session.close()




# API endpoint to update a student's city in the database
@app.patch("/students/{student_id}/city")
def update_city(student_id: int, new_city: str):
    session = SessionLocal()
    try:
        session.execute(
            text("UPDATE students SET city = :city WHERE id = :id"),
            {"city": new_city, "id": student_id}
        )
        session.commit()
        return {"message": "City updated successfully"}
    finally:
        session.close()



# API endpoint to get course revenue from the database
@app.get("/course_revenue")
def course_revenue():
    session = SessionLocal()
    query = """
    SELECT
        c.id,
        c.title,
        c.price,
        COUNT(e.id) AS total_students,
        c.price * COUNT(e.id) AS revenue
    FROM courses c
    LEFT JOIN enrollments e
        ON c.id = e.course_id
    WHERE e.status = 'active'
    GROUP BY
        c.id,
        c.title,
        c.price
    ORDER BY revenue DESC;
    """
    result = session.execute(text(query))
    rows = result.fetchall()
    session.close()
    result = []
    for row in rows:
        result.append({
            "course_id": row[0],
            "course_name": row[1],
            "price": float(row[2]),
            "total_students": row[3],
            "revenue": float(row[4])
        })
    return result