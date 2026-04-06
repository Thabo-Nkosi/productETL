#declaring libraries
import requests
import pandas as pd

url = "https://fakestoreapi.com/products"

try:
    response = requests.get(url)
    data = response.json()
    print(f"fetched {len(data)} products successfully.....! ")

# saving the raw data to csv
    df = pd.DataFrame(data)
    df.to_csv("script.csv", index=False)
    print("Raw data have been successfully saved to script.cv")

except requests.exceptions.RequestException as e:
    print("Error fetching data:", e)
