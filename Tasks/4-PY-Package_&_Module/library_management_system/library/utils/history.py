from library.logger import logging


def view_borrowing_history(history: str = "borrow_history.txt") -> str:
    logging.info("Viewing borrowing history")
    try:
        with open(history, "r") as f:
            result = f.read()
        logging.info("Borrowing history retrieved successfully")
        return result
    except FileNotFoundError:
        logging.warning("Borrowing history file not found.")
        return "No borrowing history available."