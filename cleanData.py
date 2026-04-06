import pandas as pd

# reading my CSV file
df = pd.read_csv("script.csv")

# Remove duplicate rows
df_cleaned = df.drop_duplicates()

# reset the index
df_cleaned.reset_index(drop=True, inplace=True)

# Save the cleaned CSV
df_cleaned.to_csv("script_cleaned.csv", index=False)

print(f"Removed duplicates. {len(df) - len(df_cleaned)} duplicate rows were dropped.")
