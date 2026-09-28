import csv
import os


DATA_FOLDER = "data"
PRODUCT_FILE = os.path.join(DATA_FOLDER, "products.csv")
SALES_FILE = os.path.join(DATA_FOLDER, "sales.csv")


def create_data_folder():
    os.makedirs(DATA_FOLDER, exist_ok=True)


def create_products_file():
    products = [
        [1, "Laptop", "Dell", 65000, 8, "Electronics"],
        [2, "Smartphone", "Samsung", 30000, 15, "Electronics"],
        [3, "Headphones", "Sony", 5000, 7, "Electronics"],
        [4, "Smart Watch", "Apple", 25000, 12, "Electronics"],
        [5, "Tablet", "Lenovo", 22000, 6, "Electronics"],
        [6, "Keyboard", "Logitech", 2500, 20, "Electronics"],
        [7, "Mouse", "Logitech", 1200, 25, "Electronics"],
        [8, "Monitor", "LG", 18000, 9, "Electronics"],
        [9, "Printer", "HP", 15000, 11, "Electronics"],
        [10, "Camera", "Canon", 45000, 5, "Electronics"],
        [11, "T-Shirt", "Nike", 1800, 30, "Clothing"],
        [12, "Jeans", "Levis", 3500, 18, "Clothing"],
        [13, "Jacket", "Puma", 4500, 8, "Clothing"],
        [14, "Hoodie", "Adidas", 3000, 14, "Clothing"],
        [15, "Sneakers", "Nike", 5500, 10, "Clothing"],
        [16, "Formal Shirt", "Van Heusen", 2500, 22, "Clothing"],
        [17, "Shorts", "Puma", 1800, 16, "Clothing"],
        [18, "Sweater", "H&M", 2800, 7, "Clothing"],
        [19, "Track Pants", "Adidas", 2200, 13, "Clothing"],
        [20, "Cap", "Nike", 900, 20, "Clothing"],
        [21, "Python Programming", "Pearson", 1200, 9, "Books"],
        [22, "Data Science Basics", "O'Reilly", 1800, 12, "Books"],
        [23, "Machine Learning", "Springer", 2200, 5, "Books"],
        [24, "Web Development", "Packt", 1500, 17, "Books"],
        [25, "Artificial Intelligence", "Pearson", 2000, 8, "Books"],
        [26, "Clean Code", "Prentice Hall", 1600, 11, "Books"],
        [27, "Python Cookbook", "O'Reilly", 1900, 6, "Books"],
        [28, "Deep Learning", "MIT Press", 2500, 10, "Books"],
        [29, "SQL Fundamentals", "McGraw Hill", 1300, 15, "Books"],
        [30, "Statistics Guide", "Pearson", 1100, 7, "Books"]
    ]
    headers = ["product_id", "name", "brand", "price", "stock", "category"]
    with open(PRODUCT_FILE, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(headers)
        writer.writerows(products)
    print("products.csv created successfully.")


def append_product():
    product = [31, "USB Drive", "SanDisk", 800, 25, "Electronics"]
    with open(PRODUCT_FILE, "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(product)
    print("Product appended successfully.")


def read_products():
    products = []
    with open(PRODUCT_FILE, "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            products.append(row)
    return products


def create_sales_file():
    products = read_products()
    product_dict = {}
    for product in products:
        product_dict[int(product["product_id"])] = product
    # 50 transactions
    product_ids = [
        1, 2, 3, 4, 5,
        1, 2, 6, 7, 8,
        9, 10, 11, 12, 13,
        14, 15, 16, 17, 18,
        19, 20, 21, 22, 23,
        24, 25, 26, 27, 28,
        29, 30, 1, 2, 3,
        4, 5, 6, 7, 8,
        9, 10, 11, 12, 13,
        14, 15, 16, 17, 18
    ]
    quantities = [
        2, 3, 1, 2, 4,
        1, 2, 3, 2, 1,
        2, 1, 3, 2, 1,
        2, 3, 2, 1, 2,
        3, 2, 1, 2, 3,
        1, 2, 2, 1, 2,
        3, 4, 2, 1, 3,
        2, 1, 2, 3, 2,
        1, 2, 3, 2, 1,
        3, 2, 1, 2, 3
    ]
    cities = ["Mumbai", "Pune", "Bangalore", "Delhi", "Hyderabad"]
    payment_methods = ["UPI", "Credit Card", "Debit Card", "Cash"]
    headers = ["transaction_id", "product_id", "product_name", "category", "quantity", "price", "customer_city", "payment_method"]
    with open(SALES_FILE, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(headers)
        for i in range(50):
            product_id = product_ids[i]
            product = product_dict[product_id]
            row = [
                i + 1,
                product_id,
                product["name"],
                product["category"],
                quantities[i],
                float(product["price"]),
                cities[i % len(cities)],
                payment_methods[i % len(payment_methods)]
            ]
            writer.writerow(row)
    print("sales.csv created successfully.")


def show_file_handling():
    print("\n--- File Handling Demonstration ---")
    print("Reading products using read():")
    products = read_products()
    for product in products[:3]:
        print(product)
    print("\nProducts file contains", len(products), "products.")