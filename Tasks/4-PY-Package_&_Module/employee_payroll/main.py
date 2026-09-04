from payroll.logger import logging
from payroll.employees import *
from payroll.salary import *
from payroll.tax import *
from payroll.payslip import *


def main():
    logging.info("Starting the payroll system.")
    while True:
        print("\nEmployee Payroll System")
        print("1. Add Employee")
        print("2. View All Employees")
        print("3. Find Employee by ID")
        print("4. Generate Payslip")
        print("5. Exit")

        try:
            choice = int(input("Enter your choice: "))
            if choice >0 and choice <6:
                logging.info(f"User selected option: {choice}")
        except ValueError:
            logging.warning("Invalid input. Please enter a number between 1 and 5.")
            print("Invalid input. Please enter a number between 1 and 5.")
            continue
        else:
            if choice == 1:
                id = int(input("Enter employee ID: "))
                name = input("Enter employee name: ")
                department = input("Enter employee department: ")
                salary = int(input("Enter employee salary: "))
                result = add_employee(id, name, department, salary)
                print(result)

            elif choice == 2:
                employees = get_all_employees()
                if employees:
                    for emp in employees:
                        print(emp)
                else:
                    print("No employees found.")

            elif choice == 3:
                id = int(input("Enter employee ID to find: "))
                employee = find_employee(id)
                if employee:
                    print(employee)
                else:
                    print(f"Employee with ID {id} not found.")

            elif choice == 4:
                id = int(input("Enter employee ID to generate payslip: "))
                payslip = generate_payslip(id)
                print(payslip)

            elif choice == 5:
                logging.info("Exiting the payroll system.")
                break

            else:
                logging.warning(f"Invalid choice: {choice}")
                print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()