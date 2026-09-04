from expense_manager.expenses import *
from expense_manager.validation import *
from expense_manager.reports import *
from expense_manager.logger import logging



def main():
    logging.info("Starting Expense Tracker Application")
    while True:
        print("\nExpense Tracker Menu:")
        print("1. Add Expense")
        print("2. Delete Expense")
        print("3. Update Expense")
        print("4. View All Expenses")
        print("5. Find Expense by ID")
        print("6. Monthly Summary Report")
        print("7. Category Summary Report")
        print("8. Highest Expense Report")
        print("9. Exit")


        try:
            choice = int(input("Enter your choice (1-9): "))
            if not validate_input(choice):
                continue
        except ValueError:
            logging.warning("Non-integer value entered for choice.")
            print("Invalid input. Please enter a number between 1 and 9.")
            continue
        else:
            if choice == 1:
                id = int(input("Enter expense ID: "))
                date = input("Enter date (YYYY-MM-DD): ")
                amount = float(input("Enter amount: "))
                category = input("Enter category: ")
                description = input("Enter description (optional): ")
                if (validate_expense_id(id) and validate_date(date) and validate_amount(amount) and validate_category(category)):
                    result = add_expense(id, date, amount, category, description)
                else:
                    result = "Invalid input. Please check the values entered."
                print(result)

            elif choice == 2:
                id = int(input("Enter expense ID to delete: "))
                result = delete_expense(id)
                print(result)

            elif choice == 3:
                expense_id = int(input("Enter expense ID to update: "))
                print("Enter new values (press Enter to keep current value):")
                date = input("Enter new date (YYYY-MM-DD): ")
                amount = input("Enter new amount: ")
                category = input("Enter new category: ")
                description = input("Enter new description (optional): ")
                if (validate_date(date) and validate_amount(float(amount)) and validate_category(category)):
                    result = update_expense(expense_id, date, float(amount), category, description)
                else:
                    result = "Invalid input. Please check the values entered."
                print(result)

            elif choice == 4:
                result = get_all_expenses()
                print(result)

            elif choice == 5:
                expense_id = int(input("Enter expense ID to find: "))
                if validate_expense_id(expense_id):
                    found, result = find_expense(expense_id)
                    print(result)
                else:
                    print("Invalid expense ID. Please enter a valid ID.")

            elif choice == 6:
                result = monthly_summary()
                print(result)

            elif choice == 7:
                result = category_summary()
                print(result)

            elif choice == 8:
                result = highest_expense()
                print(result)

            elif choice == 9:
                logging.info("Exiting Expense Tracker Application")
                print("Exiting the application. Goodbye!")
                break

            else:
                logging.warning("Invalid menu choice entered.")
                print("Invalid choice. Please enter a number between 1 and 9.")


if __name__ == "__main__":
    main()