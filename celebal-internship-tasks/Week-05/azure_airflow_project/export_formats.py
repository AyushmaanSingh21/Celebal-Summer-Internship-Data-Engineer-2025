import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq
from fastavro import writer, parse_schema
import sqlite3
import os
from dotenv import load_dotenv

print("✅ Script started")

# Load environment variables
load_dotenv()

print("🔗 Connecting to SQLite")
conn = sqlite3.connect("sample.db")
df = pd.read_sql_query("SELECT * FROM products", conn)
print(f"📦 Data loaded: {len(df)} rows")

# Export to CSV
df.to_csv("products.csv", index=False)
print("✅ CSV exported")

# Export to Parquet
table = pa.Table.from_pandas(df)
pq.write_table(table, "products.parquet")
print("✅ Parquet exported")

# Export to Avro
records = df.to_dict(orient="records")
schema = {
    "doc": "Product table",
    "name": "Product",
    "namespace": "product.avro",
    "type": "record",
    "fields": [
        {"name": "id", "type": "int"},
        {"name": "name", "type": "string"},
        {"name": "price", "type": "float"},
        {"name": "quantity", "type": "int"}
    ]
}
parsed_schema = parse_schema(schema)
with open("products.avro", "wb") as out:
    writer(out, parsed_schema, records)
print("✅ Avro exported")