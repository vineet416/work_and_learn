class ORDER:
    def __init__(self, order_id, customer, restaurant):
        self.order_id = order_id
        self.customer = customer
        self.restaurant = restaurant
        self.food_items = []

    def add_food_item(self, food_item):
        self.food_items.append(food_item)
        print(f"Added {food_item.name} to order {self.order_id}.")


    def display_order(self):
        print(f"Order ID: {self.order_id}")
        self.customer.display_customer()
        print(f"Restaurant: {self.restaurant.name}")
        print("Food Items:")
        for item in self.food_items:
            item.display_item()


    def calculate_total(self):
        total = sum(item.price for item in self.food_items)
        return total


    def display_order_summary(self):
        print(f"Order Summary for Order ID: {self.order_id}")
        self.customer.display_customer()
        print(f"Restaurant: {self.restaurant.name}")
        print("Food Items:")
        for item in self.food_items:
            item.display_item()
        total = self.calculate_total()
        print(f"Total Amount: ${total:.2f}")


    def remove_food_item(self, food_item):
        if food_item in self.food_items:
            self.food_items.remove(food_item)
            print(f"Removed {food_item.name} from order {self.order_id}.")
        else:
            print(f"{food_item.name} is not in the order {self.order_id}.")

    