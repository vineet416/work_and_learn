
class PRODUCT:

    def __init__(self, product_id, product_name, category, price, stock):
        self.product_id = product_id
        self.product_name = product_name
        self.category = category
        self.price = price
        self.stock = stock

    def is_available(self, quantity=1):
        return self.stock >= quantity

    def display_product(self):
        print(f"ID       : {self.product_id}")
        print(f"Name     : {self.product_name}")
        print(f"Category : {self.category}")
        print(f"Price    : ₹{self.price}")
        print(f"Stock    : {self.stock}")