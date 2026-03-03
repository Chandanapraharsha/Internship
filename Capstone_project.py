import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import joblib
from flask import Flask, request, jsonify

from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    roc_auc_score,
    classification_report,
    confusion_matrix
)

df = pd.read_csv("customer_churn.csv")

print("First 5 Rows:\n")
print(df.head())

print("\nDataset Info:\n")
print(df.info())

print("\nMissing Values:\n")
print(df.isnull().sum())

le = LabelEncoder()

for col in df.select_dtypes(include='object').columns:
    df[col] = le.fit_transform(df[col])

print("\nAfter Encoding:\n")
print(df.head())

plt.figure()
sns.heatmap(df.corr(), annot=True)
plt.title("Correlation Matrix")
plt.show()

plt.figure()
df['Churn'].value_counts().plot(kind='bar')
plt.title("Churn Distribution (0 = No, 1 = Yes)")
plt.show()

X = df.drop("Churn", axis=1)
y = df["Churn"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print("\nModel Performance:\n")

print("Accuracy:", accuracy_score(y_test, y_pred))
print("Precision:", precision_score(y_test, y_pred))
print("Recall:", recall_score(y_test, y_pred))
print("F1 Score:", f1_score(y_test, y_pred))
print("ROC AUC:", roc_auc_score(y_test, y_pred))

print("\nClassification Report:\n")
print(classification_report(y_test, y_pred))

print("\nConfusion Matrix:\n")
print(confusion_matrix(y_test, y_pred))
param_grid = {
    'n_estimators': [100, 200],
    'max_depth': [None, 10, 20],
    'min_samples_split': [2, 5]
}

grid = GridSearchCV(
    RandomForestClassifier(random_state=42),
    param_grid,
    cv=3,
    scoring='f1'
)

grid.fit(X_train, y_train)

print("\nBest Parameters:\n", grid.best_params_)

best_model = grid.best_estimator_
y_pred_best = best_model.predict(X_test)

print("\nImproved Accuracy:", accuracy_score(y_test, y_pred_best))
print("Improved F1 Score:", f1_score(y_test, y_pred_best))

joblib.dump(best_model, "churn_model.pkl")
print("\nModel saved as churn_model.pkl")
app = Flask(__name__)
loaded_model = joblib.load("churn_model.pkl")

@app.route("/")
def home():
    return "Customer Churn Prediction API Running"

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json["features"]
    prediction = loaded_model.predict([data])
    return jsonify({"Churn Prediction": int(prediction[0])})

if __name__ == "__main__":
    print("\nStarting Flask API...")
    app.run(debug=True)