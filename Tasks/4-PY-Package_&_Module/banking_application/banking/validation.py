from .logger import logging


def validate_account_number(account_number: int) -> bool:
    logging.info(f"Validating account number: {account_number}")
    if not isinstance(account_number, str):
        logging.error("Account number must be a string.")
        return False
    if len(account_number) != 4 or not account_number.isdigit():
        logging.error("Account number must be a 4-digit number.")
        return False
    return True



def check_if_account_exists(account_number: str, account_details: dict) -> bool:
    return account_number in account_details


def validate_deposit_amount(amount: float) -> bool:
    logging.info(f"Validating deposit amount: {amount}")
    if not isinstance(amount, (int, float)):
        logging.error("Deposit amount must be a number.")
        return False
    if amount <= 0:
        logging.error("Deposit amount must be positive.")
        return False
    return True


def validate_withdrawal_amount(amount: float, account_number: str, account_details: dict) -> bool:
    logging.info(f"Validating withdrawal amount: {amount}")
    if not isinstance(amount, (int, float)):
        logging.error("Withdrawal amount must be a number.")
        return False
    if amount <= 0:
        logging.error("Withdrawal amount must be positive.")
        return False
    if account_number in account_details:
        if amount > account_details[account_number]["Balance"]:
            logging.error("Withdrawal amount exceeds available balance.")
            return False
    else:
        logging.error("Account number does not exist.")
        return False
    return True