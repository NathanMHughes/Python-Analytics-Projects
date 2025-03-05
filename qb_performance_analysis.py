import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Create a dataset of quarterbacks with more detailed stats
data = {
    "Name": ["Josh Allen", "Patrick Mahomes", "Jalen Hurts", "Joe Burrow", "Justin Herbert"],
    "Team": ["Bills", "Chiefs", "Eagles", "Bengals", "Chargers"],
    "Games Played": [16, 17, 15, 16, 17],
    "Passing Yards": [4283, 5250, 3701, 4475, 4739],
    "Passing TDs": [35, 41, 22, 35, 25],
    "Interceptions": [14, 12, 6, 12, 10],
    "Completion %": [63.3, 67.1, 66.5, 68.3, 67.0],
    "Passer Rating": [91.5, 105.2, 101.5, 100.8, 93.2],
    "Rushing Yards": [762, 358, 760, 257, 147],
    "Rushing TDs": [7, 4, 13, 5, 0],
    "Sacks Taken": [33, 26, 38, 41, 35],
    "Fumbles": [5, 2, 8, 4, 6],
}

# Convert the data to a pandas DataFrame
qb_df = pd.DataFrame(data)

# Calculate new metrics
qb_df["Total Yards"] = qb_df["Passing Yards"] + qb_df["Rushing Yards"]
qb_df["Total TDs"] = qb_df["Passing TDs"] + qb_df["Rushing TDs"]
qb_df["Yards/Attempt"] = qb_df["Passing Yards"] / qb_df["Games Played"]
qb_df["TD/Turnover Ratio"] = qb_df["Total TDs"] / (qb_df["Interceptions"] + qb_df["Fumbles"])

# Display the dataset with calculated metrics
print("Quarterbacks Dataset with Advanced Metrics:")
print(qb_df)

# Correlation Analysis
print("\nCorrelation Matrix:")
correlation_matrix = qb_df[["Passing Yards", "Passing TDs", "Interceptions", "Rushing Yards", "Passer Rating", "Total Yards"]].corr()
print(correlation_matrix)

# Visualize the correlation matrix
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Correlation Heatmap")
plt.tight_layout()
plt.savefig("qb_correlation_heatmap.png")
plt.show()

# Scatter Plot: Passing Yards vs. Passer Rating
plt.figure(figsize=(8, 6))
sns.scatterplot(data=qb_df, x="Passing Yards", y="Passer Rating", hue="Name", s=100)
plt.title("Passing Yards vs. Passer Rating")
plt.xlabel("Passing Yards")
plt.ylabel("Passer Rating")
plt.tight_layout()
plt.savefig("passing_yards_vs_passer_rating.png")
plt.show()

# Save the enhanced DataFrame to a CSV
qb_df.to_csv("qb_performance_analysis.csv", index=False)
print("\nAnalysis complete. Data saved to 'qb_performance_analysis.csv', and visualizations saved as images.")
