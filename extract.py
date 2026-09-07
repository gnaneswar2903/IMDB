import requests
import json
import sys
from config import API_KEY, BASE_URL

# -----------------------------
# Take movie name from the user
# -----------------------------
movie = input("Enter movie name: ").strip()

# -----------------------------
# Create API URL
# -----------------------------
url = f"{BASE_URL}?t={movie}&apikey={API_KEY}"

print("\nFetching movie data from OMDb API...")

try:
    # -----------------------------
    # Send request to API
    # -----------------------------
    response = requests.get(url)

    # Check if request was successful
    response.raise_for_status()

    # Convert JSON response to Python dictionary
    data = response.json()

    # -----------------------------
    # Check whether movie exists
    # -----------------------------
    if data.get("Response") == "True":

        print("\n✅ Movie Found!\n")

        # Save raw JSON file
        with open("data/imdb_raw.json", "w") as file:
            json.dump(data, file, indent=4)

        print("✅ Raw JSON saved successfully.")
        print(f"Movie: {data['Title']}")
        print(f"Year : {data['Year']}")
        print(f"IMDb Rating : {data['imdbRating']}")

    else:
        print("\n❌ Movie not found!")
        print("Reason:", data.get("Error"))

        # Stop the ETL pipeline
        sys.exit("ETL Pipeline Stopped.")

except requests.exceptions.RequestException as e:
    print("\n❌ Error while connecting to the API")
    print(e)

    sys.exit("ETL Pipeline Stopped.")