import pandas as pd
import matplotlib.pyplot as plt

# Create a dataset of quarterbacks
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
}

# Convert the data to a pandas DataFrame
qb_df = pd.DataFrame(data)

# Add new metrics
qb_df["Total TDs"] = qb_df["Passing TDs"] + qb_df["Rushing TDs"]
qb_df["Yards/Game"] = (qb_df["Passing Yards"] + qb_df["Rushing Yards"]) / qb_df["Games Played"]
qb_df["TD/INT Ratio"] = qb_df["Passing TDs"] / qb_df["Interceptions"]

# Display the dataset with calculated metrics
print("Quarterbacks Dataset with Advanced Metrics:")
print(qb_df)

# Plot Total Touchdowns for each QB
plt.figure(figsize=(10, 6))
plt.bar(qb_df["Name"], qb_df["Total TDs"], color="skyblue")
plt.title("Total Touchdowns by Quarterback")
plt.xlabel("Quarterbacks")
plt.ylabel("Total Touchdowns")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("Total_Touchdowns.png")  # Save the plot
plt.show()

# Find the QB with the highest Passer Rating
top_passer_rating = qb_df.loc[qb_df["Passer Rating"].idxmax()]
print(f"\nQuarterback with the highest Passer Rating:\n{top_passer_rating['Name']} ({top_passer_rating['Passer Rating']} rating)")

# Save the DataFrame to a CSV for further analysis
qb_df.to_csv("qb_analytics.csv", index=False)
print("\nData saved to 'qb_analytics.csv' and the plot saved as 'Total_Touchdowns.png'.")
