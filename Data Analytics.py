
import pandas as pd
df = pd.read_csv("sales_data.csv")

print("Dataset loaded successfully!\n")
print("First 5 rows of the dataset:")
print(df.head(), "\n")
print("Dataset Shape (Rows, Columns):")
print(df.shape, "\n")
print("Column Names:")
print(df.columns.tolist(), "\n")
print("Dataset Information:")
print(df.info(), "\n")
print("Missing values before cleaning:")
print(df.isnull().sum(), "\n")
df.fillna(0, inplace=True)
df.drop_duplicates(inplace=True)

print("Data cleaning completed!\n")
total_sales = df["Total_Sales"].sum()

average_sales = df["Total_Sales"].mean()
highest_sales = df["Total_Sales"].max()
lowest_sales = df["Total_Sales"].min()
best_selling_product = (
    df.groupby("Product")["Total_Sales"]
    .sum()
    .idxmax()
)

print("========== SALES ANALYSIS REPORT ==========\n")

print(f"Total Revenue        : ₹{total_sales:,.2f}")
print(f"Average Sales Value  : ₹{average_sales:,.2f}")
print(f"Highest Sale Value   : ₹{highest_sales:,.2f}")
print(f"Lowest Sale Value    : ₹{lowest_sales:,.2f}")
print(f"Best-Selling Product : {best_selling_product}")

print("\n===========================================")
