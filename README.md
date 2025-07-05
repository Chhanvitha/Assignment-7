This project automates the process of reading multiple types of CSV files from a local directory, processing them based on file name patterns, and loading them into their respective SQL database tables. The logic also includes column transformations based on filename content.

## Use Case

You may receive daily data files of different types:

- `CUST_MSTR_YYYYMMDD.csv`
- `master_child_export-YYYYMMDD.csv`
- `H_ECOM_ORDER.csv`

This script:
- Processes each file type appropriately
- Adds columns derived from filenames
- Truncates the relevant database tables
- Loads data into PostgreSQL or any other SQL database using SQLAlchemy

---

##  File Structure


project/
├── data/
│ ├── CUST_MSTR_20191112.csv
│ ├── master_child_export-20191112.csv
│ ├── H_ECOM_ORDER.csv
├── main.py
├── README.md

How to Run
1. Install Required Libraries

pip install pandas sqlalchemy psycopg2-binary
You can replace psycopg2-binary with a different SQL driver if needed.

2. Configure main.py
Set your local folder path:

data_folder = "./data"
Set your database connection URL:

db_url = "postgresql://username:password@localhost:5432/your_db"
You can use any SQLAlchemy-supported database: PostgreSQL, MySQL, SQLite, etc.

Ensure these tables exist in your database:

CUST_MSTR

master_child

H_ECOM_Orders

3.  Run the Script

python main.py



