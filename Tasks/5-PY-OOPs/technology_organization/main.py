# LEVEL 1 - PERSON
class Person:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city

    def display_person(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"City: {self.city}")



# LEVEL 2 - EMPLOYEE
class Employee(Person):
    def __init__(self, name, age, city, employee_id, salary, company):
        super().__init__(name, age, city)
        self.employee_id = employee_id
        self.salary = salary
        self.company = company

    def display_employee(self):
        print(f"Employee ID: {self.employee_id}")
        print(f"Salary: {self.salary}")
        print(f"Company: {self.company}")



# LEVEL 3 - DEVELOPER
class Developer(Employee):
    def __init__(self, name, age, city, employee_id, salary, company, language, framework, experience):
        super().__init__(name, age, city, employee_id, salary, company)
        self.language = language
        self.framework = framework
        self.experience = experience

    def display_developer(self):
        print(f"Programming Language: {self.language}")
        print(f"Framework: {self.framework}")
        print(f"Experience: {self.experience} years")




# Create 5 Developer Objects
developer1 = Developer("Vineet", 25, "Mumbai", "E001", 80000, "TechCorp", "Python", "LangGraph", 3)
developer2 = Developer("Amit", 30, "Delhi", "E002", 90000, "CodeWorks", "JavaScript", "React", 5)
developer3 = Developer("Priya", 28, "Bangalore", "E003", 85000, "DevSolutions", "Java", "Spring", 4)
developer4 = Developer("Rohit", 32, "Hyderabad", "E004", 95000, "SoftTech", "C#", ".NET", 6)
developer5 = Developer("Sneha", 27, "Pune", "E005", 87000, "Innovatech", "Ruby", "Rails", 3)


# DEMONSTRATE DEVELOPER 1
print("\nDeveloper 1")
print("\nPerson level:")
developer1.display_person()
print("\nEmployee level:")
developer1.display_employee()
print("\nDeveloper level:")
developer1.display_developer()




# DEMONSTRATE ALL FIVE DEVELOPERS
developers = [developer1, developer2, developer3, developer4, developer5]
print("\nAll Developers")
for developer in developers:
    print("\n", "-"*50)
    developer.display_person()
    developer.display_employee()
    developer.display_developer()





# DEMONSTRATE INHERITED PROPERTIES
print("\nINHERITED PROPERTIES")
print("\nDeveloper 1 Name:", developer1.name)
print("Developer 1 Age:", developer1.age)
print("Developer 1 City:", developer1.city)
print("Developer 1 Employee ID:", developer1.employee_id)
print("Developer 1 Salary:", developer1.salary)
print("Developer 1 Company:", developer1.company)
print("Developer 1 Programming Language:", developer1.language)
print("Developer 1 Framework:", developer1.framework)
print("Developer 1 Experience:", developer1.experience, "years")