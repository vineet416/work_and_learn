from .logger import logging

def monthly_summary(expenses: str = "expenses.csv") -> str:
    logging.info("Generating monthly summary report")
    try:
        with open(expenses, "r") as f:
            lines = f.readlines()
        if not lines:
            logging.warning("No expenses available for monthly summary.")
            return "No expenses available for monthly summary."
        
        monthly_expenses = {}
        for line in lines:
            expense = line.strip().split(",")
            date = expense[1]
            amount = float(expense[2])
            month = date[:7]
            if month in monthly_expenses:
                monthly_expenses[month] += amount
            else:
                monthly_expenses[month] = amount
        
        summary = "\n".join([f"{month}: {total}" for month, total in monthly_expenses.items()])
        logging.info("Monthly summary report generated successfully")
        return summary
    except FileNotFoundError:
        logging.warning("Expenses file not found.")
        return "No expenses available for monthly summary."
    except Exception as e:
        logging.error(f"Error occurred while generating monthly summary: {e}")
        return f"Error occurred while generating monthly summary: {e}"







def category_summary(expenses: str = "expenses.csv") -> str:
    logging.info("Generating category summary report")
    try:
        with open(expenses, "r") as f:
            lines = f.readlines()
        if not lines:
            logging.warning("No expenses available for category summary.")
            return "No expenses available for category summary."
        
        category_expenses = {}
        for line in lines:
            expense = line.strip().split(",")
            category = expense[3]
            amount = float(expense[2])
            if category in category_expenses:
                category_expenses[category] += amount
            else:
                category_expenses[category] = amount
        
        summary = "\n".join([f"{category}: {total}" for category, total in category_expenses.items()])
        logging.info("Category summary report generated successfully")
        return summary
    except FileNotFoundError:
        logging.warning("Expenses file not found.")
        return "No expenses available for category summary."
    except Exception as e:
        logging.error(f"Error occurred while generating category summary: {e}")
        return f"Error occurred while generating category summary: {e}"
    




def highest_expense(expenses: str = "expenses.csv") -> str:
    logging.info("Generating highest expense report")
    try:
        with open(expenses, "r") as f:
            lines = f.readlines()
        if not lines:
            logging.warning("No expenses available for highest expense report.")
            return "No expenses available for highest expense report."
        
        highest = max(lines, key=lambda line: float(line.strip().split(",")[2]))
        expense = highest.strip().split(",")
        logging.info("Highest expense report generated successfully")
        return f"Highest Expense:\nID: {expense[0]}, Date: {expense[1]}, Amount: {expense[2]}, Category: {expense[3]}, Description: {expense[4]}"
    except FileNotFoundError:
        logging.warning("Expenses file not found.")
        return "No expenses available for highest expense report."
    except Exception as e:
        logging.error(f"Error occurred while generating highest expense report: {e}")
        return f"Error occurred while generating highest expense report: {e}"