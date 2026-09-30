from database import driver, close_connection
from operations import create_student, create_relationship, read_students, search_students_by_city, update_student_city, delete_relationship, delete_student
from models import Course, Student, UpdateCity, Relationship
from fastapi import FastAPI

def create_course(name):
    query = """
    CREATE (c:Course {
        name: $name
    })
    RETURN c
    """
    with driver.session() as session:
        result = session.run(query, name=name)
        record = result.single()
        if record:
            return {"message": "Course created:", "course": record["c"]}


app = FastAPI()

# Create a new course
@app.post("/courses/")
def create_course_endpoint(name: Course):
    message = create_course(name.name)
    return message


# Create a new student
@app.post("/students/")
def create_student_endpoint(student: Student):
    message = create_student(student.name, student.age, student.city)
    return message


# Create a relationship between a student and a course
@app.post("/relationships/")
def create_relationship_endpoint(relationship: Relationship):
    message = create_relationship(relationship.student_name, relationship.course_name)
    return message


# Read all students
@app.get("/students/")
def read_students_endpoint():
    message = read_students()
    return message


# Search students by city
@app.get("/students/search/{city}")
def search_students_by_city_endpoint(city: str):
    message = search_students_by_city(city)
    return message


# Update a student's city
@app.put("/students/update_city/")
def update_student_city_endpoint(update_city: UpdateCity):
    message = update_student_city(update_city.name, update_city.new_city)
    return message


# Delete a relationship between a student and a course
@app.delete("/relationships/")
def delete_relationship_endpoint(relationship: Relationship):
    message = delete_relationship(relationship.student_name, relationship.course_name)
    return message


# Delete a student
@app.delete("/students/{name}")
def delete_student_endpoint(name: str):
    message = delete_student(name)
    return message
