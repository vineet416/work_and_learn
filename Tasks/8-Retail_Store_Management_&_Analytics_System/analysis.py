import os
import pandas as pd


OUTPUT_FOLDER = "output"
SALES_FILE = "data/sales.csv"
PRODUCT_FILE = "data/products.csv"


def create_output_folder():
    os.makedirs(OUTPUT_FOLDER, exist_ok=True)


def perform_analysis():
    create_output_folder()
    # Read CSV files
    sales_df = pd.read_csv(SALES_FILE)
    products_df = pd.read_csv(PRODUCT_FILE)

    # DATA CLEANING
    # Remove duplicate rows
    sales_df = sales_df.drop_duplicates()
    # Remove rows with missing values
    sales_df = sales_df.dropna()
    # Make sure quantity and price are numeric
    sales_df["quantity"] = pd.to_numeric(sales_df["quantity"])
    sales_df["price"] = pd.to_numeric(sales_df["price"])
    # Create total amount for each transaction
    sales_df["total_amount"] = sales_df["quantity"] * sales_df["price"]
    # Save cleaned data
    sales_df.to_csv(f"{OUTPUT_FOLDER}/cleaned_sales.csv", index=False)

    # BASIC ANALYSIS
    total_transactions = len(sales_df)
    total_quantity = sales_df["quantity"].sum()
    total_revenue = sales_df["total_amount"].sum()
    average_transaction_value = sales_df["total_amount"].mean()
    highest_transaction = sales_df["total_amount"].max()
    lowest_transaction = sales_df["total_amount"].min()

    # PRODUCT ANALYSIS
    product_sales = sales_df.groupby(["product_id", "product_name"])["quantity"].sum().reset_index()
    best_selling_product = product_sales.loc[product_sales["quantity"].idxmax()]
    lowest_selling_product = product_sales.loc[product_sales["quantity"].idxmin()]

    # Revenue product-wise
    revenue_product = sales_df.groupby(["product_id", "product_name"])["total_amount"].sum().reset_index()
    revenue_product = revenue_product.sort_values("total_amount", ascending=False)

    # Top 5 products
    top_5_products = product_sales.sort_values("quantity", ascending=False).head(5)

    # Bottom 5 products
    bottom_5_products = product_sales.sort_values("quantity", ascending=True).head(5)

    # CATEGORY ANALYSIS
    sales_category = sales_df.groupby("category")["quantity"].sum().reset_index()
    sales_category.columns = ["category", "total_quantity_sold"]
    revenue_category = sales_df.groupby("category")["total_amount"].sum().reset_index()
    revenue_category.columns = ["category", "total_revenue"]
    category_report = pd.merge(sales_category, revenue_category, on="category")

    # CITY ANALYSIS
    city_report = sales_df.groupby("customer_city")["total_amount"].sum().reset_index()
    city_report.columns = ["customer_city", "total_revenue"]
    city_report = city_report.sort_values("total_revenue", ascending=False)

    # PAYMENT METHOD
    payment_distribution = sales_df["payment_method"].value_counts().reset_index()
    payment_distribution.columns = ["payment_method", "transaction_count"]

    # PRODUCT PRICE ANALYSIS
    average_product_price = products_df["price"].mean()
    maximum_product_price = products_df["price"].max()
    minimum_product_price = products_df["price"].min()

    # Products with stock below 10
    low_stock_products = products_df[products_df["stock"] < 10]

    # Products priced above average
    expensive_products = products_df[products_df["price"] > average_product_price]

    # PRODUCT REPORT
    product_report = products_df.copy()
    product_quantity = sales_df.groupby("product_id")["quantity"].sum().reset_index()
    product_quantity.columns = ["product_id", "quantity_sold"]
    product_revenue = sales_df.groupby("product_id")["total_amount"].sum().reset_index()
    product_revenue.columns = ["product_id", "revenue"]
    product_report = product_report.merge(product_quantity, on="product_id", how="left")
    product_report = product_report.merge(product_revenue, on="product_id", how="left")
    product_report["quantity_sold"] = product_report["quantity_sold"].fillna(0)
    product_report["revenue"] = product_report["revenue"].fillna(0)
    product_report.to_csv(f"{OUTPUT_FOLDER}/product_report.csv", index=False)

    # CITY REPORT
    city_report.to_csv(f"{OUTPUT_FOLDER}/city_sales_report.csv", index=False)

    # CATEGORY REPORT
    category_report.to_csv(f"{OUTPUT_FOLDER}/category_report.csv", index=False)

    # HIGHEST REVENUE CATEGORY
    highest_revenue_category = revenue_category.loc[revenue_category["total_revenue"].idxmax()]

    # HIGHEST REVENUE CITY
    highest_revenue_city = city_report.iloc[0]

    # PAYMENT DISTRIBUTION
    print("\nPayment Method Distribution")
    print(payment_distribution)

    # SAVE TEXT SUMMARY
    summary = f"""
RETAIL STORE SALES REPORT
Total Transactions: {total_transactions}
Total Quantity Sold: {total_quantity}
Total Revenue: ₹{total_revenue:.2f}
Average Transaction Value: ₹{average_transaction_value:.2f}
Highest-Value Transaction: ₹{highest_transaction:.2f}
Lowest-Value Transaction: ₹{lowest_transaction:.2f}
Best Selling Product: {best_selling_product["product_name"]}
Best Selling Product Quantity: {best_selling_product["quantity"]}
Lowest Selling Product: {lowest_selling_product["product_name"]}
Lowest Selling Product Quantity: {lowest_selling_product["quantity"]}
Highest Revenue Category: {highest_revenue_category["category"]}
Highest Revenue Category Amount: ₹{highest_revenue_category["total_revenue"]:.2f}
Highest Revenue City: {highest_revenue_city["customer_city"]}
Highest Revenue City Amount: ₹{highest_revenue_city["total_revenue"]:.2f}
Average Product Price: ₹{average_product_price:.2f}
Maximum Product Price: ₹{maximum_product_price:.2f}
Minimum Product Price: ₹{minimum_product_price:.2f}

PAYMENT-METHOD DISTRIBUTION
{payment_distribution.to_string(index=False)}

TOP 5 PRODUCTS
{top_5_products.to_string(index=False)}

BOTTOM 5 PRODUCTS
{bottom_5_products.to_string(index=False)}

PRODUCTS WITH STOCK BELOW 10
{low_stock_products[["product_id", "name", "stock"]].to_string(index=False)}

PRODUCTS PRICED ABOVE AVERAGE
{expensive_products[["product_id", "name", "price"]].to_string(index=False)}
"""

    with open(f"{OUTPUT_FOLDER}/sales_summary.txt", "w", encoding="utf-8") as file:
        file.write(summary)

    # DISPLAY RESULTS
    print("\n===================================")
    print("RETAIL STORE SALES ANALYSIS")
    print("===================================")
    print(f"\nTotal Transactions: {total_transactions}")
    print(f"Total Quantity Sold: {total_quantity}")
    print(f"Total Revenue: ₹{total_revenue:.2f}")
    print(f"Average Transaction Value: ₹{average_transaction_value:.2f}")

    print(f"Highest-Value Transaction: ₹{highest_transaction:.2f}")
    print(f"Lowest-Value Transaction: ₹{lowest_transaction:.2f}")
    print(f"Best Selling Product: {best_selling_product['product_name']}")
    print(f"Lowest Selling Product: {lowest_selling_product['product_name']}")
    print(f"Highest Revenue Category: {highest_revenue_category['category']}")
    print(f"Highest Revenue City: {highest_revenue_city['customer_city']}")
    print(f"\nAverage Product Price: ₹{average_product_price:.2f}")
    print(f"Maximum Product Price: ₹{maximum_product_price:.2f}")
    print(f"Minimum Product Price: ₹{minimum_product_price:.2f}")
    print("\nSales Category-wise:")
    print(sales_category)
    print("\nRevenue Category-wise:")
    print(revenue_category)
    print("\nRevenue Product-wise:")
    print(revenue_product)
    print("\nRevenue City-wise:")
    print(city_report)
    print("\nTop 5 Products:")
    print(top_5_products)
    print("\nBottom 5 Products:")
    print(bottom_5_products)
    print("\nProducts Having Stock Below 10:")
    print(low_stock_products[["product_id", "name", "stock"]])
    print("\nProducts Priced Above Average:")
    print(expensive_products[["product_id", "name", "price"]])
    print("\nAll reports generated successfully.")