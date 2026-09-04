from .logger import logging



def save_students_to_file(students: dict, file_path: str = "students.txt") -> None:
    try:
        with open(file_path, "w") as file:
            for student_id, student in students.items():
                file.write(f"Student ID: {student_id}, Name: {student['name']}, Age: {student['age']}, Course: {student['course']}, Email: {student['email_id']}\n")
        logging.info("Students saved to file successfully.")
        print("Students saved to file successfully.")
    except Exception as e:
        logging.exception("Unexpected error while saving students to file: ", e)
        print("An unexpected error occurred while saving students to file.")


