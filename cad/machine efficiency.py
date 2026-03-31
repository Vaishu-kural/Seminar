import pandas as pd

data = {
    "Machine": ["M1","M2","M3","M4","M5"],
    "Working_Hours": [8,8,7,9,8],
    "Units_Produced": [400,450,390,500,470]
}

df = pd.DataFrame(data)

# Efficiency calculation
df["Efficiency"] = df["Units_Produced"] / df["Working_Hours"]

print("Machine Efficiency Report")
print(df)

best_machine = df.loc[df["Efficiency"].idxmax()]
print("\nBest Performing Machine:", best_machine["Machine"])

