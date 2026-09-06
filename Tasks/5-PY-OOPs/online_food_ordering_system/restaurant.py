class RESTAURANT:
    def __init__(self, name):
        self.name = name
        self.menu = []

    def add_food_item(self, food_item):
        self.menu.append((food_item))

    def display_menu(self):
        print(f"Menu for {self.name}:")
        for index, item in enumerate(self.menu, start=1):
            print(f"{index}. {item.name} | {item.category} | ${item.price:.2f}")
            