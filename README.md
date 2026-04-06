# Product ETL Pipeline

This project implements an **ETL (Extract, Transform, Load) workflow** to retrieve, process, and load product data into a SQL Server database.

---

## **Project Structure**

- `fetchData.py` – Retrieves product data from a source and saves it to `script.csv`.
- `cleanData.py` – Processes and cleans the raw CSV data, producing `script_cleaned.csv`.
- `loadProducts.py` – Inserts the cleaned data into a SQL Server database (`productDB`) using `pyodbc`.
- `script.csv` – Raw data file.
- `script_cleaned.csv` – Processed and cleaned data file.
- `SQLQuery1.sql` – SQL script to create the `products` table.

---

## **Requirements**

- Python 3.14+
- Libraries: `pandas`, `pyodbc`, `requests`
- SQL Server (local or remote) with a database named `productDB`
- ODBC Driver 18 for SQL Server

Install Python libraries using:

```bash
pip install pandas pyodbc requests
