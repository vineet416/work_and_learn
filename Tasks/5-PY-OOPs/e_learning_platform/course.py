class COURSE:
    def __init__(self, course_id, title, category):
        self.course_id = course_id
        self.title = title
        self.category = category


    def display_course_info(self):
        print(f"Course ID: {self.course_id}")
        print(f"Title: {self.title}")
        print(f"Category: {self.category}")