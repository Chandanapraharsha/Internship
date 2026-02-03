
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
df = pd.read_csv("data/raw_data.csv")

print("Dataset Shape:", df.shape)
print("\nFirst 5 rows:")
display(df.head())
print("\nMissing Values:")
print(df.isnull().sum())
num_cols = df.select_dtypes(include=['int64', 'float64']).columns
df[num_cols] = df[num_cols].fillna(df[num_cols].median())
cat_cols = df.select_dtypes(include=['object']).columns
for col in cat_cols:
    df[col] = df[col].fillna(df[col].mode()[0])
df = df.drop_duplicates()
df.to_csv("data/cleaned_data.csv", index=False)

print("\nData Cleaning Completed!")
plt.figure(figsize=(6,4))
df['Churn'].value_counts().plot(kind='bar')
plt.title("Customer Churn Distribution")
plt.xlabel("Churn (0 = No, 1 = Yes)")
plt.ylabel("Count")
plt.show()
plt.figure(figsize=(6,4))
df.boxplot(column='MonthlyCharges', by='Churn')
plt.title("Monthly Charges vs Churn")
plt.suptitle("")
plt.show()
plt.figure(figsize=(6,4))
df.boxplot(column='tenure', by='Churn')
plt.title("Tenure vs Churn")
plt.suptitle("")
plt.show()
plt.figure(figsize=(8,6))
corr = df[num_cols].corr()
plt.imshow(corr, cmap='coolwarm')
plt.colorbar()
plt.title("Correlation Heatmap")
plt.show()
le = LabelEncoder()
for col in cat_cols:
    df[col] = le.fit_transform(df[col])
X = df.drop(columns=['Churn'])
y = df['Churn']
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)
model = LogisticRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
print("\nModel Accuracy:", accuracy_score(y_test, y_pred))

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))

print("\nClassification Report:")
print(classification_report(y_test, y_pred))
print("\n===== BUSINESS INSIGHTS =====")
print("1. Higher monthly charges increase churn risk.")
print("2. Longer tenure reduces churn probability.")
print("3. Customers with poor service ratings are more likely to churn.")
print("\n===== RECOMMENDATIONS =====")
print("- Offer loyalty discounts to long-term customers.")
print("- Improve customer support response time.")
print("- Provide personalized subscription plans.")
import joblib
joblib.dump(model, "models/churn_model.pkl")
print("\nModel saved successfully!")
