import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Simulated customer churn dataset
data = {
    "CustomerID": range(1, 21),
    "Age": [25, 34, 45, 23, 30, 35, 40, 50, 29, 28, 33, 37, 48, 22, 27, 31, 38, 49, 26, 24],
    "Gender": ["Male", "Female", "Male", "Female", "Male", "Female", "Male", "Female", "Male", "Female",
               "Female", "Male", "Female", "Male", "Female", "Male", "Female", "Male", "Female", "Male"],
    "MonthlyCharges": [70, 80, 60, 75, 65, 85, 90, 50, 55, 60, 70, 75, 80, 55, 65, 85, 90, 50, 55, 75],
    "TenureMonths": [24, 36, 12, 48, 18, 60, 72, 6, 12, 24, 36, 48, 60, 6, 18, 30, 42, 54, 12, 24],
    "Churn": ["No", "Yes", "No", "No", "Yes", "No", "Yes", "No", "No", "Yes", "No", "No", "Yes", "No", "Yes", "No", "No", "Yes", "No", "No"]
}

# Create DataFrame
churn_df = pd.DataFrame(data)

# Display basic information
print("Basic Information:")
print(churn_df.info())
print("\nFirst 5 Rows:")
print(churn_df.head())

# Descriptive statistics
print("\nDescriptive Statistics:")
print(churn_df.describe())

# Convert categorical data to numeric for analysis
churn_df["Gender"] = churn_df["Gender"].map({"Male": 1, "Female": 0})
churn_df["Churn"] = churn_df["Churn"].map({"Yes": 1, "No": 0})

# Visualize the distribution of Monthly Charges
plt.figure(figsize=(10, 6))
sns.histplot(churn_df["MonthlyCharges"], kde=True, bins=10, color="blue")
plt.title("Distribution of Monthly Charges")
plt.xlabel("Monthly Charges")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig("monthly_charges_distribution.png")
plt.show()

# Correlation heatmap (numeric columns only)
numeric_df = churn_df.select_dtypes(include=[np.number])  # Select only numeric columns
correlation_matrix = numeric_df.corr()

plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Correlation Heatmap")
plt.tight_layout()
plt.savefig("correlation_heatmap.png")
plt.show()

# Churn rate by tenure visualization
plt.figure(figsize=(10, 6))
sns.boxplot(data=churn_df, x="Churn", y="TenureMonths", palette="Set2")
plt.title("Tenure Distribution by Churn Status")
plt.xlabel("Churn Status (0 = No, 1 = Yes)")
plt.ylabel("Tenure (Months)")
plt.tight_layout()
plt.savefig("tenure_churn_boxplot.png")
plt.show()

# Save the processed dataset for further analysis
output_file = r"C:\Users\Hughe\Downloads\Resume Work\processed_customer_churn.csv"
churn_df.to_csv(output_file, index=False)
print(f"Processed data saved to {output_file}")
