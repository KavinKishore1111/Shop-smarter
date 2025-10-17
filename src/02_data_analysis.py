import os
import pandas as pd

# Load cleaned data
# Determine project root
project_root = os.path.dirname(os.path.dirname(__file__))  # src -> project root

# Paths
processed_file = os.path.join(project_root, "data", "processed", "ecommerce_cleaned.csv")
df = pd.read_csv(processed_file)






# Revenue by Product Category
category_revenue = df.groupby('Product_Category')['Revenue'].sum().sort_values(ascending=False)
print("Revenue by Product Category:")
print(category_revenue)

# Best Customers by total spend
best_customers = df.groupby('Customer_Id')['Revenue'].sum().sort_values(ascending=False).head(10)
print("\nTop 10 Customers by Revenue:")
print(best_customers)

# Peak Sales by Month
df['Month'] = pd.to_datetime(df['Order_Date']).dt.to_period('M')
monthly_sales = df.groupby('Month')['Revenue'].sum()
print("\nMonthly Revenue Trend:")
print(monthly_sales)

# Underperforming Products
product_sales = df.groupby('Product')['Revenue'].sum().sort_values()
underperforming_products = product_sales.head(10)
print("\nUnderperforming Products:")
print(underperforming_products)

# Save analysis summaries for Power BI or report
category_revenue.to_csv("../data/processed/category_revenue.csv")
best_customers.to_csv("../data/processed/best_customers.csv")
monthly_sales.to_csv("../data/processed/monthly_sales.csv")
underperforming_products.to_csv("../data/processed/underperforming_products.csv")

print("Analysis complete. Summaries saved to ../data/processed/")

