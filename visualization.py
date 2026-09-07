import os
import pandas as pd
import matplotlib.pyplot as plt
from sqlalchemy import create_engine
from sqlalchemy.engine import URL

# Create graphs folder
os.makedirs("graphs", exist_ok=True)

# Database connection
connection_url = URL.create(
    drivername="mysql+pymysql",
    username="root",
    password="Gnana@2004",   # Your password
    host="localhost",
    port=3306,
    database="imdb_project"
)

engine = create_engine(connection_url)

# Read all movies from MySQL
query = """
SELECT Title, imdbRating
FROM movies
"""

df = pd.read_sql(query, engine)

# Convert rating to numeric
df["imdbRating"] = pd.to_numeric(df["imdbRating"])

# Create graph
plt.figure(figsize=(10,6))

bars = plt.bar(df["Title"], df["imdbRating"])

# Show rating on each bar
for bar in bars:
    plt.text(
        bar.get_x() + bar.get_width()/2,
        bar.get_height(),
        f"{bar.get_height():.1f}",
        ha="center",
        va="bottom"
    )

plt.title("IMDb Ratings")
plt.xlabel("Movie")
plt.ylabel("Rating")
plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig("graphs/imdb_rating.png")

print("✅ Graph saved successfully.")