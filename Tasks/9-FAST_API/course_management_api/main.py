from typing import Optional
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field


# FastAPI instance
app = FastAPI()


# Pydantic Models
class CourseCreate(BaseModel):
    title: str = Field(min_length=3, max_length=100)
    description: str = Field(min_length=10, max_length=500)
    price: float = Field(gt=0)
    duration: str = Field(min_length=2, max_length=50)
    instructor: str = Field(min_length=2, max_length=100)
    category: str = Field(min_length=2, max_length=50)
    rating: float = Field(ge=0, le=5)
    active: bool = True


class CourseUpdate(BaseModel):
    title: Optional[str] = Field(default=None, min_length=3, max_length=100)
    description: Optional[str] = Field(default=None, min_length=10, max_length=500)
    price: Optional[float] = Field(default=None, gt=0)
    duration: Optional[str] = Field(default=None, min_length=2, max_length=50)
    instructor: Optional[str] = Field(default=None, min_length=2, max_length=100)
    category: Optional[str] = Field(default=None, min_length=2, max_length=50)
    rating: Optional[float] = Field(default=None, ge=0, le=5)
    active: Optional[bool] = None


# Course Data
courses = {
    1: {
        "course_id": 1,
        "title": "Python Programming",
        "description": "Learn Python programming from basics to advanced concepts.",
        "price": 999,
        "duration": "8 weeks",
        "instructor": "Vineet Patel",
        "category": "python",
        "rating": 4.5,
        "active": True
    },

    2: {
        "course_id": 2,
        "title": "Machine Learning",
        "description": "Learn machine learning algorithms and practical applications.",
        "price": 4500,
        "duration": "12 weeks",
        "instructor": "Arya Patel",
        "category": "machine learning",
        "rating": 4.8,
        "active": True
    },

    3: {
        "course_id": 3,
        "title": "Web Development",
        "description": "Learn frontend and backend web development fundamentals.",
        "price": 3000,
        "duration": "10 weeks",
        "instructor": "Rohit Sharma",
        "category": "web development",
        "rating": 4.2,
        "active": False
    }
}


# Find Course Function
def find_course(course_id: int) -> dict:
    for id, course in courses.items():
        if id == course_id:
            return course
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Course with id {course_id} not found"
    )


# Home Endpoint
@app.get("/")
def home():
    return {"message": "Welcome to the Course Management API"}


# CREATE Courses Endpoint
@app.post("/create_course") 
def create_course(course_data: CourseCreate):
    next_id = max(courses.keys()) + 1
    new_course = {
        "course_id": next_id,
        "title": course_data.title,
        "description": course_data.description,
        "price": course_data.price,
        "duration": course_data.duration,
        "instructor": course_data.instructor,
        "category": course_data.category,
        "rating": course_data.rating,
        "active": course_data.active
    }
    courses[next_id] = new_course
    return {"message": "Course created successfully", "course_id": next_id}


# Replace Course Endpoint
@app.put("/replace_courses/{course_id}")
def replace_course(course_id: int, course_data: CourseCreate):
    existing_course = find_course(course_id)
    replacement = {
        "course_id": course_id,
        "title": course_data.title,
        "description": course_data.description, 
        "price": course_data.price,
        "duration": course_data.duration,
        "instructor": course_data.instructor,
        "category": course_data.category,
        "rating": course_data.rating,
        "active": course_data.active
    }
    courses[course_id] = replacement
    return {"message": "Course replaced successfully", "course_id": course_id, "course_data": replacement}


# PARTIAL UPDATE Courses Endpoint
@app.patch("/update_courses/{course_id}")
def update_course(course_id: int, course_data: CourseUpdate):
    existing_course = find_course(course_id)
    updates = course_data.model_dump(exclude_unset=True)
    courses[course_id].update(updates)
    return {"message": "Course updated successfully", "course_id": course_id, "updated_fields": updates}


# DELETE Courses Endpoint
@app.delete("/delete_courses/{course_id}")
def delete_course(course_id: int):
    course = find_course(course_id)
    del courses[course_id]
    return {"message": "Course deleted successfully", "deleted_course_id": course_id}


# GET ALL Courses Endpoint
@app.get("/courses/")
def get_all_courses():
    return {"courses": list(courses.values())}


# GET Course with Filtering Endpoint
@app.get("/courses")
def get_courses(category: Optional[str] = None, min_price: Optional[float] = None, max_price: Optional[float] = None, active: Optional[bool] = None):
    filtered_courses = list(courses.values())
    if category:
        filtered_courses = [course for course in filtered_courses if course["category"].lower() == category.lower()]
    if min_price is not None:
        filtered_courses = [course for course in filtered_courses if course["price"] >= min_price]
    if max_price is not None:
        filtered_courses = [course for course in filtered_courses if course["price"] <= max_price]
    if active is not None:
        filtered_courses = [course for course in filtered_courses if course["active"] == active]
    return {"courses": filtered_courses}