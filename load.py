import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.engine import URL

# Read CSV
df = pd.read_csv("data/imdb_clean.csv")

# Create connection URL
connection_url = URL.create(
    drivername="mysql+pymysql",
    username="root",
    password="Gnana@2004",   # Your MySQL password
    host="localhost",
    port=3306,
    database="imdb_project"
)

engine = create_engine(connection_url)

# Load data into MySQL
df.to_sql("movies", engine, if_exists="append", index=False)

print("✅ Data Loaded Successfully into MySQL")