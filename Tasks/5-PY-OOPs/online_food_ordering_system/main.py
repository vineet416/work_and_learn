from customer import CUSTOMER
from restaurant import RESTAURANT
from food_item import FOOD_ITEM
from order import ORDER


restaurant1 = RESTAURANT("Pizza Hut")
restaurant2 = RESTAURANT("H2 Chinese")

PepperoniPizza = FOOD_ITEM("Pepperoni Pizza", "Main Course", 399)
MargheritaPizza = FOOD_ITEM("Margherita Pizza", "Main Course", 349)
FriedRice = FOOD_ITEM("Fried Rice", "Main Course", 299)
noodles = FOOD_ITEM("Noodles", "Main Course", 299)

restaurant1.add_food_item(PepperoniPizza)
restaurant1.add_food_item(MargheritaPizza)
restaurant2.add_food_item(FriedRice)
restaurant2.add_food_item(noodles)

customer1 = CUSTOMER(1, "Vineet Patel", "1234567890")
customer2 = CUSTOMER(2, "Virat Kohli", "9876543210")

def main():
    print("\n"+ "-"*50)
    print("Welcome to the Food Ordering System!")
    print("-"*50 + "\n")

    while True:
        print("\n"+ "-"*50)
        print("Please select a customer:")
        print("1. Vineet Patel")
        print("2. Virat Kohli")
        print("3. Exit")
        customer_choice = int(input("Select a customer (1-3): "))
        print("-"*50 + "\n")

        if customer_choice == 1:
            customer = customer1
        elif customer_choice == 2:
            customer = customer2
        elif customer_choice == 3:
            print("Thank you for using the Food Ordering System!")
            break
        else:
            print("Invalid choice. Please try again.")


        print("Available Restaurants:")
        print("1. Pizza Hut")
        print("2. H2 Chinese")
        print("3. Exit")
        choice = int(input("Select a restaurant (1-3): "))
        print("-"*50 + "\n")

        if choice == 1:
            restaurant = restaurant1

        elif choice == 2:
            restaurant = restaurant2
        elif choice == 3:
            print("\n"+ "-"*50)
            print("Thank you for using the Food Ordering System!")
            print("-"*50 + "\n")
            break
        else:
            print("\n"+ "-"*50)
            print("Invalid choice. Please try again.")
            print("-"*50 + "\n")

        print("\n"+ "-"*50)
        restaurant.display_menu()
        print("-"*50 + "\n")

        print("\n"+ "-"*50)
        print("Please select food items to add to your order (enter 0 to finish):")
        order = ORDER(order_id=1, customer=customer, restaurant=restaurant)
        while True:
            food_choice = int(input(f"Select a food item (1-{len(restaurant.menu)}): "))
            if food_choice == 0:
                break
            elif 1 <= food_choice <= len(restaurant.menu):
                selected_food_item = restaurant.menu[food_choice - 1]
                order.add_food_item(selected_food_item)
            else:
                print("Invalid choice. Please try again.")
        print("-"*50 + "\n")

        print("\n"+ "-"*50)
        print("Order Summary:")
        order.display_order_summary()
        print("-"*50 + "\n")


if __name__ == "__main__":
    main()
