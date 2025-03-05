import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Generate a synthetic dataset for wide receivers
np.random.seed(42)
receivers = [
    "Justin Jefferson", "Tyreek Hill", "Davante Adams", "Stefon Diggs", "Ja'Marr Chase",
    "A.J. Brown", "CeeDee Lamb", "DeAndre Hopkins", "DK Metcalf", "Cooper Kupp",
    "Terry McLaurin", "Amari Cooper", "Garrett Wilson", "Chris Olave", "Deebo Samuel",
    "Mike Evans", "Keenan Allen", "Jaylen Waddle", "Tee Higgins", "Brandon Aiyuk"
]

data = {
    "Receiver": receivers,
    "Team": np.random.choice(
        ["MIN", "MIA", "LVR", "BUF", "CIN", "PHI", "DAL", "ARI", "SEA", "LAR",
         "WAS", "CLE", "NYJ", "NO", "SF", "TB", "LAC", "MIA", "CIN", "SF"], len(receivers)
    ),
    "Receptions": np.random.randint(50, 120, len(receivers)),
    "Targets": np.random.randint(80, 160, len(receivers)),
    "Yards": np.random.randint(700, 1800, len(receivers)),
    "Touchdowns": np.random.randint(2, 15, len(receivers)),
    "Yards Per Reception (Y/R)": np.random.uniform(10, 18, len(receivers)),
    "Yards After Catch (YAC)": np.random.randint(200, 700, len(receivers)),
    "Drop Rate (%)": np.random.uniform(0.5, 5.0, len(receivers)),
}

# Convert data to pandas DataFrame
wr_df = pd.DataFrame(data)

# Calculate new metrics
wr_df["Catch Rate (%)"] = (wr_df["Receptions"] / wr_df["Targets"] * 100).round(2)
wr_df["Yards Per Target (Y/T)"] = (wr_df["Yards"] / wr_df["Targets"]).round(2)

# Display dataset
print("Wide Receiver Dataset with Advanced Metrics:")
print(wr_df)

# Save the dataset to a CSV file
wr_df.to_csv("nfl_wide_receiver_stats.csv", index=False)

# Correlation analysis
print("\nCorrelation Matrix:")
correlation_matrix = wr_df[
    ["Receptions", "Targets", "Yards", "Touchdowns", "Yards After Catch (YAC)", "Catch Rate (%)", "Yards Per Target (Y/T)"]
].corr()
print(correlation_matrix)

# Visualize correlation matrix
plt.figure(figsize=(12, 8))
sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Correlation Heatmap for Wide Receiver Metrics")
plt.tight_layout()
plt.savefig("wr_correlation_heatmap.png")
plt.show()

# Scatterplot: Yards vs Touchdowns
plt.figure(figsize=(10, 6))
sns.scatterplot(data=wr_df, x="Yards", y="Touchdowns", hue="Receiver", s=100)
plt.title("Yards vs Touchdowns")
plt.xlabel("Yards")
plt.ylabel("Touchdowns")
plt.tight_layout()
plt.savefig("yards_vs_touchdowns.png")
plt.show()

# Scatterplot: Catch Rate vs Drop Rate
plt.figure(figsize=(10, 6))
sns.scatterplot(data=wr_df, x="Drop Rate (%)", y="Catch Rate (%)", hue="Receiver", s=100)
plt.title("Catch Rate vs Drop Rate")
plt.xlabel("Drop Rate (%)")
plt.ylabel("Catch Rate (%)")
plt.tight_layout()
plt.savefig("catch_rate_vs_drop_rate.png")
plt.show()

# Bar Plot: Top 5 Wide Receivers by Yards
top_5_yards = wr_df.nlargest(5, "Yards")
plt.figure(figsize=(10, 6))
sns.barplot(data=top_5_yards, x="Yards", y="Receiver", palette="viridis")
plt.title("Top 5 Wide Receivers by Yards")
plt.xlabel("Yards")
plt.ylabel("Receiver")
plt.tight_layout()
plt.savefig("top_5_wr_yards.png")
plt.show()

# Save results to files
wr_df.to_csv("nfl_wide_receiver_advanced_analysis.csv", index=False)
print("\nAnalysis complete. Results saved to 'nfl_wide_receiver_advanced_analysis.csv' and visualizations saved as images.")
