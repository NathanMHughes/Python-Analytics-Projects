import pandas as pd

# Create a dataset of quarterbacks
data = {
    "Name": ["Josh Allen", "Patrick Mahomes", "Jalen Hurts", "Joe Burrow", "Justin Herbert"],
    "Team": ["Bills", "Chiefs", "Eagles", "Bengals", "Chargers"],
    "Passing Yards": [4283, 5250, 3701, 4475, 4739],
    "Touchdowns": [35, 41, 22, 35, 25],
    "Interceptions": [14, 12, 6, 12, 10],
}

# Convert the data to a pandas DataFrame
qb_df = pd.DataFrame(data)

# Display the dataset
print("Quarterbacks Dataset:")
print(qb_df)

# Calculate and display a new column for TD-INT differential
qb_df["TD-INT Differential"] = qb_df["Touchdowns"] - qb_df["Interceptions"]
print("\nDataset with TD-INT Differential:")
print(qb_df)

# Find the QB with the most passing yards
top_passer = qb_df.loc[qb_df["Passing Yards"].idxmax()]
print(f"\nQuarterback with the most passing yards:\n{top_passer['Name']} ({top_passer['Passing Yards']} yards)")
