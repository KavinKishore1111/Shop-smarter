import pandas as pd
import os

# Build absolute path to the CSV
base_dir = os.path.dirname(os.path.dirname(__file__))  # Goes from src → 05project
file_path = os.path.join(base_dir, "data", "raw", "ecommerce_data.csv")
processed_dir = os.path.join(base_dir, "data", "processed") 
print(f"📂 Loading data from: {file_path}")
df = pd.read_csv(file_path)

# Create processed folder if it doesn't exist
os.makedirs(processed_dir, exist_ok=True)



# Inspect basic info
print(df.head())
print(df.info())
print(df.describe())

# Convert Order_Date to datetime
df['Order_Date'] = pd.to_datetime(df['Order_Date'], errors='coerce')

# Fill missing numeric values
df.fillna({'Discount': 0, 'Shipping_Cost': 0, 'Profit': 0, 'Aging':0}, inplace=True)

# Drop rows with missing crucial values
df.dropna(subset=['Customer_Id', 'Product', 'Product_Category', 'Sales', 'Quantity'], inplace=True)

# Strip text columns
text_cols = ['Gender','Device_Type','Customer_Login_type','Product_Category','Product','Order_Priority','Payment_method']
for col in text_cols:
    df[col] = df[col].astype(str).str.strip()

# Calculate Revenue
df['Revenue'] = df['Sales'] * df['Quantity']



processed_path = os.path.join(processed_dir, "ecommerce_cleaned.csv")
df.to_csv(processed_path, index=False)
print(f"Data cleaning complete. Saved to {processed_path}")
