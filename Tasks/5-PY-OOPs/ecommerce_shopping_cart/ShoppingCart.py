

class SHOPPING_CART:

    def __init__(self):
        self.items = []

    def add_product(self, product, quantity=1):
        if not product.is_available():
            return f"Sorry, {product.product_name} is out of stock."
        self.items.append((product, quantity))
        product.stock -= quantity
        return f"{product.product_name} added to cart."

    def remove_product(self, product, quantity=1):
        if (product, quantity) in self.items:
            self.items.remove((product, quantity))
            product.stock += quantity
            return f"{product.product_name} removed from cart."
        return f"{product.product_name} is not in the cart."

    def calculate_total(self):
        total = sum(product.price * quantity for product, quantity in self.items)
        return total

    def view_cart(self):
        if not self.items:
            return "Your cart is empty."
        cart_contents = "Items in your cart:\n"
        for product, quantity in self.items:
            cart_contents += f"- {product.product_name} (₹{product.price}) x {quantity}\n"

        total = self.calculate_total()
        cart_contents += "-" * 30 + "\n"
        cart_contents += f"Total: ₹{total}"
        return cart_contents


