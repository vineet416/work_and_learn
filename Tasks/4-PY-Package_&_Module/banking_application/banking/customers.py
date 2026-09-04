from .logger import logging
from .validation import check_if_account_exists

def create_account(account_number: int, account_holder: str, initial_balance: float, account_details: dict) -> str:
    try:
        logging.info(f"Creating account for {account_holder} with account number {account_number}.")
        if check_if_account_exists(account_number, account_details):
            logging.warning(f"Account number {account_number} already exists.")
            return "Account already exists."
        else:
            account_details[account_number] = {
                "Account_Number": account_number,
                "Name": account_holder,
                "Balance": initial_balance
            }
            logging.info(f"Account created successfully for {account_holder}.")
            return "Account created successfully."
    except Exception as e:
        logging.error(f"Error occurred while creating account: {e}")
        return "An error occurred while creating the account."
        


def show_all_accounts(account_details: dict) -> list:
    try:
        logging.info("Fetching all account details.")
        accounts = []
        for account_number, details in account_details.items():
            accounts.append({
                "Account_Number": details["Account_Number"],
                "Name": details["Name"],
                "Balance": details["Balance"]
            })
        logging.info(f"Total accounts fetched: {len(accounts)}")
        return accounts
    except Exception as e:
        logging.error(f"Error occurred while fetching accounts: {e}")
        return []


def total_money_in_bank(account_details: dict) -> float:
    try:
        logging.info("Calculating total money in the bank.")
        total_balance = sum(details["Balance"] for details in account_details.values())
        logging.info(f"Total money in the bank: {total_balance}")
        return total_balance
    except Exception as e:
        logging.error(f"Error occurred while calculating total money: {e}")
        return 0.0

def richest_customer(account_details: dict) -> dict:
    try:
        logging.info("Finding the richest customer.")
        richest = max(account_details.items(), key=lambda x: x[1]["Balance"], default=(None, None))
        logging.info(f"Richest customer found: {richest[1]['Name']} with balance {richest[1]['Balance']}" if richest[1] else "No customers found.")
        return richest[1]
    except Exception as e:
        logging.error(f"Error occurred while finding richest customer: {e}")
        return {}
    except Exception as e:
        logging.error(f"Error occurred while finding richest customer: {e}")
        return None   