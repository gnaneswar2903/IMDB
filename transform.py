import json
import pandas as pd

# Read JSON

with open("data/imdb_raw.json", "r") as file:
    data = json.load(file)

# Convert JSON to DataFrame

df = pd.DataFrame([data])

print("Original Data")
print(df.head())

print("\nMissing Values")
print(df.isnull().sum())

print("\nData Types")
print(df.dtypes)

# Convert datatypes

df["Year"] = df["Year"].str[:4]
df["Year"] = pd.to_numeric(df["Year"])

df["imdbRating"] = pd.to_numeric(df["imdbRating"])

# Remove unwanted columns

df.drop(
    columns=[
        "Poster",
        "Website",
        "DVD",
        "totalSeasons",
        "Response",
        "Ratings"
    ],
    errors="ignore",
    inplace=True
)

# Save CSV

df.to_csv("data/imdb_clean.csv", index=False)

print("\nClean CSV Created Successfully")