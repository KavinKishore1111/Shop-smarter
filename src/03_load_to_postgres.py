import os
import pandas as pd
from db_utils import upload_df

# Load cleaned data
# Determine project root
project_root = os.path.dirname(os.path.dirname(__file__))  # src -> project root

# Paths
processed_file = os.path.join(project_root, "data", "processed", "ecommerce_cleaned.csv")

# Load cleaned data
df = pd.read_csv(processed_file)


# Fix numeric columns — convert float-like numbers to integers safely
int_columns = ['Aging', 'Customer_ID', 'Quantity']

for col in int_columns:
    if col in df.columns:
        df[col] = pd.to_numeric(df[col], errors='coerce').fillna(0).astype(int)

        

# Also ensure numeric columns are proper decimals
float_columns = ['Sales', 'Discount', 'Profit', 'Shipping_Cost', 'Revenue']

for col in float_columns:
    if col in df.columns:
        df[col] = pd.to_numeric(df[col], errors='coerce').round(2)

# Rename columns to lowercase for PostgreSQL
df.columns = [col.lower() for col in df.columns]


# Upload to PostgreSQL (Order_ID is auto-generated)
upload_df(df, 'sales')
