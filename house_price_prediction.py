
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler, PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
df = pd.read_csv("house_data.csv")

print("Dataset Shape:", df.shape)
display(df.head())
print("\nMissing Values:")
print(df.isnull().sum())
print("\nBasic Statistics:")
display(df.describe())
plt.figure(figsize=(6,4))
plt.scatter(df['Area'], df['Price'])
plt.title("Area vs Price")
plt.xlabel("Area (sq ft)")
plt.ylabel("House Price")
plt.show()

plt.figure(figsize=(6,4))
plt.scatter(df['Bedrooms'], df['Price'])
plt.title("Bedrooms vs Price")
plt.xlabel("Bedrooms")
plt.ylabel("House Price")
plt.show()
df = df.dropna()  
le = LabelEncoder()
df['Location'] = le.fit_transform(df['Location'])

X = df[['Area', 'Bedrooms', 'Location']]
y = df['Price']
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
x = df['Area'].values
y = df['Price'].values

m = np.cov(x, y)[0, 1] / np.var(x)
c = np.mean(y) - m * np.mean(x)

print("\nLinear Regression (From Scratch)")
print("Slope (m):", m)
print("Intercept (c):", c)
lr_model = LinearRegression()
lr_model.fit(X_train_scaled, y_train)

y_pred_lr = lr_model.predict(X_test_scaled)
mae = mean_absolute_error(y_test, y_pred_lr)
mse = mean_squared_error(y_test, y_pred_lr)
r2 = r2_score(y_test, y_pred_lr)

print("\n===== LINEAR REGRESSION RESULTS =====")
print("MAE:", mae)
print("MSE:", mse)
print("R² Score:", r2)
plt.figure(figsize=(6,4))
plt.scatter(y_test, y_pred_lr)
plt.xlabel("Actual Prices")
plt.ylabel("Predicted Prices")
plt.title("Predicted vs Actual House Prices")
plt.savefig("predictions_vs_actual.png")
plt.show()
poly = PolynomialFeatures(degree=2)
X_train_poly = poly.fit_transform(X_train_scaled)
X_test_poly = poly.transform(X_test_scaled)

poly_model = LinearRegression()
poly_model.fit(X_train_poly, y_train)

y_pred_poly = poly_model.predict(X_test_poly)

print("\n===== POLYNOMIAL REGRESSION =====")
print("R² Score:", r2_score(y_test, y_pred_poly))
dt_model = DecisionTreeRegressor(random_state=42)
dt_model.fit(X_train, y_train)
y_pred_dt = dt_model.predict(X_test)

print("\n===== DECISION TREE =====")
print("R² Score:", r2_score(y_test, y_pred_dt))

rf_model = RandomForestRegressor(n_estimators=100, random_state=42)
rf_model.fit(X_train, y_train)
y_pred_rf = rf_model.predict(X_test)

print("\n===== RANDOM FOREST =====")
print("R² Score:", r2_score(y_test, y_pred_rf))
importance = pd.DataFrame({
    "Feature": X.columns,
    "Importance": rf_model.feature_importances_
}).sort_values(by="Importance", ascending=False)

print("\nFeature Importance:")
display(importance)
import joblib
joblib.dump(lr_model, "house_price_model.pkl")
print("\nModel saved as house_price_model.pkl")
