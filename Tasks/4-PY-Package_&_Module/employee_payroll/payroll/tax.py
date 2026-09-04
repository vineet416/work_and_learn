from .logger import logging


def calculate_tax(salary: float) -> float:
    logging.info(f"Calculating tax for salary: {salary}")
    try:
        if salary <= 10000:
            tax = 0.0
        elif salary <= 20000:
            tax = (salary - 10000) * 0.1
        elif salary <= 50000:
            tax = (salary - 20000) * 0.2 + 1000
        else:
            tax = (salary - 50000) * 0.3 + 7000
        logging.info(f"Calculated tax: {tax}")
        return tax
    except Exception as e:
        logging.error(f"Error occurred while calculating tax: {e}")
        return 0.0

    