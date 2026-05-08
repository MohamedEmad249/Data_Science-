import pandas as pd
import numpy as np

# Load dataset
df = pd.read_csv("filtered_states.csv")

print("Original Shape:", df.shape)

# ==================================================
# 1. Convert Date Columns

df["Start_Time"] = pd.to_datetime(df["Start_Time"], errors="coerce")
df["End_Time"] = pd.to_datetime(df["End_Time"], errors="coerce")
df["Weather_Timestamp"] = pd.to_datetime(df["Weather_Timestamp"], errors="coerce")

# ==================================================
# 2. Create Duration Column (minutes)

df["Duration_Minutes"] = (
    df["End_Time"] - df["Start_Time"]
).dt.total_seconds() / 60

# ==================================================
# 3. Remove Negative Durations

df = df[df["Duration_Minutes"] >= 0]

# ==================================================
# 4. Handle Missing Values

# Fill numeric columns with median
numeric_cols = [
    "Temperature(F)", "Wind_Chill(F)", "Humidity(%)",
    "Pressure(in)", "Visibility(mi)", "Wind_Speed(mph)",
    "Precipitation(in)"
]

for col in numeric_cols:
    if col in df.columns:
        df[col].fillna(df[col].median(), inplace=True)

# Fill categorical columns with mode
categorical_cols = [
    "Weather_Condition", "Wind_Direction",
    "Sunrise_Sunset", "Civil_Twilight"
]

for col in categorical_cols:
    if col in df.columns:
        df[col].fillna(df[col].mode()[0], inplace=True)

# ==================================================
# 5. Remove Columns With Too Many Missing Values

drop_cols = ["End_Lat", "End_Lng"]
df.drop(columns=drop_cols, inplace=True, errors="ignore")

# ==================================================
# 6. Standardize Text Values

df["Weather_Condition"] = df["Weather_Condition"].str.strip().str.title()

# ==================================================
# 7. Remove Duplicate Rows

df.drop_duplicates(inplace=True)

# ==================================================
# 8. Remove Outliers Using IQR (Duration)

Q1 = df["Duration_Minutes"].quantile(0.25)
Q3 = df["Duration_Minutes"].quantile(0.75)
IQR = Q3 - Q1

lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR

df = df[
    (df["Duration_Minutes"] >= lower) &
    (df["Duration_Minutes"] <= upper)
]

# ==================================================
# 9. Keep Only CO and OK (Validation)

df = df[df["State"].isin(["CO", "OK"])]

# ==================================================
# 10. Save Cleaned Dataset

df.to_csv("cleaned_accidents.csv", index=False)

print("Cleaned Shape:", df.shape)
print("Cleaning Complete.")