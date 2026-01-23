
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from scipy import stats
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

sales = pd.read_csv("sales_data.csv")

print("\n===== DATA PREVIEW =====")
print(sales.head())

print("\n===== DATA INFO =====")
print(sales.info())

print("\n===== DESCRIPTIVE STATISTICS =====")
print(sales.describe())
mean_sales = sales['Sales'].mean()
median_sales = sales['Sales'].median()
mode_sales = sales['Sales'].mode()[0]
std_sales = sales['Sales'].std()
var_sales = sales['Sales'].var()

print("\n===== MANUAL STATISTICS =====")
print("Mean:", mean_sales)
print("Median:", median_sales)
print("Mode:", mode_sales)
print("Standard Deviation:", std_sales)
print("Variance:", var_sales)
plt.figure(figsize=(6,4))
sns.histplot(sales['Sales'], kde=True)
plt.title("Sales Distribution")
plt.xlabel("Sales")
plt.ylabel("Frequency")
plt.show()
stat, p = stats.shapiro(sales['Sales'])
print("\nShapiro Test p-value:", p)
print("Normally Distributed" if p > 0.05 else "Not Normally Distributed")
correlation_matrix = sales.corr(numeric_only=True)
print("\n===== CORRELATION MATRIX =====")
print(correlation_matrix)

plt.figure(figsize=(6,4))
sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()

corr_sales_marketing = sales['Sales'].corr(sales['Marketing_Spend'])
print("\nSales-Marketing Correlation:", corr_sales_marketing)
t1, p1 = stats.ttest_1samp(sales['Sales'], 40000)
print("\nOne Sample t-test p-value:", p1)
region1 = sales[sales['Region']=="East"]['Sales']
region2 = sales[sales['Region']=="West"]['Sales']
t2, p2 = stats.ttest_ind(region1, region2, equal_var=False)
print("Independent t-test p-value:", p2)
groups = [sales[sales['Region']==r]['Sales'] for r in sales['Region'].unique()]
f_stat, p3 = stats.f_oneway(*groups)
print("ANOVA p-value:", p3)
n = len(sales)
ci = stats.t.interval(0.95, n-1, loc=mean_sales, scale=std_sales/np.sqrt(n))
margin_error = ci[1] - mean_sales

print("\n===== CONFIDENCE INTERVAL =====")
print("Mean Sales:", mean_sales)
print("95% CI:", ci)
print("Margin of Error:", margin_error)

X = sales[['Marketing_Spend']]
y = sales['Sales']

model = LinearRegression()
model.fit(X, y)

pred = model.predict(X)
r2 = r2_score(y, pred)

print("\n===== REGRESSION RESULTS =====")
print("Coefficient:", model.coef_[0])
print("Intercept:", model.intercept_)
print("R-squared:", r2)

plt.figure(figsize=(6,4))
plt.scatter(X, y)
plt.plot(X, pred)
plt.xlabel("Marketing Spend")
plt.ylabel("Sales")
plt.title("Marketing Spend vs Sales")
plt.show()
print("\n===== STATISTICAL BUSINESS SUMMARY =====")
print("Average Sales:", round(mean_sales,2))
print("Standard Deviation:", round(std_sales,2))
print("Sales-Marketing Correlation:", round(corr_sales_marketing,2))
print("Marketing impact significance (p):", p1)
print("R-squared:", round(r2,2))
with open("hypothesis_tests_results.txt", "w") as f:
    f.write("STATISTICAL TEST RESULTS\n\n")
    f.write("One sample t-test p-value: " + str(p1) + "\n")
    f.write("Independent t-test p-value: " + str(p2) + "\n")
    f.write("ANOVA p-value: " + str(p3) + "\n")
    f.write("Sales-Marketing Correlation: " + str(corr_sales_marketing) + "\n")
    f.write("R-squared: " + str(r2))

print("\nResults saved to hypothesis_tests_results.txt")
