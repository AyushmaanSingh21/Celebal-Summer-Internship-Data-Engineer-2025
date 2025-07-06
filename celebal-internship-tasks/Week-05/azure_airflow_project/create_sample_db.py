import sqlite3

conn = sqlite3.connect("sample.db")
cursor = conn.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY,
    name TEXT,
    price REAL,
    quantity INTEGER
)
''')
cursor.executemany('''
INSERT INTO products (name, price, quantity)
VALUES (?, ?, ?)
''', [
    ("Laptop", 700.0, 10),
    ("Phone", 300.0, 25),
    ("Headphones", 50.0, 100),
])
conn.commit()
conn.close()
print("sample.db created with dummy data.")
