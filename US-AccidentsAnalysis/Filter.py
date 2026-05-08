import pandas as pd

# Load dataset
df = pd.read_csv("US_Accidents_March23.csv")

state1 = "CO"
state2 = "OK"

# Filter rows
filtered_df = df[df["State"].isin([state1, state2])]

# Save result
filtered_df.to_csv("filtered_states.csv", index=False)

print("Original rows:", len(df))
print("Filtered rows:", len(filtered_df))
print(filtered_df["State"].value_counts())