class Product:
    def __init__(self, product_id, name, brand, price, stock):
        self.product_id = product_id
        self.name = name
        self.brand = brand
        self.price = price
        self.stock = stock

    def display_product(self):
        print(f"Product ID: {self.product_id}")
        print(f"Name: {self.name}")
        print(f"Brand: {self.brand}")
        print(f"Price: ₹{self.price}")
        print(f"Stock: {self.stock}")

    def update_stock(self, quantity):
        self.stock += quantity


class Electronics(Product):
    def __init__(self, product_id, name, brand, price, stock, warranty, model):
        super().__init__(product_id, name, brand, price, stock)
        self.warranty = warranty
        self.model = model

    def display_product(self):
        super().display_product()
        print(f"Warranty: {self.warranty}")
        print(f"Model: {self.model}")


class Clothing(Product):
    def __init__(self, product_id, name, brand, price, stock, size, material):
        super().__init__(product_id, name, brand, price, stock)
        self.size = size
        self.material = material

    def display_product(self):
        super().display_product()
        print(f"Size: {self.size}")
        print(f"Material: {self.material}")


class Books(Product):
    def __init__(self, product_id, name, brand, price, stock, author, publisher):
        super().__init__(product_id, name, brand, price, stock)
        self.author = author
        self.publisher = publisher

    def display_product(self):
        super().display_product()
        print(f"Author: {self.author}")
        print(f"Publisher: {self.publisher}")