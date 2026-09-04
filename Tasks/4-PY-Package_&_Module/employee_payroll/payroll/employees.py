from .logger import logging

def add_employee(id: int, name: str, department: str, salary: int) -> str:
    logging.info(f"Adding employee: {id}, {name}, {department}, {salary}")
    try:
        with open("employees.csv", "a") as file:
            file.write(f"\n{id},{name},{department},{salary}")
        logging.info("Employee added successfully.")
        return f"Employee {name} added successfully."
    except Exception as e:
        logging.error(f"Error occurred while adding employee: {e}")
        return "Error adding employee. Please try again."



def get_all_employees() -> list:
    logging.info("Retrieving all employees.")
    employees = []
    try:
        with open("employees.csv", "r") as file:
            for line in file:
                id, name, department, salary = line.strip().split(",")
                employees.append({
                    "id": int(id),
                    "name": name,
                    "department": department,
                    "salary": float(salary)
                })
        logging.info("Employees retrieved successfully.")
        return employees
    except FileNotFoundError:
        logging.warning("No employees found. The file does not exist.")
    except Exception as e:
        logging.error(f"Error occurred while retrieving employees: {e}")




def find_employee(id: int) -> dict:
    logging.info(f"Searching for employee with ID: {id}")
    try:
        with open("employees.csv", "r") as file:
            for line in file:
                emp_id, name, department, salary = line.strip().split(",")
                if int(emp_id) == id:
                    logging.info("Employee found.")
                    return {
                        "id": int(emp_id),
                        "name": name,
                        "department": department,
                        "salary": float(salary)
                    }
            logging.info(f"Employee with ID {id} not found.")
            return {}
    except FileNotFoundError:
        logging.warning("No employees found. The file does not exist.")
    except Exception as e:
        logging.error(f"Error occurred while searching for employee: {e}")