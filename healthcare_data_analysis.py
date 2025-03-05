import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Simulate healthcare dataset
np.random.seed(42)
num_patients = 1000

data = {
    "Patient_ID": np.arange(1, num_patients + 1),
    "Age": np.random.randint(18, 90, num_patients),
    "Gender": np.random.choice(["Male", "Female"], num_patients),
    "Diagnosis": np.random.choice(
        ["Hypertension", "Diabetes", "Asthma", "Heart Disease", "Healthy"], num_patients
    ),
    "Visits_Last_Year": np.random.randint(1, 20, num_patients),
    "Annual_Expenditure ($)": np.random.randint(500, 10000, num_patients),
    "Medication_Adherence (%)": np.random.uniform(50, 100, num_patients).round(2),
    "Hospital_Readmissions": np.random.randint(0, 3, num_patients),
}

# Convert data to pandas DataFrame
healthcare_df = pd.DataFrame(data)

# Add derived metrics
healthcare_df["High Risk"] = healthcare_df["Diagnosis"].apply(
    lambda x: 1 if x in ["Hypertension", "Heart Disease"] else 0
)

# Display dataset
print("Healthcare Dataset:")
print(healthcare_df.head())

# Save the dataset
healthcare_df.to_csv("healthcare_patient_data.csv", index=False)

# Summary statistics
print("\nSummary Statistics:")
summary = healthcare_df.describe()
print(summary)

# Analyze and visualize data
# Gender distribution
gender_counts = healthcare_df["Gender"].value_counts()
plt.figure(figsize=(8, 6))
sns.barplot(x=gender_counts.index, y=gender_counts.values, palette="pastel")
plt.title("Gender Distribution")
plt.xlabel("Gender")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig("gender_distribution.png")
plt.show()

# Diagnosis distribution
diagnosis_counts = healthcare_df["Diagnosis"].value_counts()
plt.figure(figsize=(10, 6))
sns.barplot(x=diagnosis_counts.index, y=diagnosis_counts.values, palette="muted")
plt.title("Diagnosis Distribution")
plt.xlabel("Diagnosis")
plt.ylabel("Count")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("diagnosis_distribution.png")
plt.show()

# Scatterplot: Age vs Annual Expenditure
plt.figure(figsize=(10, 6))
sns.scatterplot(data=healthcare_df, x="Age", y="Annual_Expenditure ($)", hue="Diagnosis", alpha=0.7)
plt.title("Age vs Annual Expenditure by Diagnosis")
plt.xlabel("Age")
plt.ylabel("Annual Expenditure ($)")
plt.tight_layout()
plt.savefig("age_vs_expenditure.png")
plt.show()

# Correlation matrix
print("\nCorrelation Matrix:")
correlation_matrix = healthcare_df[
    ["Age", "Visits_Last_Year", "Annual_Expenditure ($)", "Medication_Adherence (%)", "Hospital_Readmissions"]
].corr()
print(correlation_matrix)

# Heatmap of correlations
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Correlation Heatmap")
plt.tight_layout()
plt.savefig("healthcare_correlation_heatmap.png")
plt.show()

# High-risk patients: Average expenditure and adherence
high_risk_group = healthcare_df[healthcare_df["High Risk"] == 1]
avg_expenditure = high_risk_group["Annual_Expenditure ($)"].mean()
avg_adherence = high_risk_group["Medication_Adherence (%)"].mean()

print(f"\nHigh-Risk Patients - Average Expenditure: ${avg_expenditure:.2f}")
print(f"High-Risk Patients - Average Medication Adherence: {avg_adherence:.2f}%")

# Save high-risk patient data
high_risk_group.to_csv("high_risk_patients.csv", index=False)

# Barplot: Top diagnoses by readmissions
readmission_counts = healthcare_df.groupby("Diagnosis")["Hospital_Readmissions"].sum().sort_values(ascending=False)
plt.figure(figsize=(10, 6))
sns.barplot(x=readmission_counts.index, y=readmission_counts.values, palette="flare")
plt.title("Total Readmissions by Diagnosis")
plt.xlabel("Diagnosis")
plt.ylabel("Readmissions")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("readmissions_by_diagnosis.png")
plt.show()

print("\nAnalysis complete. Results saved to CSV files and visualizations saved as images.")
