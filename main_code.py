import pandas as pd
import os
import re
from datetime import datetime
from sqlalchemy import create_engine

data_folder = "./data"  
db_url = "postgresql://john:q4qfc2xiQzP6xRgI2T@do6uk2gs739ijf0-a:5432/data_export"
engine = create_engine(db_url)


def extract_date_from_filename(filename):
    match = re.search(r'(\d{8})', filename)
    if match:
        date_str = match.group(1)
        date = datetime.strptime(date_str, "%Y%m%d").date()
        return date, date_str
    return None, None

def process_cust_mstr(filepath, filename):
    df = pd.read_csv(filepath)
    date, _ = extract_date_from_filename(filename)
    df['Date'] = date
    engine.execute("TRUNCATE TABLE CUST_MSTR")
    df.to_sql("CUST_MSTR", con=engine, if_exists='append', index=False)
    print(f"✅ Loaded {filename} into CUST_MSTR")

def process_master_child(filepath, filename):
    df = pd.read_csv(filepath)
    date, datekey = extract_date_from_filename(filename)
    df['Date'] = date
    df['DateKey'] = datekey
    engine.execute("TRUNCATE TABLE master_child")
    df.to_sql("master_child", con=engine, if_exists='append', index=False)
    print(f"✅ Loaded {filename} into master_child")

def process_ecom_order(filepath, filename):
    df = pd.read_csv(filepath)
    engine.execute("TRUNCATE TABLE H_ECOM_Orders")
    df.to_sql("H_ECOM_Orders", con=engine, if_exists='append', index=False)
    print(f"✅ Loaded {filename} into H_ECOM_Orders")    

for filename in os.listdir(data_folder):
    if not filename.endswith(".csv"):
        continue

    filepath = os.path.join(data_folder, filename)

    if filename.startswith("CUST_MSTR"):
        process_cust_mstr(filepath, filename)
    elif filename.startswith("master_child_export"):
        process_master_child(filepath, filename)
    elif filename.startswith("H_ECOM_ORDER"):
        process_ecom_order(filepath, filename)
    else:
        print(f"⛔ Unknown file type: {filename}")