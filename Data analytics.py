import pandas as pd
df = pd.read_csv("sales_data.csv")
df.fillna(0, inplace=True)
df.drop_duplicates(inplace=True)

total_sales = df["Total_Sales"].sum()
average_sales = df["Total_Sales"].mean()
highest_sales = df["Total_Sales"].max()
lowest_sales = df["Total_Sales"].min()

best_selling_product = df.groupby("Product")["Total_Sales"].sum().idxmax()
print("Sales Analysis Report")
print(f"Total Revenue: ₹{total_sales}")
print(f"Average Sales: ₹{average_sales}")
print(f"Highest Sale: ₹{highest_sales}")
print(f"Lowest Sale: ₹{lowest_sales}")
print(f"Best-Selling Product: {best_selling_product}")
