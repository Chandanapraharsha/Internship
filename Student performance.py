

import pandas as pd
import matplotlib.pyplot as plt

try:  
    data = pd.read_csv("student_data.csv")
    print("Dataset loaded successfully!\n")
    print("First 5 rows of the dataset:")
    print(data.head())

    
    print("\nMissing values:")
    print(data.isnull().sum())
    print("\nBasic Statistics:")
    print(data.describe())
    avg_marks_gender = data.groupby("Gender")["Marks"].mean()
    print("\nAverage Marks by Gender:")
    print(avg_marks_gender)
    print("\nStudy Hours vs Marks:")
    print(data[["Study_Hours", "Marks"]])
    plt.figure()
    avg_marks_gender.plot(kind="bar")
    plt.title("Average Marks by Gender")
    plt.xlabel("Gender")
    plt.ylabel("Average Marks")
    plt.tight_layout()
    plt.savefig("avg_marks_by_gender.png")
    plt.show()
    plt.figure()
    plt.plot(data["Study_Hours"], data["Marks"], marker="o")
    plt.title("Study Hours vs Marks")
    plt.xlabel("Study Hours")
    plt.ylabel("Marks")
    plt.tight_layout()
    plt.savefig("study_hours_vs_marks.png")
    plt.show()

    print("\nCharts generated and saved successfully!")

except FileNotFoundError:
    print("Error: student_data.csv file not found.")
except Exception as e:
    print("An error occurred:", e)
