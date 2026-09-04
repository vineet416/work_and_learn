from library.logger import logging


def search_by_title(books: dict, title: str) -> str:
    logging.info(f"Searching for books with title: {title}")
    try:
        found_books = [book for book in books.values() if book["title"].lower() == title.lower()]
        if found_books:
            result = "Books found:\n"
            for book in found_books:
                result += f"ID: {book['id']}, Title: {book['title']}, Author: {book['author']}, Available: {book['available']}\n"
            logging.info("Books found successfully")
            return result
        else:
            logging.info("No books found with the given title.")
            return "No books found with the given title."
    except Exception as e:
        logging.error(f"Error occurred while searching for books by title: {e}")
        return f"Error occurred while searching for books by title: {e}"



def search_by_author(books: dict, author: str) -> str:
    logging.info(f"Searching for books by author: {author}")
    try:
        found_books = [book for book in books.values() if book["author"].lower() == author.lower()]
        if found_books:
            result = "Books found:\n"
            for book in found_books:
                result += f"ID: {book['id']}, Title: {book['title']}, Author: {book['author']}, Available: {book['available']}\n"
            logging.info("Books found successfully")
            return result
        else:
            logging.info("No books found by the given author.")
            return "No books found by the given author."
    except Exception as e:
        logging.error(f"Error occurred while searching for books by author: {e}")
        return f"Error occurred while searching for books by author: {e}"