from database import SessionLocal
from models import Student, Course, Enrollment, StudentUpdate, CourseUpdate, EnrollmentUpdate
from fastapi import FastAPI, HTTPException
from sqlalchemy import text


# Create FastAPI instance
app = FastAPI()

# Home API endpoint
@app.get("/")
def home():
    return {"message": "Welcome to the Student Course API"}


# API endpoint to get all students from the database
@app.get("/students")
def get_students():
    session = SessionLocal()
    try:
        students = session.execute(text("SELECT * FROM students")).fetchall()
        return {"students": [dict(student._mapping) for student in students]}
    finally:
        session.close()


# API endpoint to get all courses from the database
@app.get("/courses")
def get_courses():
    session = SessionLocal()
    try:
        courses = session.execute(text("SELECT * FROM courses")).fetchall()
        return {"courses": [dict(course._mapping) for course in courses]}
    finally:
        session.close()


# API endpoint to get all enrollments from the database
@app.get("/enrollments")
def get_enrollments():
    session = SessionLocal()
    try:
        enrollments = session.execute(text("SELECT * FROM enrollments")).fetchall()
        return {"enrollments": [dict(enrollment._mapping) for enrollment in enrollments]}
    finally:
        session.close()


# API endpoint to create a new student in the database
@app.post("/create_student")
def create_student(student: Student):
    session = SessionLocal()
    try:
        session.execute(
            text("INSERT INTO students (name, email, age) VALUES (:name, :email, :age)"),
            {"name": student.name, "email": student.email, "age": student.age},
        )
        session.commit()
        return {"message": "Student created successfully"}
    finally:
        session.close()


# API endpoint to create a new course in the database
@app.post("/create_course")
def create_course(course: Course):
    session = SessionLocal()
    try:
        session.execute(
            text("""INSERT INTO courses (title, description, price, duration, instructor, category, rating, active)
                    VALUES (:title, :description, :price, :duration, :instructor, :category, :rating, :active)"""),
            {
                "title": course.title,
                "description": course.description,
                "price": course.price,
                "duration": course.duration,
                "instructor": course.instructor,
                "category": course.category,
                "rating": course.rating,
                "active": course.active,
            },
        )
        session.commit()
        return {"message": "Course created successfully"}
    finally:
        session.close()


# API endpoint to enroll a student in a course
@app.post("/enroll_student")
def enroll_student(enrollment: Enrollment):
    session = SessionLocal()
    try:
        session.execute(
            text("""INSERT INTO enrollments (student_id, course_id, status) 
            VALUES (:student_id, :course_id, :status)"""),
            {
                "student_id": enrollment.student_id,
                "course_id": enrollment.course_id,
                "status": enrollment.status,
            },
        )
        session.commit()
        return {"message": "Student enrolled successfully"}
    finally:
        session.close()


# API endpoint to update a student's record in the database
@app.patch("/update_student/{student_id}")
def update_student(student_id: int, student_update: StudentUpdate):
    session = SessionLocal()
    try:
        if student_id not in [s.id for s in session.execute(text("SELECT id FROM students")).fetchall()]:
            raise HTTPException(status_code=404, detail="Student not found")
        update_data = student_update.model_dump(exclude_unset=True)
        if not update_data:
            raise HTTPException(status_code=404, detail="No fields provided for update")
        session.execute(
            text(f"""UPDATE students SET 
            {", ".join(f"{key} = :{key}" for key in update_data.keys())}
             WHERE id = :student_id"""),
            {**update_data, "student_id": student_id}
        )
        session.commit()
        return {"message": "Student updated successfully"}
    finally:
        session.close()


# API endpoint to update a course's record in the database
@app.patch("/update_course/{course_id}")
def update_course(course_id: int, course_update: CourseUpdate):
    session = SessionLocal()
    try:
        if course_id not in [c.id for c in session.execute(text("SELECT id FROM courses")).fetchall()]:
            raise HTTPException(status_code=404, detail="Course not found")
        update_data = course_update.model_dump(exclude_unset=True)
        if not update_data:
            raise HTTPException(status_code=404, detail="No fields provided for update")
        session.execute(
            text(f"""UPDATE courses SET 
            {", ".join(f"{key} = :{key}" for key in update_data.keys())}
             WHERE id = :course_id"""),
            {**update_data, "course_id": course_id},
        )
        session.commit()
        return {"message": "Course updated successfully"}
    finally:
        session.close()


# API endpoint to update an enrollment's record in the database
@app.patch("/update_enrollment/{enrollment_id}")
def update_enrollment(enrollment_id: int, enrollment_update: EnrollmentUpdate):
    session = SessionLocal()
    try:
        if enrollment_id not in [e.id for e in session.execute(text("SELECT id FROM enrollments")).fetchall()]:
            raise HTTPException(status_code=404, detail="Enrollment not found")
        update_data = enrollment_update.model_dump(exclude_unset=True)
        if not update_data:
            raise HTTPException(status_code=404, detail="No fields provided for update")
        session.execute(
            text(f"""UPDATE enrollments SET 
            {", ".join(f"{key} = :{key}" for key in update_data.keys())}
             WHERE id = :enrollment_id"""),
            {**update_data, "enrollment_id": enrollment_id},
        )
        session.commit()
        return {"message": "Enrollment updated successfully"}
    finally:
        session.close()


# API endpoint to delete a student from the database
@app.delete("/delete_student/{student_id}")
def delete_student(student_id: int):
    session = SessionLocal()
    try:
        if student_id not in [s.id for s in session.execute(text("SELECT id FROM students")).fetchall()]:
            raise HTTPException(status_code=404, detail="Student not found")
        session.execute(text("DELETE FROM students WHERE id = :student_id"), {"student_id": student_id})
        session.commit()
        return {"message": "Student deleted successfully"}
    finally:
        session.close()


# API endpoint to delete a course from the database
@app.delete("/delete_course/{course_id}")
def delete_course(course_id: int):
    session = SessionLocal()
    try:
        if course_id not in [c.id for c in session.execute(text("SELECT id FROM courses")).fetchall()]:
            raise HTTPException(status_code=404, detail="Course not found")
        session.execute(text("DELETE FROM courses WHERE id = :course_id"), {"course_id": course_id})
        session.commit()
        return {"message": "Course deleted successfully"}
    finally:
        session.close()


# API endpoint to delete an enrollment from the database
@app.delete("/delete_enrollment/{enrollment_id}")
def delete_enrollment(enrollment_id: int):
    session = SessionLocal()
    try:
        if enrollment_id not in [e.id for e in session.execute(text("SELECT id FROM enrollments")).fetchall()]:
            raise HTTPException(status_code=404, detail="Enrollment not found")
        session.execute(text("DELETE FROM enrollments WHERE id = :enrollment_id"), {"enrollment_id": enrollment_id})
        session.commit()
        return {"message": "Enrollment deleted successfully"}
    finally:
        session.close()


# API endpoint to get student by ID from the database
@app.get("/students/{student_id}")
def get_student_by_id(student_id: int):
    session = SessionLocal()
    try:
        student = session.execute(text("SELECT * FROM students WHERE id = :student_id"), {"student_id": student_id}).fetchone()
        if not student:
            raise HTTPException(status_code=404, detail="Student not found")
        return {"student": dict(student._mapping)}
    finally:
        session.close()


# API endpoint to get course by ID from the database
@app.get("/courses/{course_id}")
def get_course_by_id(course_id: int):
    session = SessionLocal()
    try:
        course = session.execute(text("SELECT * FROM courses WHERE id = :course_id"), {"course_id": course_id}).fetchone()
        if not course:
            raise HTTPException(status_code=404, detail="Course not found")
        return {"course": dict(course._mapping)}
    finally:
        session.close()


# API endpoint to get enrollment by ID from the database
@app.get("/enrollments/{enrollment_id}")
def get_enrollment_by_id(enrollment_id: int):
    session = SessionLocal()
    try:
        enrollment = session.execute(text("SELECT * FROM enrollments WHERE id = :enrollment_id"), {"enrollment_id": enrollment_id}).fetchone()
        if not enrollment:
            raise HTTPException(status_code=404, detail="Enrollment not found")
        return {"enrollment": dict(enrollment._mapping)}
    finally:
        session.close()