from .logger import logging
from .employees import find_employee
from .salary import *
from .tax import calculate_tax


def generate_payslip(employee_id:int) -> str:
    logging.info(f"Generating payslip for employee id: {employee_id}")
    try:
        employee = find_employee(employee_id)
        if not employee:
            logging.warning(f"Employee with id {employee_id} not found.")
            return "Employee not found."
        else:
            logging.info(f"Employee found: {employee}")
            basic_salary = employee["salary"]
            bonus, gross_salary, tax, net_salary = calculate_salary(basic_salary)

        with open("payroll.csv", "a") as file:
            file.write(f"{employee_id},{employee['name']},{basic_salary},{bonus},{gross_salary},{tax},{net_salary}\n")
            logging.info("Payslip written to payroll.csv successfully.")

            payslip = f"""
Payslip for {employee["name"]}
{"-" * 50}
Basic Salary: ${basic_salary:.2f}
Bonus: ${bonus:.2f}
Gross Salary: ${gross_salary:.2f}
Tax: ${tax:.2f}
Net Salary: ${net_salary:.2f}
"""
        logging.info("Payslip generated successfully.")
        return payslip
    except Exception as e:
        logging.error(f"Error occurred while generating payslip: {e}")
        return "Error generating payslip."