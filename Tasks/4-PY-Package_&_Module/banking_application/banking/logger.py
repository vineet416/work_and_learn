import logging

logging.basicConfig(
    filename="banking.log",
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.DEBUG
)


def log_transaction(transaction_type: str, account_number: int, amount: float, status: str, to_account: int = None) -> None:
    try:
        with open("transactions.txt", "a") as log_file:
            if transaction_type == "deposit":
                log_file.write(f"Deposit: Account {account_number}, Amount: {amount}, Status: {status}\n")
            elif transaction_type == "withdrawal":
                log_file.write(f"Withdrawal: Account {account_number}, Amount: {amount}, Status: {status}\n")
            elif transaction_type == "transfer":
                log_file.write(f"Transfer: Account {account_number}, To Account: {to_account}, Amount: {amount}, Status: {status}\n")
    except Exception as e:
        logging.error(f"Error occurred while logging transaction: {e}")


def read_transaction_history() -> list:
    try:
        logging.info("Reading transaction history.")
        with open("transactions.txt", "r") as log_file:
            transactions = log_file.readlines()
        logging.info(f"Total transactions found: {len(transactions)}")
        return transactions
    except FileNotFoundError:
        logging.warning("transactions.txt not found. No transactions yet.")
        return []
    except Exception as e:
        logging.error(f"Error occurred while reading transaction history: {e}")
        return []
