import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load cleaned dataset
df = pd.read_csv("cleaned_accidents.csv")

# ==========================================
# 1. Numerical Statistics

num_cols = [
    "Severity",
    "Distance(mi)",
    "Temperature(F)",
    "Humidity(%)",
    "Pressure(in)",
    "Visibility(mi)",
    "Wind_Speed(mph)",
    "Precipitation(in)",
    "Duration_Minutes"
]

stats = df[num_cols].describe()
print(stats)

# Save stats table
stats.to_csv("numerical_statistics.csv")

# ==========================================
# 2. Correlation Matrix

corr = df[num_cols].corr()

plt.figure(figsize=(10,8))
sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Correlation Matrix")
plt.tight_layout()
plt.savefig("correlation_heatmap.png")
plt.show()

# ==========================================
# 3. Severity Distribution

plt.figure(figsize=(6,4))
df["Severity"].value_counts().sort_index().plot(kind="bar")
plt.title("Accident Severity Distribution")
plt.xlabel("Severity")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig("severity_distribution.png")
plt.show()

# ==========================================
# 4. State Comparison

plt.figure(figsize=(6,4))
df["State"].value_counts().plot(kind="bar")
plt.title("Accidents by State")
plt.xlabel("State")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig("state_counts.png")
plt.show()

# ==========================================
# 5. Day vs Night

plt.figure(figsize=(6,4))
df["Sunrise_Sunset"].value_counts().plot(kind="bar")
plt.title("Day vs Night Accidents")
plt.xlabel("Time")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig("day_night.png")
plt.show()

# ==========================================
# 6. Top Weather Conditions

plt.figure(figsize=(10,5))
df["Weather_Condition"].value_counts().head(10).plot(kind="bar")
plt.title("Top 10 Weather Conditions")
plt.xlabel("Weather")
plt.ylabel("Count")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("weather_top10.png")
plt.show()

# ==========================================
# 7. Junction Effect

pd.crosstab(df["Junction"], df["Severity"]).plot(kind="bar", stacked=True, figsize=(8,5))
plt.title("Severity by Junction")
plt.xlabel("Junction")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig("junction_severity.png")
plt.show()

print("Statistical Analysis Complete.")