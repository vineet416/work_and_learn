from .logger import logging
from .tax import calculate_tax

def calculate_bonus(salary: float, bonus_percentage: float = 10.0) -> float:
    logging.info(f"Calculating bonus for salary: {salary} with bonus percentage: {bonus_percentage}")
    try:
        bonus = salary * (bonus_percentage / 100)
        logging.info(f"Calculated bonus: {bonus}")
        return bonus
    except Exception as e:
        logging.error(f"Error occurred while calculating bonus: {e}")
        return 0.0


def calculate_gross_salary(salary: float, bonus: float) -> float:
    logging.info(f"Calculating gross salary for salary: {salary} with bonus: {bonus}")
    try:
        gross_salary = salary + bonus
        logging.info(f"Calculated gross salary: {gross_salary}")
        return gross_salary
    except Exception as e:
        logging.error(f"Error occurred while calculating gross salary: {e}")
        return 0.0



def calculate_salary(salary: float, bonus_percentage: float = 10.0) -> tuple:
    logging.info(f"Calculating final salary for salary: {salary}, bonus percentage: {bonus_percentage}")
    try:
        bonus = calculate_bonus(salary, bonus_percentage)
        gross_salary = calculate_gross_salary(salary, bonus)
        tax = calculate_tax(gross_salary)
        net_salary = gross_salary - tax
        logging.info(f"Calculated final salary: {net_salary}")
        return bonus, gross_salary, tax, net_salary
    except Exception as e:
        logging.error(f"Error occurred while calculating final salary: {e}")
        return 0.0, 0.0, 0.0, 0.0