#Charts_File

"""
import pandas as pd
import matplotlib.pyplot as plt

# ==================================================
#Colorado Has More Severe Accidents Than Oklahoma
#Stacked bar chart of Severity by State

df = pd.read_csv("cleaned_accidents.csv")

pd.crosstab(df["State"], df["Severity"]).plot(kind="bar", stacked=True, figsize=(8,5))
plt.title("Severity Comparison: CO vs OK")
plt.xlabel("State")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig("story_state_severity.png")
plt.show()

# ==================================================
#Nighttime Accidents Are More Severe
#Severity by Day/Night
pd.crosstab(df["Sunrise_Sunset"], df["Severity"]).plot(kind="bar", stacked=True, figsize=(8,5))
plt.title("Severity by Day vs Night")
plt.tight_layout()
plt.savefig("story_day_night_severity.png")
plt.show()

# ==================================================
#Junctions Increase Risk

pd.crosstab(df["Junction"], df["Severity"]).plot(kind="bar", stacked=True, figsize=(8,5))
plt.title("Severity by Junction")
plt.tight_layout()
plt.savefig("story_junction.png")
plt.show()

# ==================================================
#Traffic Signals Reduce Severe Outcomes
pd.crosstab(df["Traffic_Signal"], df["Severity"]).plot(kind="bar", stacked=True, figsize=(8,5))
plt.title("Severity by Traffic Signal")
plt.tight_layout()
plt.savefig("story_signal.png")
plt.show()

# ==================================================
#Accident Time Peaks Differ by State

df["Start_Time"] = pd.to_datetime(df["Start_Time"])
df["Hour"] = df["Start_Time"].dt.hour

hourly = df.groupby(["Hour","State"]).size().unstack()

hourly.plot(figsize=(10,5))
plt.title("Accidents by Hour and State")
plt.xlabel("Hour")
plt.ylabel("Count")
plt.grid(True)
plt.tight_layout()
plt.savefig("story_hourly_state.png")
plt.show()

# ==================================================
#Weather Conditions Affect Severity
pd.crosstab(df["Weather_Condition"], df["Severity"]).plot(kind="bar", stacked=True, figsize=(10,5))
plt.title("Severity by Weather Condition")
plt.xlabel("Weather Condition")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig("story_weather_severity.png")
plt.show()



top_weather = df["Weather_Condition"].value_counts().head(10).index

weather_df = df[df["Weather_Condition"].isin(top_weather)]

pd.crosstab(
    weather_df["Weather_Condition"],
    weather_df["Severity"]
).plot(kind="bar", stacked=True, figsize=(12,6))
plt.title("Severity by Top Weather Conditions")
plt.xlabel("Weather Condition")
plt.ylabel("Count")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("story_weather_severity.png")
plt.show()

"""