from .logger import logging


def add_student(students: dict):
    try:
        student_id = int(input("Enter student ID: "))

        if student_id in students:
            logging.warning(f"Student with ID: {student_id} already exists.")
            print(f"Student with ID {student_id} already exists.")
        else:
            name = input("Enter student name: ").strip()
            age = int(input("Enter student age: "))
            course = input("Enter student course: ").strip()
            email_id = input("Enter student email: ").strip()
            students[student_id] = {
                "student_id": student_id,
                "name": name,
                "age": age,
                "course": course,
                "email_id": email_id
            }
            logging.info(f"Student added successfully. Student ID: {student_id}, Name: {name}")
            print(f"Student {name} added successfully.")

    except ValueError:
        logging.error("Invalid input while adding student.")
        print("Invalid input. Student ID and age must be numbers.")

    except Exception as e:
        logging.exception("Unexpected error while adding student: ", e)
        print("An unexpected error occurred while adding the student.")





def remove_student(students: dict):
    try:
        student_id = int(input("Enter student ID to remove: "))
        if student_id in students:
            removed_student = students.pop(student_id)
            logging.info(f"Student removed successfully. Student ID: {student_id}, Name: {removed_student['name']}")
            print(f"Student {removed_student['name']} removed successfully.")
        else:
            logging.warning(f"Student with ID: {student_id} does not exist.")
            print(f"Student with ID {student_id} does not exist.")

    except ValueError:
        logging.error("Invalid input while removing student.")
        print("Invalid input. Student ID must be a number.")

    except Exception as e:
        logging.exception("Unexpected error while removing student: ", e)
        print("An unexpected error occurred while removing the student.")




def update_student(students: dict):
    try:
        student_id = int(input("Enter student ID to update: "))
        if student_id in students:
            name = input("Enter new student name: ").strip()
            age = int(input("Enter new student age: "))
            course = input("Enter new student course: ").strip()
            email_id = input("Enter new student email: ").strip()
            students[student_id].update({
                "name": name,
                "age": age,
                "course": course,
                "email_id": email_id
            })
            logging.info(f"Student updated successfully. Student ID: {student_id}, Name: {name}")
            print(f"Student {name} updated successfully.")
        else:
            logging.warning(f"Student with ID: {student_id} does not exist.")
            print(f"Student with ID {student_id} does not exist.")

    except ValueError:
        logging.error("Invalid input while updating student.")
        print("Invalid input. Student ID and age must be numbers.")

    except Exception as e:
        logging.exception("Unexpected error while updating student: ", e)
        print("An unexpected error occurred while updating the student.")




def search_student(students: dict):
    try:
        student_id = int(input("Enter student ID to search: "))
        if student_id in students:
            student = students[student_id]
            logging.info(f"Student found. Student ID: {student_id}, Name: {student['name']}")
            print(f"Student found: {student}")
        else:
            logging.warning(f"Student with ID: {student_id} does not exist.")
            print(f"Student with ID {student_id} does not exist.")

    except ValueError:
        logging.error("Invalid input while searching for student.")
        print("Invalid input. Student ID must be a number.")

    except Exception as e:
        logging.exception("Unexpected error while searching for student: ", e)
        print("An unexpected error occurred while searching for the student.")




def check_student_exists(students: dict, student_id: int) -> bool:
    exists = student_id in students
    if exists:
        logging.info(f"Student with ID: {student_id} exists.")
        print(f"Student with ID {student_id} exists.")
    else:
        logging.info(f"Student with ID: {student_id} does not exist.")
        print(f"Student with ID {student_id} does not exist.")
    return exists




def display_students(students: dict):
    if students:
        logging.info("Displaying all students.")
        for student_id, student in students.items():
            print(f"Student ID: {student_id}, Name: {student['name']}, Age: {student['age']}, Course: {student['course']}, Email: {student['email_id']}")
    else:
        logging.info("No students to display.")
        print("No students found.")





