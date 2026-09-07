import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.engine import URL

# Create database connection
connection_url = URL.create(
    drivername="mysql+pymysql",
    username="root",
    password="Gnana@2004",   # Your MySQL password
    host="localhost",
    port=3306,
    database="imdb_project"
)

engine = create_engine(connection_url)

query = """
SELECT *
FROM movies
"""

df = pd.read_sql(query, engine)

print(df)