import sqlite3

conn = sqlite3.connect("vitals.db", check_same_thread=False)

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS vitals(
id INTEGER PRIMARY KEY AUTOINCREMENT,
patient_id INT,
heart_rate INT,
spo2 INT,
temperature REAL,
status TEXT
)
""")

conn.commit()