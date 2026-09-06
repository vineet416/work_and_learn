from user import USER


class STUDENT(USER):
    def __init__(self, user_id, username, email):
        super().__init__(user_id, username, email)
        self.enrolled_courses = {}

    def enroll_course(self, course):
        if course.course_id in self.enrolled_courses:
            print(f"{self.username} is already enrolled in {course.title}.")
        else:
            self.enrolled_courses[course.course_id] = {"course": course, "progress": 0}
            print(f"{self.username} has enrolled in {course.title}.")


    def view_enrolled_courses(self):
        if not self.enrolled_courses:
            print(f"{self.username} is not enrolled in any courses.")
        else:
            print(f"{self.username}'s Enrolled Courses:")
            for course_info in self.enrolled_courses.values():
                course = course_info["course"]
                progress = course_info["progress"]
                course.display_course_info()
                print(f"Progress: {progress}%")


    def check_progress(self, course_id):
        if course_id in self.enrolled_courses:
            progress = self.enrolled_courses[course_id]["progress"]
            print(f"{self.username}'s progress in course ID {course_id}: {progress}%")
        else:
            print(f"{self.username} is not enrolled in course ID {course_id}.")


    def update_progress(self, course_id, progress):
        if course_id in self.enrolled_courses:
            if 0 <= progress <= 100:
                self.enrolled_courses[course_id]["progress"] = progress
                print(f"{self.username}'s progress in course ID {course_id} has been updated to {progress}%.")
            else:
                print("Progress must be between 0 and 100.")
        else:
            print(f"{self.username} is not enrolled in course ID {course_id}.")