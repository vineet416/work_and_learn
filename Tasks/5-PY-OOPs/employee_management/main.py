# PARENT CLASS
class Employee:
    def __init__(self, employee_id, name, salary,department):
        self.employee_id = employee_id
        self.name = name
        self.salary = salary
        self.department = department

    def display_details(self):
        print(f"Employee ID: {self.employee_id}")
        print(f"Name: {self.name}")
        print(f"Salary: {self.salary}")
        print(f"Department: {self.department}")

    def calculate_salary(self):
        return self.salary



# CHILD CLASS - DEVELOPER
class Developer(Employee):
    def __init__(self, employee_id, name, salary, department, programming_language):
        super().__init__(employee_id, name, salary, department)
        self.programming_language = programming_language

    def display_details(self):
        super().display_details()
        print(f"Programming Language: {self.programming_language}")




# CHILD CLASS - MANAGER
class Manager(Employee):
    def __init__(self, employee_id, name, salary, department, team_size):
        super().__init__(employee_id, name, salary, department)
        self.team_size = team_size

    def display_details(self):
        super().display_details()
        print(f"Team Size: {self.team_size}")



# CHILD CLASS - HR
class HR(Employee):
    def __init__(self, employee_id, name, salary, department, region):
        super().__init__(employee_id, name, salary, department)
        self.region = region

    def display_details(self):
        super().display_details()
        print(f"Region: {self.region}")




# CREATE DEVELOPER OBJECTS
developer1 = Developer(101, "Aarav", 75000, "Technology", "Python")
developer2 = Developer(102, "Priya", 85000, "Technology", "Java")

# CREATE MANAGER OBJECTS
manager1 = Manager(201, "Rahul", 110000, "Management", 8)
manager2 = Manager(202, "Sneha", 125000, "Management", 12)

# CREATE HR OBJECTS
hr1 = HR(301, "Neha", 70000, "Human Resources", "West")
hr2 = HR(302, "Karan", 78000, "Human Resources", "South")



# DISPLAY DEVELOPERS
print("\nDEVELOPER 1")
developer1.display_details()
print(f"Calculated Salary: ₹{developer1.calculate_salary():,.2f}")

print("\n", "-"*50)
print("DEVELOPER 2")
developer2.display_details()
print(f"Calculated Salary: ₹{developer2.calculate_salary():,.2f}")



# DISPLAY MANAGERS
print("\n", "-"*50)
print("MANAGER 1")
manager1.display_details()
print(f"Calculated Salary: ₹{manager1.calculate_salary():,.2f}")

print("\n", "-"*50)
print("MANAGER 2")
manager2.display_details()
print(f"Calculated Salary: ₹{manager2.calculate_salary():,.2f}")



# DISPLAY HR
print("\n", "-"*50)
print("HR 1")
hr1.display_details()
print(f"Calculated Salary: ₹{hr1.calculate_salary():,.2f}")

print("\n", "-"*50)
print("HR 2")
hr2.display_details()
print(f"Calculated Salary: ₹{hr2.calculate_salary():,.2f}")



# DEMONSTRATE INHERITED PROPERTIES
print("\n", "-"*50)
print("INHERITED PROPERTIES")
print("Developer Name:", developer1.name)
print("Developer Salary:", developer1.salary)
print("Developer Department:", developer1.department)



# DEMONSTRATE CHILD-SPECIFIC ATTRIBUTES
print("\n", "-"*50)
print("CHILD-SPECIFIC ATTRIBUTES")
print("Developer Programming Language:", developer1.programming_language)
print("Manager Team Size:", manager1.team_size)
print("HR Region:", hr1.region)