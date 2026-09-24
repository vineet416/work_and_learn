from pydantic import BaseModel, Field, EmailStr
from typing import Optional


# Pydantic models student creation and validation
class Student(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)
    email: EmailStr
    age: int | None = Field(None, gt=0)


# Pydantic model for course creation and validation
class Course(BaseModel):
    title: str = Field(min_length=1, max_length=100)
    description: str = Field(min_length=1, max_length=500)
    price: float = Field(gt=0)
    duration: int = Field(gt=0)
    instructor: str = Field(min_length=1, max_length=100)
    category: str = Field(min_length=1, max_length=100)
    rating: float = Field(ge=0, le=5)
    active: bool = Field(default=True)


# Pydantic model for enrollment creation and validation
class Enrollment(BaseModel):
    student_id: int = Field(gt=0)
    course_id: int = Field(gt=0)
    status: str = Field(min_length=1, max_length=50)


# Pydantic model for updating student records
class StudentUpdate(BaseModel):
    name: Optional[str] = Field(None, min_length=1, max_length=100)
    email: Optional[EmailStr] = None
    age: Optional[int] = Field(None, gt=0)


# Pydantic model for updating course records
class CourseUpdate(BaseModel):
    title: Optional[str] = Field(None, min_length=1, max_length=100)
    description: Optional[str] = Field(None, min_length=1, max_length=500)
    price: Optional[float] = Field(None, gt=0)
    duration: Optional[int] = Field(None, gt=0)
    instructor: Optional[str] = Field(None, min_length=1, max_length=100)
    category: Optional[str] = Field(None, min_length=1, max_length=100)
    rating: Optional[float] = Field(None, ge=0, le=5)
    active: Optional[bool] = None


# Pydantic model for updating enrollment records
class EnrollmentUpdate(BaseModel):
    student_id: Optional[int] = Field(None, gt=0)
    course_id: Optional[int] = Field(None, gt=0)
    status: Optional[str] = Field(None, min_length=1, max_length=50)