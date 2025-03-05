import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Create a dataset of NFL teams with performance metrics
data = {
    "Team": [
        "Buffalo Bills", "Kansas City Chiefs", "Philadelphia Eagles",
        "Cincinnati Bengals", "San Francisco 49ers", "Dallas Cowboys",
        "Minnesota Vikings", "Jacksonville Jaguars", "New York Giants",
        "Miami Dolphins"
    ],
    "Wins": [13, 14, 14, 12, 13, 12, 13, 9, 9, 9],
    "Losses": [3, 3, 3, 4, 4, 5, 4, 8, 7, 8],
    "Points Scored": [455, 496, 477, 418, 450, 467, 424, 404, 365, 397],
    "Points Allowed": [286, 369, 344, 322, 277, 342, 427, 350, 371, 399],
    "Turnovers": [27, 23, 19, 18, 20, 23, 24, 17, 16, 21],
    "Takeaways": [30, 20, 27, 24, 30, 33, 25, 27, 19, 14],
    "Yards Gained": [6393, 7044, 6564, 6131, 5831, 6214, 6009, 5784, 5683, 5842],
    "Yards Allowed": [5100, 5997, 5546, 5408, 5117, 5434, 6187, 5582, 5554, 5883],
}

# Convert the data to a pandas DataFrame
team_df = pd.DataFrame(data)

# Calculate new metrics
team_df["Point Differential"] = team_df["Points Scored"] - team_df["Points Allowed"]
team_df["Net Turnovers"] = team_df["Takeaways"] - team_df["Turnovers"]
team_df["Yards Differential"] = team_df["Yards Gained"] - team_df["Yards Allowed"]

# Display the dataset with calculated metrics
print("NFL Teams Dataset with Advanced Metrics:")
print(team_df)

# Correlation Analysis
print("\nCorrelation Matrix:")
correlation_matrix = team_df[
    ["Wins", "Points Scored", "Points Allowed", "Point Differential", "Net Turnovers", "Yards Differential"]
].corr()
print(correlation_matrix)

# Visualize the correlation matrix
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Correlation Heatmap for Team Metrics")
plt.tight_layout()
plt.savefig("team_correlation_heatmap.png")
plt.show()

# Scatter Plot: Point Differential vs Wins
plt.figure(figsize=(8, 6))
sns.scatterplot(data=team_df, x="Point Differential", y="Wins", hue="Team", s=100)
plt.title("Point Differential vs Wins")
plt.xlabel("Point Differential")
plt.ylabel("Wins")
plt.tight_layout()
plt.savefig("point_differential_vs_wins.png")
plt.show()

# Scatter Plot: Net Turnovers vs Wins
plt.figure(figsize=(8, 6))
sns.scatterplot(data=team_df, x="Net Turnovers", y="Wins", hue="Team", s=100)
plt.title("Net Turnovers vs Wins")
plt.xlabel("Net Turnovers")
plt.ylabel("Wins")
plt.tight_layout()
plt.savefig("net_turnovers_vs_wins.png")
plt.show()

# Save the enhanced DataFrame to a CSV
team_df.to_csv("nfl_team_performance_analysis.csv", index=False)
print("\nAnalysis complete. Data saved to 'nfl_team_performance_analysis.csv', and visualizations saved as images.")
