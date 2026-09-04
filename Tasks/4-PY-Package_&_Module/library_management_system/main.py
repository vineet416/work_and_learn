from library.books.book_operations import *
from library.search.search_operations import *
from library.transactions.borrowing import *
from library.logger import logging
from library.utils.validation import *
from library.utils.history import * 

books = {
    101: {
        "id": 101,
        "title": "Python Crash Course",
        "author": "Eric Matthes",
        "available": True
    },
    102: {
        "id": 102,
        "title": "Automate the Boring Stuff",
        "author": "Al Sweigart",
        "available": True
    },
    103: {
        "id": 103,
        "title": "Fluent Python",
        "author": "Luciano Ramalho",
        "available": True
    }
}



def main():
        while True:
            print("\nLibrary Management System")
            print("1. Add Book")
            print("2. Remove Book")
            print("3. Update Book")
            print("4. Search Book")
            print("5. Borrow Book")
            print("6. Return Book")
            print("7. List All Books")
            print("8. List Available Books")
            print("9. View Borrowing History")
            print("0. Exit")


            try:
                choice = int(input("Enter your choice: "))
                logging.info(f"User selected option: {choice}")
                if choice < 0 or choice > 9:
                    logging.warning("Invalid choice entered. Please enter a number between 0 and 9.")
                    print("Invalid choice. Please enter a number between 0 and 9.")
                    continue
            except ValueError:
                logging.error("Invalid input. Please enter a number between 0 and 9.")
                print("Invalid input. Please enter a number between 0 and 9.")
                continue

            else:      
                if choice == 1:
                    title = input("Enter book title: ")
                    author = input("Enter book author: ")
                    result = add_book(books, title, author)
                    print(result)

                elif choice == 2:
                    book_id = int(input("Enter book ID to remove: "))
                    result = remove_book(books, book_id)
                    print(result)

                elif choice == 3:
                    book_id = int(input("Enter book ID to update: "))
                    new_title = input("Enter new title (leave blank to keep current): ")
                    new_author = input("Enter new author (leave blank to keep current): ")
                    result = update_book(books, book_id, new_title, new_author)
                    print(result)

                elif choice == 4:
                    search_choice = int(input("Search by: 1. Title 2. Author: "))
                    logging.info(f"User selected search option: {search_choice}")
                    if search_choice == 1:
                        title = input("Enter book title to search: ")
                        result = search_by_title(books, title)
                        print(result)
                    elif search_choice == 2:
                        author = input("Enter author name to search: ")
                        result = search_by_author(books, author)
                        print(result)
                    else:
                        logging.warning("Invalid search choice. Please enter 1 or 2.")
                        print("Invalid search choice. Please enter 1 or 2.") 

                elif choice == 5:
                    borrow_choice = int(input("Borrow by: 1. ID 2. Title: "))
                    logging.info(f"User selected borrow option: {borrow_choice}")
                    if borrow_choice == 1:
                        book_id = int(input("Enter book ID to borrow: "))
                        result = borrow_book_by_id(books, book_id)
                        print(result)
                    elif borrow_choice == 2:
                        title = input("Enter book title to borrow: ")
                        result = borrow_book_by_title(books, title)
                        print(result)
                    else:
                        logging.warning("Invalid borrow choice. Please enter 1 or 2.")
                        print("Invalid borrow choice. Please enter 1 or 2.")

                elif choice == 6:
                    return_choice = int(input("Return by: 1. ID 2. Title: "))
                    logging.info(f"User selected return option: {return_choice}")
                    if return_choice == 1:
                        book_id = int(input("Enter book ID to return: "))
                        result = return_book_by_id(books, book_id)
                        print(result)
                    elif return_choice == 2:
                        title = input("Enter book title to return: ")
                        result = return_book_by_title(books, title)
                        print(result)
                    else:
                        logging.warning("Invalid return choice. Please enter 1 or 2.")
                        print("Invalid return choice. Please enter 1 or 2.")

                elif choice == 7:
                    result = view_all_books(books)
                    print(result)

                elif choice == 8:
                    result = view_all_available_books(books)
                    print(result)

                elif choice == 9:
                    history_result = view_borrowing_history()
                    print(history_result)

                elif choice == 0:
                    logging.info("Exiting the Library Management System.")
                    break


if __name__ == "__main__":
    main()