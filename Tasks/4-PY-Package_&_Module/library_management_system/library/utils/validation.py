from library.logger import logging



def validate_book_id(book_id: int) -> bool:
    logging.info(f"Validating book ID: {book_id}")
    if isinstance(book_id, int) and book_id > 0:
        logging.info("Book ID is valid.")
        return True
    else:
        logging.warning("Invalid book ID. It must be a positive integer.")
        return False




def log_borrow(book_id: int, book_title: str) -> None:
    try:
        with open("borrow_history.txt", "a") as file:
            file.write(f"User borrowed book '{book_title}' (ID: {book_id})\n")
    except Exception as e:
        logging.error(f"Error occurred while logging borrow event: {e}")


def log_return(book_id: int, book_title: str) -> None:
    try:
        with open("borrow_history.txt", "a") as file:
            file.write(f"User returned book '{book_title}' (ID: {book_id})\n")
    except Exception as e:
        logging.error(f"Error occurred while logging return event: {e}")