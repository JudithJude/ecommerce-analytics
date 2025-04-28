import pandas as pd
from sqlalchemy import create_engine
import os

#PostgreSQL connection parameters from environment variables
POSTGRES_USER = os.getenv("POSTGRES_USER")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
POSTGRES_DB = os.getenv("POSTGRES_DB")
POSTGRES_HOST = os.getenv("POSTGRES_HOST")  # fallback to localhost
PORT = 5432

#creating database engine
engine = create_engine(f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{PORT}/{POSTGRES_DB}")

#mapping CSV files to table names
files = {
    "olist_customers_dataset.csv": "customers",
    "olist_geolocation_dataset.csv": "geolocation",
    "olist_order_items_dataset.csv": "order_items",
    "olist_order_payments_dataset.csv": "order_payments",
    "olist_order_reviews_dataset.csv": "order_reviews",
    "olist_orders_dataset.csv": "orders",
    "olist_products_dataset.csv": "products",
    "olist_sellers_dataset.csv": "sellers",
    "product_category_name_translation.csv": "product_category_translation"
}

DATA_DIR = "./data"

for file_name, table_name in files.items():
    path = os.path.join(DATA_DIR, file_name)
    print(f"Loading {path} into {table_name}...")
    df = pd.read_csv(path)
    df.to_sql(table_name, engine, index = False, if_exists = "replace")
    print(f"{table_name} loaded successfully.")

print("ETL process completed.")