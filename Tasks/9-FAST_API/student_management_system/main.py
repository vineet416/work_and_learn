from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field, EmailStr
from typing import Optional


# FastAPI Application
app = FastAPI()


# Pydantic Models
class Student(BaseModel):
    name: str = Field(min_length=2, max_length=100)
    age: int = Field(ge=5, le=100)
    course: str = Field(min_length=2, max_length=100)
    email: EmailStr = Field(min_length=5, max_length=150)
    marks: float = Field(ge=0, le=100)


class StudentPatch(BaseModel):
    name: Optional[str] = Field(default=None, min_length=2, max_length=100)
    age: Optional[int] = Field(default=None, ge=5, le=100)
    course: Optional[str] = Field(default=None, min_length=2, max_length=100)
    email: Optional[str] = Field(default=None, min_length=5, max_length=150)
    marks: Optional[float] = Field(default=None, ge=0, le=100)


# Student Data
students = {
    1: {
        "student_id": 1,
        "name": "Vineet Patel",
        "age": 23,
        "course": "Computer Science",
        "email": "vineet@aiwithvineet.in",
        "marks": 88.5
    },
    2: {
        "student_id": 2,
        "name": "Arya Sharma",
        "age": 22,
        "course": "Mathematics",
        "email": "arya@aiwithvineet.in",
        "marks": 92.0
    }
}


# Find Student Function
def find_student(student_id: int) -> Student:
    for id, student in students.items():
        if id == student_id:
            return student

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Student with id {student_id} not found"
    )



# Home Endpoint
@app.get("/")
def home():
    return {"message": "Welcome to the Student Management API"}


# CREATE students
@app.post("/students")
def create_student(student_data: Student):
    new_id = max(students.keys()) + 1
    students[new_id] = {
        "student_id": new_id,
        "name": student_data.name,
        "age": student_data.age,
        "course": student_data.course,
        "email": student_data.email,
        "marks": student_data.marks
    } 
    return {"message": "Student created successfully", "student_id": new_id}


# GET list of all students
@app.get("/students")
def list_students():
    return list(students.values())


# Get a specific student by ID
@app.get("/students/{student_id}")
def get_student(student_id: int):
    return find_student(student_id)


# Replace a student record with PUT /students/{student_id}
@app.put("/students/{student_id}")
def replace_student(student_id: int, student_data: Student):
    find_student(student_id) # To verify if the student exists, will raise 404 if not found
    students[student_id] = {
        "student_id": student_id,
        "name": student_data.name,
        "age": student_data.age,
        "course": student_data.course,
        "email": student_data.email,
        "marks": student_data.marks
    }
    return {"message": "Student record replaced successfully", "student_id": student_id}


# PARTIAL UPDATE using PATCH /students/{student_id}
@app.patch("/students/{student_id}")
def update_student(student_id: int,student_data: StudentPatch):
    find_student(student_id) # To verify if the student exists, will raise 404 if not found
    students[student_id].update(student_data.model_dump(exclude_unset=True))
    return {"message": "Student record updated successfully", "student_id": student_id}


# DELETE - DELETE /students/{student_id}
@app.delete("/students/{student_id}")
def delete_student(student_id: int):
    find_student(student_id) # To verify if the student exists, will raise 404 if not found
    students.pop(student_id)
    return {"message": "Student record deleted successfully", "student_id": student_id}