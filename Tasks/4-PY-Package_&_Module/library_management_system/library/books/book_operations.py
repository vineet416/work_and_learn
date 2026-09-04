from library.logger import logging


def add_book(books: dict, book: str, author: str) -> str:
    logging.info(f"Adding book: {book} by {author}")
    try:
        new_book = {
            "id": max(book["id"] for book in books) + 1 if books else 101,
            "title": book,
            "author": author,
            "available": True
        }
        books[new_book["id"]] = new_book
        logging.info(f"Book added successfully: {new_book}")
        return f"Book '{book}' by {author} added successfully with ID {new_book['id']}."
    except Exception as e:
        logging.error(f"Error occurred while adding book: {e}")
        return f"Error occurred while adding book: {e}"




def remove_book(books: dict, book_id: int) -> str:
    logging.info(f"Removing book with ID: {book_id}")
    try:
        if book_id in books:
            book_to_remove = books.pop(book_id)
            logging.info(f"Book removed successfully: {book_to_remove}")
            return f"Book with ID {book_id} removed successfully."
        else:
            logging.warning(f"No book found with ID: {book_id}")
            return f"No book found with ID: {book_id}"
    except Exception as e:
        logging.error(f"Error occurred while removing book: {e}")
        return f"Error occurred while removing book: {e}"



def update_book(books: dict, book_id: int, new_title: str = None, new_author: str = None) -> str:
    logging.info(f"Updating book with ID: {book_id}")
    try:
        if book_id in books:
            if new_title:
                books[book_id]["title"] = new_title
            if new_author:
                books[book_id]["author"] = new_author
            logging.info(f"Book updated successfully: {books[book_id]}")
            return f"Book with ID {book_id} updated successfully."
        else:
            logging.warning(f"No book found with ID: {book_id}")
            return f"No book found with ID: {book_id}"
    except Exception as e:
        logging.error(f"Error occurred while updating book: {e}")
        return f"Error occurred while updating book: {e}"




def view_all_books(books: dict) -> str:
    logging.info("Listing all books")
    try:
        if books:
            result = "Books in the library:\n"
            for book_id, book in books.items():
                result += f"ID: {book_id}, Title: {book['title']}, Author: {book['author']}, Available: {book['available']}\n"
            logging.info("Books listed successfully")
            return result
        else:
            logging.info("No books available in the library.")
            return "No books available in the library."
    except Exception as e:
        logging.error(f"Error occurred while listing books: {e}")
        return f"Error occurred while listing books: {e}"





def view_all_available_books(books: dict) -> str:
    logging.info("Listing all available books")
    try:
        available_books = {book_id: book for book_id, book in books.items() if book["available"]}
        if available_books:
            result = "Available books in the library:\n"
            for book_id, book in available_books.items():
                result += f"ID: {book_id}, Title: {book['title']}, Author: {book['author']}\n"
            logging.info("Available books listed successfully")
            return result
        else:
            logging.info("No available books in the library.")
            return "No available books in the library."
    except Exception as e:
        logging.error(f"Error occurred while listing available books: {e}")
        return f"Error occurred while listing available books: {e}"





def get_book_by_id(books: dict, book_id: int) -> str:
    logging.info(f"Fetching book with ID: {book_id}")
    try:
        if book_id in books:
            book = books[book_id]
            logging.info(f"Book fetched successfully: {book}")
            return f"ID: {book_id}, Title: {book['title']}, Author: {book['author']}, Available: {book['available']}"
        else:
            logging.warning(f"No book found with ID: {book_id}")
            return f"No book found with ID: {book_id}"
    except Exception as e:
        logging.error(f"Error occurred while fetching book: {e}")
        return f"Error occurred while fetching book: {e}"