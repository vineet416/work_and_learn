from .logger import logging
from datetime import datetime


def validate_input(choice: int) -> bool:
    logging.info(f"Validating user input: {choice}")
    if isinstance(choice, int) and 1 <= choice <= 9:
        logging.info("User input is valid.")
        return True
    else:
        logging.warning("Invalid user input. It must be an integer between 1 and 9.")
        return False


def validate_expense_id(expense_id: int) -> bool:
    logging.info(f"Validating expense ID: {expense_id}")
    if isinstance(expense_id, int) and expense_id > 0:
        logging.info("Expense ID is valid.")
        return True
    else:
        logging.warning("Invalid expense ID. It must be a positive integer.")
        return False


def validate_amount(amount: float) -> bool:
    logging.info(f"Validating amount: {amount}")
    if isinstance(amount, (int, float)) and amount > 0:
        logging.info("Amount is valid.")
        return True
    else:
        logging.warning("Invalid amount. It must be a positive number.")
        return False


def validate_date(date: str) -> bool:
    logging.info(f"Validating date: {date}")
    try:
        datetime.strptime(date, "%Y-%m-%d")
        logging.info("Date is valid.")
        return True
    except ValueError:
        logging.warning("Invalid date format. It must be in YYYY-MM-DD format.")
        return False

def validate_category(category: str) -> bool:
    logging.info(f"Validating category: {category}")
    if isinstance(category, str) and category.strip():
        logging.info("Category is valid.")
        return True
    else:
        logging.warning("Invalid category. It must be a non-empty string.")
        return False

def validate_description(description: str) -> bool:
    logging.info(f"Validating description: {description}")
    if isinstance(description, str) and description.strip():
        logging.info("Description is valid.")
        return True
    else:
        logging.warning("Invalid description. It must be a non-empty string.")
        return False