from pydantic import BaseModel


class Course(BaseModel):
    name: str


class Student(BaseModel):
    name: str
    age: int
    city: str


class UpdateCity(BaseModel):
    name: str
    new_city: str


class Relationship(BaseModel):
    student_name: str
    course_name: str