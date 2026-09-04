from student.student_operations import *
from student.file_operations import *

students = {
    1001 : {
        "student_id": 1001,
        "name": "vineet",
        "age": 21,
        "course": "BS",
        "email_id": "vineet@aiwithvineet.in"
    },
    1002: {
        "student_id": 1002,
        "name": "rohit",
        "age": 23,
        "course": "BE",
        "email_id": "rohit@aiwithvineet.in"
    },
    1003: {
        "student_id": 1003,
        "name": "virat",
        "age": 22,
        "course": "B.Tech",
        "email_id": "virat@aiwithvineet.in"        
    }
}




def main():
    while True:
        print("\nStudent Management System")
        print("1. Add Student")
        print("2. Remove Student")
        print("3. Update Student")
        print("4. Search Student")
        print("5. Display All Students")
        print("6. Check Student Exists")
        print("7. Save Students to File")
        print("8. Exit")

        choice = int(input("Enter your choice (1-8): "))
        try:
            choice = int(choice)
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 8.")
            continue
        else:
            if choice == 1:
                add_student(students)
            elif choice == 2:
                remove_student(students)
            elif choice == 3:
                update_student(students)
            elif choice == 4:
                search_student(students)
            elif choice == 5:
                display_students(students)
            elif choice == 6:
                student_id = int(input("Enter student ID to check: "))
                check_student_exists(students, student_id)
            elif choice == 7:
                save_students_to_file(students)
            elif choice == 8:
                print("Exiting the Student Management System.")
                break
            else:
                print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()