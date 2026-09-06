from instructor import INSTRUCTOR
from student import STUDENT


instructor1 = INSTRUCTOR(user_id=1, username="Sudhanshu", email="sudhanshu@euron.one")
instructor2 = INSTRUCTOR(user_id=2, username="Priya Sharma", email="priya@euron.one")

course1 = instructor1.create_course(course_id=101, title="Python Programming", category="Programming")
course2 = instructor1.create_course(course_id=102, title="Machine Learning", category="Artificial Intelligence")
course3 = instructor2.create_course(course_id=201, title="Data Analysis", category="Data Science")
course4 = instructor2.create_course(course_id=202, title="Web Development", category="Programming")

student1 = STUDENT(user_id=1, username="Vineet Patel", email="vineet@aiwithvineet.in")
student2 = STUDENT(user_id=2, username="Ananya Singh", email="ananya@aiwithvineet.in")


print("\n--- Online Learning Platform ---")


def main():
    while True:
        print("\nMenu:")
        print("1. Instructor: Create Course")
        print("2. Instructor: Display Courses")
        print("3. Student: Enroll in Course")
        print("4. Student: View Enrolled Courses")
        print("5. Student: Update Progress")
        print("6. Student: Check Progress")
        print("7. Exit")

        choice = int(input("Enter your choice (1-7): "))

        if choice == 1:
            print("\n"+"-"*50)
            instructor_id = int(input("Enter Instructor ID (1 or 2): "))
            if instructor_id == 1:
                instructor = instructor1
            elif instructor_id == 2:
                instructor = instructor2
            else:
                print("Invalid Instructor ID.")
                continue

            course_id = int(input("Enter Course ID: "))
            title = input("Enter Course Title: ")
            category = input("Enter Course Category: ")
            instructor.create_course(course_id, title, category)
            print("\n"+"-"*50)


        elif choice == 2:
            print("\n"+"-"*50)  
            instructor_id = int(input("Enter Instructor ID (1 or 2): "))
            if instructor_id == 1:
                instructor = instructor1
            elif instructor_id == 2:
                instructor = instructor2
            else:
                print("Invalid Instructor ID.")
                continue

            instructor.display_courses()
            print("\n"+"-"*50)


        elif choice == 3:
            print("\n"+"-"*50)
            student_id = int(input("Enter Student ID (1 or 2): "))
            if student_id == 1:
                student = student1
            elif student_id == 2:
                student = student2
            else:
                print("Invalid Student ID.")
                continue

            course_id = int(input("Enter Course ID to enroll: "))
            course = None
            for instructor in [instructor1, instructor2]:
                for c in instructor.course:
                    if c.course_id == course_id:
                        course = c
                        break
                if course:
                    break

            if course:
                student.enroll_course(course)
            else:
                print(f"Course ID {course_id} not found.")
            print("\n"+"-"*50)

        elif choice == 4:
            print("\n"+"-"*50)
            student_id = int(input("Enter Student ID (1 or 2): "))
            if student_id == 1:
                student = student1
            elif student_id == 2:
                student = student2
            else:
                print("Invalid Student ID.")
                continue

            student.view_enrolled_courses()
            print("\n"+"-"*50)


        elif choice == 5:
            print("\n"+"-"*50)
            student_id = int(input("Enter Student ID (1 or 2): "))
            if student_id == 1:
                student = student1
            elif student_id == 2:
                student = student2
            else:
                print("Invalid Student ID.")
                continue

            course_id = int(input("Enter Course ID to update progress: "))
            progress = int(input("Enter new progress (0-100): "))
            student.update_progress(course_id, progress)
            print("\n"+"-"*50)


        elif choice == 6:
            print("\n"+"-"*50)
            student_id = int(input("Enter Student ID (1 or 2): "))
            if student_id == 1:
                student = student1
            elif student_id == 2:
                student = student2
            else:
                print("Invalid Student ID.")
                continue

            course_id = int(input("Enter Course ID to check progress: "))
            student.check_progress(course_id)
            print("\n"+"-"*50)


        elif choice == 7:
            print("\n"+"-"*50)
            print("Exiting the program.")
            print("\n"+"-"*50)
            break


        else:
            print("\n"+"-"*50)
            print("Invalid choice. Please try again.")
            print("\n"+"-"*50)



if __name__ == "__main__":
    main()