from library.logger import logging
from library.utils.validation import log_borrow, log_return



def borrow_book_by_id(books: dict, book_id: int) -> str:
    logging.info(f"Attempting to borrow book with ID: {book_id}")
    try:
        if book_id in books:
            if books[book_id]["available"]:
                books[book_id]["available"] = False
                log_borrow(book_id, books[book_id]["title"])
                logging.info(f"Book borrowed successfully: {books[book_id]}")
                return f"Book with ID {book_id} borrowed successfully."
            else:
                logging.warning(f"Book with ID {book_id} is not available for borrowing.")
                return f"Book with ID {book_id} is not available for borrowing."
        else:
            logging.warning(f"No book found with ID: {book_id}")
            return f"No book found with ID: {book_id}"
    except Exception as e:
        logging.error(f"Error occurred while borrowing book: {e}")
        return f"Error occurred while borrowing book: {e}"




def borrow_book_by_title(books: dict, title: str) -> str:
    logging.info(f"Attempting to borrow book with title: {title}")
    try:
        found_books = [book for book in books.values() if book["title"].lower() == title.lower()]
        if found_books:
            for book in found_books:
                if book["available"]:
                    book["available"] = False
                    log_borrow(book["id"], book["title"])
                    logging.info(f"Book borrowed successfully: {book}")
                    return f"Book '{book['title']}' borrowed successfully."
            logging.warning(f"No available copies of the book titled '{title}' for borrowing.")
            return f"No available copies of the book titled '{title}' for borrowing."
        else:
            logging.warning(f"No book found with title: {title}")
            return f"No book found with title: {title}"
    except Exception as e:
        logging.error(f"Error occurred while borrowing book by title: {e}")
        return f"Error occurred while borrowing book by title: {e}"





def return_book_by_id(books: dict, book_id: int) -> str:
    logging.info(f"Attempting to return book with ID: {book_id}")
    try:
        if book_id in books:
            if not books[book_id]["available"]:
                books[book_id]["available"] = True
                log_return(book_id, books[book_id]["title"])
                logging.info(f"Book returned successfully: {books[book_id]}")
                return f"Book with ID {book_id} returned successfully."
            else:
                logging.warning(f"Book with ID {book_id} was not borrowed.")
                return f"Book with ID {book_id} was not borrowed."
        else:
            logging.warning(f"No book found with ID: {book_id}")
            return f"No book found with ID: {book_id}"
    except Exception as e:
        logging.error(f"Error occurred while returning book: {e}")
        return f"Error occurred while returning book: {e}"




def return_book_by_title(books: dict, title: str) -> str:
    logging.info(f"Attempting to return book with title: {title}")
    try:
        found_books = [book for book in books.values() if book["title"].lower() == title.lower()]
        if found_books:
            for book in found_books:
                if not book["available"]:
                    book["available"] = True
                    log_return(book["id"], book["title"])
                    logging.info(f"Book returned successfully: {book}")
                    return f"Book '{book['title']}' returned successfully."
            logging.warning(f"No borrowed copies of the book titled '{title}' to return.")
            return f"No borrowed copies of the book titled '{title}' to return."
        else:
            logging.warning(f"No book found with title: {title}")
            return f"No book found with title: {title}"
    except Exception as e:
        logging.error(f"Error occurred while returning book by title: {e}")
        return f"Error occurred while returning book by title: {e}"