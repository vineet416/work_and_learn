from .logger import logging, log_transaction


def deposit(account: int, amount: float, account_details: dict) -> str:
    try:
        logging.info(f"Depositing {amount} to account {account}.")
        if account in account_details:
            account_details[account]["Balance"] += amount
            logging.info(f"Deposit successful. New balance: {account_details[account]['Balance']}")
            log_transaction("deposit", account, amount, "successful")
            return "Deposit successful."
        else:
            logging.warning(f"Account {account} does not exist.")
            log_transaction("deposit", account, amount, "failed")
            return "Account does not exist."
    except Exception as e:
        logging.error(f"Error occurred during deposit: {e}")
        return "An error occurred during deposit."



def withdraw(account: int, amount: float, account_details: dict) -> str:
    try:
        logging.info(f"Withdrawing {amount} from account {account}.")
        if account in account_details:
            if amount <= account_details[account]["Balance"]:
                account_details[account]["Balance"] -= amount
                logging.info(f"Withdrawal successful. New balance: {account_details[account]['Balance']}")
                log_transaction("withdrawal", account, amount, "successful")
                return "Withdrawal successful."
            else:
                logging.warning(f"Insufficient funds for withdrawal from account {account}.")
                log_transaction("withdrawal", account, amount, "failed")
                return "Insufficient funds."
        else:
            logging.warning(f"Account {account} does not exist.")
            return "Account does not exist."
    except Exception as e:
        logging.error(f"Error occurred during withdrawal: {e}")
        return "An error occurred during withdrawal."



def transfer_money(from_account: int, to_account: int, amount: float, account_details: dict) -> str:
    try:
        logging.info(f"Transferring {amount} from account {from_account} to account {to_account}.")
        if from_account in account_details and to_account in account_details:
            if amount <= account_details[from_account]["Balance"]:
                account_details[from_account]["Balance"] -= amount
                account_details[to_account]["Balance"] += amount
                logging.info(f"Transfer successful. New balance for {from_account}: {account_details[from_account]['Balance']}, for {to_account}: {account_details[to_account]['Balance']}")
                log_transaction("transfer", from_account, amount, "successful", to_account)
                return "Transfer successful."
            else:
                logging.warning(f"Insufficient funds for transfer from account {from_account}.")
                log_transaction("transfer", from_account, amount, "failed", to_account)
                return "Insufficient funds."
        else:
            logging.warning(f"One or both accounts do not exist: {from_account}, {to_account}.")
            return "One or both accounts do not exist."
    except Exception as e:
        logging.error(f"Error occurred during transfer: {e}")
        return "An error occurred during transfer."




def check_balance(account: int, account_details: dict) -> str:
    try:
        logging.info(f"Checking balance for account {account}.")
        if account in account_details:
            balance = account_details[account]["Balance"]
            logging.info(f"Balance for account {account}: {balance}")
            return f"Balance for account {account}: {balance}"
        else:
            logging.warning(f"Account {account} does not exist.")
            return "Account does not exist."
    except Exception as e:
        logging.error(f"Error occurred while checking balance: {e}")
        return "An error occurred while checking balance."