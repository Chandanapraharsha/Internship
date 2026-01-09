
import pandas as pd
import matplotlib.pyplot as plt
sales = pd.read_csv("sales_data.csv")
customers = pd.read_csv("customer_data.csv")
churn = pd.read_csv("customer_churn.csv")

print("=== Sales Data ===")
print(sales.head())
print("\n=== Customer Data ===")
print(customers.head())

print("\n=== Missing Values (Sales) ===")
print(sales.isnull().sum())
sales['order_date'] = pd.to_datetime(sales['order_date'])
sales['year'] = sales['order_date'].dt.year
sales['month'] = sales['order_date'].dt.month
sales['day'] = sales['order_date'].dt.day

sales.dropna(inplace=True)
sales['total_price'] = sales['quantity'] * sales['price']

print("\n=== Cleaned Sales Data ===")
print(sales.head())
merged = pd.merge(sales, customers, on="customer_id", how="inner")

print("\n=== Merged Data ===")
print(merged.head())
top_customers = merged.groupby("customer_name")['total_price'].sum().sort_values(ascending=False)
print("\n=== Top Customers ===")
print(top_customers.head(10))
clv = merged.groupby("customer_id")['total_price'].sum()
print("\n=== Customer Lifetime Value ===")
print(clv.head())
region_sales = merged.groupby("region")['total_price'].sum()
print("\n=== Region Wise Sales ===")
print(region_sales)
monthly_sales = merged.groupby("month")['total_price'].sum()
print("\n=== Monthly Sales ===")
print(monthly_sales)
best_products = merged.groupby("product")['quantity'].sum().sort_values(ascending=False)
print("\n=== Best Selling Products ===")
print(best_products)
pivot_table = pd.pivot_table(
    merged,
    values='total_price',
    index='region',
    columns='product',
    aggfunc='sum'
)

print("\n=== Pivot Table (Region vs Product) ===")
print(pivot_table)
repeat_customers = merged['customer_id'].value_counts()
retained_customers = repeat_customers[repeat_customers > 1].count()

print("\nRepeat Customers Count:", retained_customers)

total_revenue = merged['total_price'].sum()
total_customers = merged['customer_id'].nunique()
avg_order_value = merged['total_price'].mean()

print("\n=== BUSINESS SUMMARY ===")
print("Total Revenue:", total_revenue)
print("Total Customers:", total_customers)
print("Average Order Value:", avg_order_value)
monthly_sales.plot(kind='bar', title="Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.show()
top_customers.head(5).plot(kind='pie', autopct='%1.1f%%')
plt.title("Top 5 Customers Contribution")
plt.ylabel("")
plt.show()
region_sales.plot(kind='barh', title="Sales by Region")
plt.xlabel("Total Sales")
plt.show()
best_products.head(5).plot(kind='line', title="Top 5 Best-Selling Products")
plt.ylabel("Quantity Sold")
plt.show()
print("\n=== PROJECT COMPLETED SUCCESSFULLY ===")
