
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import os
sns.set_theme(style="darkgrid")
plt.rcParams["figure.figsize"] = (8,5)

if not os.path.exists("visualizations"):
    os.makedirs("visualizations")
data = {
    "Date": pd.date_range(start="2025-01-01", periods=20, freq="D"),
    "Category": ["Electronics","Clothing","Grocery","Electronics","Clothing"] * 4,
    "Product": ["A","B","C","D","E"] * 4,
    "Sales": [1200,800,500,1500,700,1100,850,600,1400,750,1300,900,550,1600,720,1250,880,580,1550,760],
    "Profit": [200,120,80,300,100,180,130,90,280,110,230,140,85,320,105,210,135,88,310,115],
    "Customer_Type": ["New","Returning","New","Returning","New"] * 4
}

df = pd.DataFrame(data)
df.to_csv("sales_data.csv", index=False)
df = pd.read_csv("sales_data.csv")
df["Date"] = pd.to_datetime(df["Date"])
print(df.head())
plt.figure()
sns.boxplot(x="Category", y="Sales", data=df)
plt.title("Sales Distribution by Category")
plt.savefig("visualizations/boxplot.png")
plt.show()
plt.figure()
sns.violinplot(x="Customer_Type", y="Sales", data=df)
plt.title("Sales Distribution by Customer Type")
plt.savefig("visualizations/violinplot.png")
plt.show()
plt.figure(figsize=(6,5))
corr = df[["Sales","Profit"]].corr()
sns.heatmap(corr, annot=True, cmap="coolwarm")
plt.title("Sales vs Profit Correlation")
plt.savefig("visualizations/heatmap.png")
plt.show()
fig, axs = plt.subplots(2, 2, figsize=(12,10))

sns.boxplot(x="Category", y="Sales", data=df, ax=axs[0,0])
axs[0,0].set_title("Box Plot")

sns.violinplot(x="Customer_Type", y="Sales", data=df, ax=axs[0,1])
axs[0,1].set_title("Violin Plot")

sns.barplot(x="Category", y="Profit", data=df, ax=axs[1,0])
axs[1,0].set_title("Profit by Category")

sns.histplot(df["Sales"], kde=True, ax=axs[1,1])
axs[1,1].set_title("Sales Distribution")

fig.suptitle("Sales Dashboard Overview", fontsize=16)
plt.tight_layout()
plt.show()
fig1 = px.line(df, x="Date", y="Sales", color="Category",
               title="Interactive Sales Trend")
fig1.show()
fig2 = px.bar(df, x="Category", y="Sales", color="Category",
              title="Category-wise Sales",
              hover_data=["Profit"])
fig2.show()
fig3 = px.pie(df, names="Category", values="Sales",
              title="Sales Share by Category")
fig3.show()
fig1.write_html("interactive_sales_dashboard.html")

print("Dashboard created successfully!")
