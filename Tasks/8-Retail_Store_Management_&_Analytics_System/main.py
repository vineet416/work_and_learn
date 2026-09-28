from product import Product, Electronics, Clothing, Books
from file_handler import create_data_folder, create_products_file, append_product, read_products, create_sales_file, show_file_handling, PRODUCT_FILE
from analysis import perform_analysis


def demonstrate_classes():
    print("\n===================================")
    print("PRODUCT CLASS DEMONSTRATION")
    print("===================================")
    product = Product(1, "Laptop", "Dell", 65000, 8)
    print("\nParent Class - Product")
    product.display_product()
    print("\nUpdating stock...")
    product.update_stock(2)
    print("Updated stock:", product.stock)
    electronics = Electronics(2, "Smartphone", "Samsung", 30000, 15, "2 Years", "Galaxy S25")
    print("\nChild Class - Electronics")
    electronics.display_product()
    clothing = Clothing(11, "T-Shirt", "Nike", 1800, 30, "M", "Cotton")
    print("\nChild Class - Clothing")
    clothing.display_product()
    book = Books(21, "Python Programming", "Pearson", 1200, 9, "John Smith", "Pearson")
    print("\nChild Class - Books")
    book.display_product()


def main():
    print("===================================")
    print("RETAIL STORE MANAGEMENT SYSTEM")
    print("===================================")
    # Create data folder
    create_data_folder()
    # Create products.csv
    create_products_file()
    # Read product records
    products = read_products()
    print(f"\nNumber of products: {len(products)}")
    # Demonstrate append operation
    # Only append if product 31 does not already exist
    product_ids = [int(product["product_id"]) for product in products]
    if 31 not in product_ids:
        append_product()
    # Demonstrate file reading
    show_file_handling()
    # Create sales.csv
    create_sales_file()
    # Demonstrate OOP and inheritance
    demonstrate_classes()
    # Perform Pandas analysis
    perform_analysis()
    print("\n===================================")
    print("PROJECT COMPLETED")
    print("===================================")
    print("\nGenerated files:")
    print("data/products.csv")
    print("data/sales.csv")
    print("\noutput/cleaned_sales.csv")
    print("output/product_report.csv")
    print("output/city_sales_report.csv")
    print("output/category_report.csv")
    print("output/sales_summary.txt")


if __name__ == "__main__":
    main()