import pandas as pd
import pyodbc
import ast  # for safely evaluating string representations of dicts

# -----------------------------
# Load CSV data
# -----------------------------
df = pd.read_csv("script.csv")
print(f"Loaded {len(df)} rows from CSV.")

# -----------------------------
# Connect to SQL Server
# -----------------------------
server = r'DESKTOP-VVFEEJF\MSSQLERVER1'
database = 'productDB'

conn = pyodbc.connect(
    f'DRIVER={{ODBC Driver 18 for SQL Server}};'
    f'SERVER={server};'
    f'DATABASE={database};'
    f'Trusted_Connection=yes;'
    f';Encrypt=no'  # local dev, disables SSL check
)
cursor = conn.cursor()
print("Connected to SQL Server successfully!")

# -----------------------------
# Insert CSV data into SQL table
# -----------------------------
for index, row in df.iterrows():
    rating_value = row['rating']

    # Convert string representation of dict to actual dict
    if isinstance(rating_value, str):
        rating_dict = ast.literal_eval(rating_value)
        rating_value = rating_dict.get('rate', 0)  # get the 'rate', default 0
    elif isinstance(rating_value, dict):
        rating_value = rating_value.get('rate', 0)

    # Insert into SQL table
    cursor.execute("""
        INSERT INTO dbo.products (id, title, price, description, category, image, rating)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """,
    row['id'],
    row['title'],
    row['price'],
    row['description'],
    row['category'],
    row['image'],
    float(rating_value)  # use float so SQL can accept decimal ratings
    )

# Commit changes
conn.commit()
conn.close()
print(f"Inserted {len(df)} products into dbo.products successfully!")