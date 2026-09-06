class FOOD_ITEM:
    def __init__(self, name, category, price):
        self.name = name
        self.category = category
        self.price = price

    def display_item(self):
        print(f"{self.name} | {self.category} | ${self.price:.2f}")