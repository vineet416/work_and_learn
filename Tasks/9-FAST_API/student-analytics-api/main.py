from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from app.data import students
from app.analysis import *
from app.visualization import create_subject_average_chart, create_top_five_chart

# FastAPI instance
app = FastAPI()

# 1. ALL STUDENTS
@app.get("/students")
def get_students():
    return {"count": len(students), "students": students}


# 2. STUDENT DETAILS
@app.get("/student/{student_id}")
def get_student(student_id: int):
    for student in students:
        if student["student_id"] == student_id:
            return student
    raise HTTPException(status_code=404, detail="Student not found")


# 3. PYTHON AVERAGE
@app.get("/average/python")
def get_python_average():
    return {"subject": "Python", "average": round(float(python_average), 2)}


# 4. MATHEMATICS AVERAGE
@app.get("/average/mathematics")
def get_mathematics_average():
    return {"subject": "Mathematics", "average": round(float(mathematics_average), 2)}


# 5. DATA SCIENCE AVERAGE
@app.get("/average/data-science")
def get_data_science_average():
    return {"subject": "Data Science", "average": round(float(data_science_average), 2)}


# 6. TOP STUDENT
@app.get("/topper")
def get_topper():
    return top_student


# 7. PASSED STUDENTS
@app.get("/passed")
def get_passed_students():
    return {"passing_criteria": "40 or above in every subject", "count": len(passed_students), "students": passed_students}


# 8. FAILED STUDENTS
@app.get("/failed")
def get_failed_students():
    return {"passing_criteria": "40 or above in every subject", "count": len(failed_students), "students": failed_students}


# 9. STATISTICS
@app.get("/statistics")
def get_statistics():
    return {
        "subject_averages": {
            "python": round(float(python_average), 2),
            "mathematics": round(float(mathematics_average), 2),
            "data_science": round(float(data_science_average), 2)
},
        "highest_marks": highest_marks,
        "lowest_marks": lowest_marks,
        "overall_average": round(float(overall_average), 2)
    }


# 10. SUBJECT AVERAGE VISUALIZATION
@app.get("/visualization/subject-averages")
def subject_average_visualization():
    fig = create_subject_average_chart()
    return HTMLResponse(content=fig, status_code=200)


# 11. TOP FIVE VISUALIZATION
@app.get("/visualization/top-five")
def top_five_visualization():
    fig = create_top_five_chart()
    return HTMLResponse(content=fig, status_code=200)