import os
from fastapi import FastAPI
from supabase import create_client
from dotenv import load_dotenv
load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

client = create_client(SUPABASE_URL, SUPABASE_KEY)

app = FastAPI()

@app.get("/students")
def get_students():
    response = client.table("students").select("*").execute()
    return response.data


@app.get("/students/{student_id}")
def get_student(student_id: int):
    response = client.table("students").select("*").eq("id", student_id).execute()
    return response.data[0] if response.data else None


@app.get("/students/age/{age}")
def filter_by_age(age: int):
    response = client.table("students").select("*").eq("age", age).execute()
    return response.data



from pydantic import BaseModel, EmailStr
class Student(BaseModel):
    name: str
    email: EmailStr
    age: int
    course: str


@app.post("/students")
def insert_student(student: Student):
    response = client.table("students").insert(student.model_dump()).execute()
    return response.data