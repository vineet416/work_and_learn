from Product import PRODUCT
from ShoppingCart import SHOPPING_CART


laptop = PRODUCT(101, "Laptop", "Electronics", 55000, 5)
mouse = PRODUCT(102, "Wireless Mouse", "Electronics", 800, 10)
keyboard = PRODUCT(103, "Mechanical Keyboard", "Electronics", 2500, 4)
headphones = PRODUCT(104, "Headphones", "Audio", 3000, 6)
backpack = PRODUCT(105, "Laptop Backpack", "Accessories", 1800, 8)


shopping_cart = SHOPPING_CART()
print("\n--- Welcome to the E-commerce Store ---")

while True:
    print("\nMenu:")
    print("1. View Products")
    print("2. Add Product to Cart")
    print("3. Remove Product from Cart")
    print("4. View Cart")
    print("5. Checkout")
    print("6. Exit")

    choice = int(input("Enter your choice (1-6): "))

    if choice == 1:
        print("\nAvailable Products:")
        for product in [laptop, mouse, keyboard, headphones, backpack]:
            product.display_product()
            print("-" * 30)

    elif choice == 2:
        product_id = int(input("Enter the Product ID to add to cart: "))
        product_map = {101: laptop, 102: mouse, 103: keyboard, 104: headphones, 105: backpack}
        product = product_map.get(product_id)
        if product:
            quantity = int(input("Enter the quantity: "))
            is_available = product.is_available(quantity)
            if is_available:
                message = shopping_cart.add_product(product, quantity)
                print(message)
            else:
                print(f"Sorry, only {product.stock} units of {product.product_name} are available in stock.")
        else:
            print("Invalid Product ID.")

    elif choice == 3:
        product_id = int(input("Enter the Product ID to remove from cart: "))
        product_map = {101: laptop, 102: mouse, 103: keyboard, 104: headphones, 105: backpack}
        product = product_map.get(product_id)
        if product:
            quantity = int(input("Enter the quantity to remove: "))
            if (product, quantity) in shopping_cart.items:
                message = shopping_cart.remove_product(product, quantity)
                print(message)
            else:
                print(f"Sorry, {product.product_name} is not in the cart or the requested quantity is not available.")

    elif choice == 4:
        cart_contents = shopping_cart.view_cart()
        print(cart_contents)

    elif choice == 5:
        total = shopping_cart.calculate_total()
        if total > 0:
            print(f"Your total amount is: ₹{total}")
            break
        else:
            print("Your cart is empty. Please add products before checkout.")

    elif choice == 6:
        print("Thank you for visiting! Goodbye!")
        break