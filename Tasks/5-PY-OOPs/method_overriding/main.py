# PARENT CLASS
class Payment:
    def process_payment(self, amount):
        print(f"Processing ₹{amount} as payment")



# CHILD CLASS - CREDIT CARD
class CreditCardPayment(Payment):
    def process_payment(self, amount):
        print(f"Processing ₹{amount} using Credit Card")



# CHILD CLASS - UPI
class UPIPayment(Payment):
    def process_payment(self, amount):
        print(f"Processing ₹{amount} using UPI")



# CHILD CLASS - NET BANKING
class NetBankingPayment(Payment):
    def process_payment(self, amount):
        print(f"Processing ₹{amount} using Net Banking")



# CHILD CLASS - WALLET
class WalletPayment(Payment):
    def process_payment(self, amount):
        print(f"Processing ₹{amount} using Wallet")



# CREATE OBJECTS
credit_card = CreditCardPayment()
upi = UPIPayment()
net_banking = NetBankingPayment()
wallet = WalletPayment()


# DEMONSTRATE METHOD OVERRIDING
print("\n PAYMENT PROCESSING ")
credit_card.process_payment(5000)
upi.process_payment(5000)
net_banking.process_payment(5000)
wallet.process_payment(5000)


# DIFFERENT PAYMENT AMOUNTS
print("\n DIFFERENT PAYMENT AMOUNTS ")
credit_card.process_payment(2500)
upi.process_payment(1500)
net_banking.process_payment(7500)
wallet.process_payment(1000)