# PARENT CLASS
class BankAccount:
    def __init__(self, account_number, holder_name, balance):
        self.account_number = account_number
        self.holder_name = holder_name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"₹{amount:,.2f} deposited successfully.")

    def display_balance(self):
        print(f"Current Balance: ₹{self.balance:,.2f}")

    def account_details(self):
        print(f"Account Number: {self.account_number}")
        print(f"Holder Name: {self.holder_name}")
        print(f"Balance: ₹{self.balance:,.2f}")




# CHILD CLASS - SAVINGS ACCOUNT
class SavingsAccount(BankAccount):

    def __init__(self, account_number, holder_name, balance, interest_rate):
        super().__init__(account_number, holder_name, balance)
        self.interest_rate = interest_rate

    def display_account_type(self):
        print("Account Type: Savings Account")
        print(f"Interest Rate: {self.interest_rate}%")




# CHILD CLASS - CURRENT ACCOUNT
class CurrentAccount(BankAccount):

    def __init__(self, account_number, holder_name, balance, overdraft_limit):
        super().__init__(account_number, holder_name, balance)
        self.overdraft_limit = overdraft_limit

    def display_account_type(self):
        print("Account Type: Current Account")
        print(f"Overdraft Limit: ₹{self.overdraft_limit:,.2f}")




# CHILD CLASS - SALARY ACCOUNT
class SalaryAccount(BankAccount):
    def __init__(self, account_number, holder_name, balance, employer, monthly_salary):
        super().__init__(account_number, holder_name, balance)
        self.employer = employer
        self.monthly_salary = monthly_salary

    def display_account_type(self):
        print("Account Type: Salary Account")
        print(f"Employer: {self.employer}")
        print(f"Monthly Salary: ₹{self.monthly_salary:,.2f}")




# CREATE SAVINGS ACCOUNTS
savings_account1 = SavingsAccount("SA001", "Vineet Patel", 5000.00, 6.5)
savings_account2 = SavingsAccount("SA002", "Riya Sharma", 10000.00, 5.0)

# CREATE CURRENT ACCOUNTS
current_account1 = CurrentAccount("CA001", "Amit Singh", 20000.00, 5000.00)
current_account2 = CurrentAccount("CA002", "Neha Verma", 15000.00, 3000.00)

# CREATE SALARY ACCOUNTS
salary_account1 = SalaryAccount("SAL001", "Rahul Mehta", 8000.00, "ABC Corp", 50000.00)
salary_account2 = SalaryAccount("SAL002", "Priya Kapoor", 12000.00, "XYZ Ltd", 60000.00)



# SAVINGS ACCOUNT DEMONSTRATION
print("Savings Account 1")
savings_account1.account_details()
savings_account1.display_account_type()
savings_account1.deposit(5000)
savings_account1.display_balance()

print("\nSavings Account 2")
savings_account2.account_details()
savings_account2.display_account_type()
savings_account2.deposit(5000)
savings_account2.display_balance()


# CURRENT ACCOUNT DEMONSTRATION
print("\nCurrent Account 1")
current_account1.account_details()
current_account1.display_account_type()
current_account1.deposit(5000)
current_account1.display_balance()

print("\nCurrent Account 2")
current_account2.account_details()
current_account2.display_account_type()
current_account2.deposit(5000)
current_account2.display_balance()


# SALARY ACCOUNT DEMONSTRATION
print("\nSalary Account 1")
salary_account1.account_details()
salary_account1.display_account_type()
salary_account1.deposit(5000)
salary_account1.display_balance()

print("\nSalary Account 2")
salary_account2.account_details()
salary_account2.display_account_type()
salary_account2.deposit(5000)
salary_account2.display_balance()


# DEMONSTRATE INHERITED PROPERTIES
print("\nInherited Properties")
print("Savings Account 1 Holder Name:", savings_account1.holder_name)
print("Savings Account 1 Balance:", savings_account1.balance)
print("Current Account 1 Holder Name:", current_account1.holder_name)
print("Current Account 1 Balance:", current_account1.balance)
print("Salary Account 1 Holder Name:", salary_account1.holder_name)
print("Salary Account 1 Balance:", salary_account1.balance)


# DEMONSTRATE CHILD-SPECIFIC PROPERTIES
print("\nChild-Specific Properties")
print("Savings Account 1 Interest Rate:", savings_account1.interest_rate)
print("Current Account 1 Overdraft Limit:", current_account1.overdraft_limit)
print("Salary Account 1 Employer:", salary_account1.employer)
print("Salary Account 1 Monthly Salary:", salary_account1.monthly_salary)