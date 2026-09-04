from .logger import logging


def extract_expense_id(line: str):
    row = line.strip()
    if not row:
        return None
    first_col = row.split(",", 1)[0].strip()
    if first_col.lower() == "id" or not first_col.isdigit():
        return None
    return int(first_col)


def find_expense(expense_id: int, expenses_file: str = "expenses.csv") -> str:
    logging.info(f"Searching for expense with ID: {expense_id}")
    try:
        expenses = get_all_expenses(expenses_file)
        if "No expenses available." in expenses:
            logging.warning("No expenses available.")
            return False, "No expenses available."
        else:
            for line in expenses.strip().split("\n"):
                row_id = extract_expense_id(line)
                if row_id is None:
                    continue
                expense = line.split(",")
                if row_id == expense_id:
                    logging.info(f"Expense found: {expense}")
                    return True, f"Expense found: {expense}"
            logging.warning(f"No expense found with ID: {expense_id}")
            return False, f"No expense found with ID: {expense_id}"
    except Exception as e:
        logging.error(f"Error occurred while searching for expense: {e}")
        return False, f"Error occurred while searching for expense: {e}"


    

def add_expense(id: int, date: str, amount: float, category: str, description: str=None , expenses_file: str = "expenses.csv") -> str:
    logging.info(f"Adding expense: {id}, {date}, {amount}, {category}, {description}")
    try:
        expense = {
                "id": id,
                "date": date,
                "amount": amount,
                "category": category,
                "description": description
        }

        found, _ = find_expense(id, expenses_file)
        if found:
            logging.warning(f"Expense with ID {id} already exists.")
            return f"Expense with ID {id} already exists."
        else:
            with open(expenses_file, "a") as f:
                f.write(f"{expense['id']},{expense['date']},{expense['amount']},{expense['category']},{expense['description']}\n")
            logging.info("Expense added successfully")
            return "Expense added successfully."
    except Exception as e:
        logging.error(f"Error occurred while adding expense: {e}")
        return f"Error occurred while adding expense: {e}"



def get_all_expenses(expenses_file: str = "expenses.csv") -> str:
    logging.info("Retrieving all expenses")
    try:
        with open(expenses_file, "r") as f:
            result = f.read()
        logging.info("Expenses retrieved successfully")
        return result
    except FileNotFoundError:
        logging.warning("Expenses file not found.")
        return "No expenses available."
    except Exception as e:
        logging.error(f"Error occurred while retrieving expenses: {e}")
        return f"Error occurred while retrieving expenses: {e}"




def delete_expense(expense_id: int, expenses_file: str = "expenses.csv") -> str:
    logging.info(f"Deleting expense with ID: {expense_id}")
    try:
        found, _ = find_expense(expense_id, expenses_file)
        if not found:
            logging.warning(f"No expense found with ID: {expense_id}")
            return f"No expense found with ID: {expense_id}"
        else:
            with open(expenses_file, "r") as f:
                lines = f.readlines()
            with open(expenses_file, "w") as f:
                for line in lines:
                    row_id = extract_expense_id(line)
                    if row_id is None or row_id != expense_id:
                        f.write(line)
            logging.info(f"Expense with ID {expense_id} deleted successfully.")
            return f"Expense with ID {expense_id} deleted successfully."
    except FileNotFoundError:
        logging.warning("Expenses file not found.")
        return "No expenses available."
    except Exception as e:
        logging.error(f"Error occurred while deleting expense: {e}")
        return f"Error occurred while deleting expense: {e}"




def update_expense(expense_id: int, date: str, amount: float, category: str, description: str = None, expenses_file: str = "expenses.csv") -> str:
    logging.info(f"Updating expense with ID: {expense_id}")
    try:
        found, _ = find_expense(expense_id, expenses_file)
        if not found:
            logging.warning(f"No expense found with ID: {expense_id}")
            return f"No expense found with ID: {expense_id}"
        else:
            with open(expenses_file, "r") as f:
                lines = f.readlines()
            with open(expenses_file, "w") as f:
                for line in lines:
                    row_id = extract_expense_id(line)
                    if row_id == expense_id:
                        f.write(f"{expense_id},{date},{amount},{category},{description}\n")
                    else:
                        f.write(line)
            logging.info(f"Expense with ID {expense_id} updated successfully.")
            return f"Expense with ID {expense_id} updated successfully."
    except FileNotFoundError:
        logging.warning("Expenses file not found.")
        return "No expenses available."
    except Exception as e:
        logging.error(f"Error occurred while updating expense: {e}")
        return f"Error occurred while updating expense: {e}"


    