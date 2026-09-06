from user import USER
from course import COURSE

class INSTRUCTOR(USER):
    def __init__(self, user_id, username, email):
        super().__init__(user_id, username, email)
        self.course = []

    def create_course(self, course_id, title, category):
        if course_id in [course.course_id for course in self.course]:
            print(f"Course ID {course_id} already exists.")
        else:
            course = COURSE(course_id, title, category)
            self.course.append(course)
            print(f"Course '{title}' has been created by {self.username}.")
            return course


    def display_courses(self):
        if not self.course:
            print(f"{self.username} is not teaching any courses.")
        else:
            print(f"{self.username}'s Courses:")
            for course in self.course:
                course.display_course_info()


    