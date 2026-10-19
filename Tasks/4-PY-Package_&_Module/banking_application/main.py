from banking.customers import *
from banking.transactions import *
from banking.validation import *
from banking.logger import logging, read_transaction_history
from banking.exceptions import InvalidAmountError, InsufficientBalanceError


# Sample account details for testing
account_details = {
    "1001": {
    "Account_Number": "1001",
    "Name": "Vineet Patel",
    "Balance": 12000
},
    "1002": {
    "Account_Number": "1002",
    "Name": "Rohit Sharma",
    "Balance": 45000
},
    "1003": {
    "Account_Number": "1003",
    "Name": "Virat Kolhi",
    "Balance": 18000
    }
}


def main():
    logging.info("Banking application started.")
    try:
        while True:
            print("\nWelcome to the Banking Application")
            print("1. Create Account")
            print("2. Show All Accounts")
            print("3. Deposit Money")
            print("4. Withdraw Money")
            print("5. Transfer Money")
            print("6. Check Balance")
            print("7. Transaction History")
            print("8. Total Money in Bank")
            print("9. Richest Customer")
            print("10. Exit")

            choice = int(input("Enter your choice: "))

            if choice == 1:
                account_number = input("Enter account number: ")
                if validate_account_number(account_number):
                    if check_if_account_exists(account_number, account_details):
                        result = "Account already exists."
                    else:
                        account_holder = input("Enter account holder name: ")
                        initial_balance = float(input("Enter initial balance: "))
                        result = create_account(account_number, account_holder, initial_balance, account_details)
                else:
                    result = "Invalid account number. It must be a 4-digit number."
                print(result)

            elif choice == 2:
                accounts = show_all_accounts(account_details)
                for account in accounts:
                    print(f"Account Number: {account['Account_Number']}, Name: {account['Name']}, Balance: {account['Balance']}")

            elif choice == 3:
                account_number = input("Enter account number: ")
                amount = float(input("Enter amount to deposit: "))
                if validate_account_number(account_number):
                    try:
                        result = deposit(account_number, amount, account_details)
                        print(result)
                    except InvalidAmountError as e:
                        print(f"Deposit failed: {e}")
                else:
                    print("Invalid account number. It must be a 4-digit number.")

            elif choice == 4:
                account_number = input("Enter account number: ")
                amount = float(input("Enter amount to withdraw: "))
                if validate_account_number(account_number):
                    try:
                        result = withdraw(account_number, amount, account_details)
                        print(result)
                    except InvalidAmountError as e:
                        print(f"Withdrawal failed: {e}")
                    except InsufficientBalanceError as e:
                        print(f"Withdrawal failed: {e}")
                else:
                    print("Invalid account number. It must be a 4-digit number.")

            elif choice == 5:
                from_account = input("Enter your account number: ")
                to_account = input("Enter recipient's account number: ")
                amount = float(input("Enter amount to transfer: "))
                if validate_account_number(from_account) and validate_account_number(to_account):
                    try:
                        result = transfer_money(from_account, to_account, amount, account_details)
                        print(result)
                    except InvalidAmountError as e:
                        print(f"Transfer failed: {e}")
                    except InsufficientBalanceError as e:
                        print(f"Transfer failed: {e}")
                else:
                    print("Invalid account numbers. They must be 4-digit numbers.")

            elif choice == 6:
                account_number = input("Enter account number: ")
                if validate_account_number(account_number):
                    result = check_balance(account_number, account_details)
                    print(result)
                else:
                    print("Invalid account number. It must be a 4-digit number.")

            elif choice == 7:
                transactions = read_transaction_history()
                if transactions:
                    print("\n--- Transaction History ---")
                    for transaction in transactions:
                        print(transaction.strip())
                else:
                    print("No transactions found.")

            elif choice == 8:
                total_money = total_money_in_bank(account_details)
                print(f"Total money in the bank: {total_money}")

            elif choice == 9:
                richest = richest_customer(account_details)
                if richest:
                    print(f"Richest Customer - Name: {richest['Name']}, Balance: {richest['Balance']}")
                else:
                    print("No customer data available.")

            elif choice == 10:
                logging.info("Exiting the banking application.")
                break

            else:
                logging.warning(f"Invalid choice entered: {choice}")
                print("Invalid choice. Please try again.")

    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
        print("An unexpected error occurred. Please try again later.")



if __name__ == "__main__":
    main()