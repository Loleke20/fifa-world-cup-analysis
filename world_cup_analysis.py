import pandas as pd
import matplotlib.pyplot as plt

# Load the World Cup data
df = pd.read_csv("world_cup_data.csv")

# Show the data
print("FIFA World Cup Data")
print(df)

# --------------------------------
# Basic Information
# --------------------------------

print("\nNumber of World Cups:")
print(len(df))

# --------------------------------
# Total Goals
# --------------------------------

total_goals = df["Total_Goals"].sum()

print("\nTotal Goals Across Tournaments:")
print(total_goals)

# --------------------------------
# Average Goals
# --------------------------------

average_goals = df["Total_Goals"].mean()

print("\nAverage Goals Per World Cup:")
print(round(average_goals, 2))

# --------------------------------
# Find the tournament with the
# most goals
# --------------------------------

highest_scoring = df.loc[df["Total_Goals"].idxmax()]

print("\nHighest Scoring World Cup:")
print(highest_scoring["Year"])

print("Goals:")
print(highest_scoring["Total_Goals"])

# --------------------------------
# Count World Cup Championships
# --------------------------------

championships = df["Champion"].value_counts()

print("\nWorld Cup Championships:")
print(championships)

# --------------------------------
# Create a graph showing goals
# over time
# --------------------------------

plt.figure(figsize=(10, 5))

plt.plot(
    df["Year"],
    df["Total_Goals"],
    marker="o"
)

plt.xlabel("World Cup Year")
plt.ylabel("Total Goals")

plt.title("FIFA World Cup Goals Over Time")

plt.grid(True)

plt.tight_layout()

plt.savefig("goals_by_year.png")

plt.show()

# --------------------------------
# Create championship graph
# --------------------------------

plt.figure(figsize=(10, 5))

championships.plot(kind="bar")

plt.xlabel("Country")
plt.ylabel("Number of Championships")

plt.title("FIFA World Cup Championships by Country")

plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig("championships_by_country.png")

plt.show()