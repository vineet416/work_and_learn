import numpy as np
from app.data import students


# CREATE NUMPY ARRAYS
student_ids = np.array([student["student_id"] for student in students])
names = np.array([student["name"] for student in students])
python_marks = np.array([student["python"] for student in students])
mathematics_marks = np.array([student["mathematics"] for student in students])
data_science_marks = np.array([student["data_science"] for student in students])


# SUBJECT AVERAGES
python_average = np.mean(python_marks)
mathematics_average = np.mean(mathematics_marks)
data_science_average = np.mean(data_science_marks)


# OVERALL AVERAGES
overall_averages = (python_marks + mathematics_marks + data_science_marks) / 3
overall_average = np.mean(overall_averages)


# HIGHEST AND LOWEST MARKS
highest_marks = {
    "python": int(np.max(python_marks)),
    "mathematics": int(np.max(mathematics_marks)),
    "data_science": int(np.max(data_science_marks))
}

lowest_marks = {
    "python": int(np.min(python_marks)),
    "mathematics": int(np.min(mathematics_marks)),
    "data_science": int(np.min(data_science_marks))
}


# TOP STUDENT
top_index = np.argmax(overall_averages)
top_student = students[top_index].copy()
top_student["overall_average"] = round(float(overall_averages[top_index]), 2)


# PASS / FAIL
# Passing criteria: At least 40 marks in every subject.
passed_mask = ((python_marks >= 40) & (mathematics_marks >= 40) & (data_science_marks >= 40))
passed_students = [students[i] for i in range(len(students)) if passed_mask[i]]
failed_students = [students[i] for i in range(len(students)) if not passed_mask[i]]