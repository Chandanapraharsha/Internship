
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans, AgglomerativeClustering, DBSCAN
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
df = pd.read_csv("customer_churn.csv")

print("Dataset Preview:")
print(df.head())
df = pd.get_dummies(df, drop_first=True)
X = df.drop("Churn", axis=1)
y = df["Churn"]
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
wcss = []

for i in range(1,11):
    model = KMeans(n_clusters=i, random_state=42)
    model.fit(X_scaled)
    wcss.append(model.inertia_)

plt.plot(range(1,11), wcss, marker="o")
plt.title("Elbow Method")
plt.xlabel("No of Clusters")
plt.ylabel("WCSS")
plt.show()
kmeans = KMeans(n_clusters=3, random_state=42)
df["Segment"] = kmeans.fit_predict(X_scaled)
hc = AgglomerativeClustering(n_clusters=3)
df["HC_Segment"] = hc.fit_predict(X_scaled)
db = DBSCAN(eps=1.5, min_samples=5)
df["DBSCAN_Segment"] = db.fit_predict(X_scaled)

print("\nCluster Counts:")
print(df["Segment"].value_counts())
print("\nSegment Characteristics:")
print(df.groupby("Segment").mean())
results = []

for seg in df["Segment"].unique():

    print(f"\nTraining model for Segment {seg}")

    data = df[df["Segment"] == seg]

    X_seg = data.drop(["Churn","Segment","HC_Segment","DBSCAN_Segment"], axis=1)
    y_seg = data["Churn"]

    X_train, X_test, y_train, y_test = train_test_split(
        X_seg, y_seg, test_size=0.2, random_state=42
    )

    model = RandomForestClassifier()

    param_grid = {
        "n_estimators":[100,200],
        "max_depth":[5,10,None]
    }

    grid = GridSearchCV(model, param_grid, cv=3)
    grid.fit(X_train, y_train)

    best_model = grid.best_estimator_

    preds = best_model.predict(X_test)

    acc = accuracy_score(y_test,preds)
    prec = precision_score(y_test,preds)
    rec = recall_score(y_test,preds)
    f1 = f1_score(y_test,preds)

    results.append([seg,acc,prec,rec,f1])
results_df = pd.DataFrame(results, columns=["Segment","Accuracy","Precision","Recall","F1"])

print("\nMODEL PERFORMANCE:")
print(results_df)
importance = best_model.feature_importances_

features = pd.DataFrame({
    "Feature": X_seg.columns,
    "Importance": importance
}).sort_values("Importance", ascending=False)

print("\nTop Important Features:")
print(features.head())
print("\nBusiness Strategies:")

for seg in df["Segment"].unique():
    if seg == 0:
        print("Segment 0 → Offer loyalty rewards + premium services")
    elif seg == 1:
        print("Segment 1 → Give discounts + retention offers")
    else:
        print("Segment 2 → Provide onboarding + guidance")
results_df.to_csv("model_results.csv", index=False)
df.to_csv("segmented_customers.csv", index=False)

print("\nFiles Saved:")
print("✔ model_results.csv")
print("✔ segmented_customers.csv")

print("\nPROJECT COMPLETED SUCCESSFULLY 🎯")
