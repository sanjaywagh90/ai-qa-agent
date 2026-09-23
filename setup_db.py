# setup_db.py - एकदाच run करायचं, sample database तयार करण्यासाठी

import sqlite3

conn = sqlite3.connect("testing.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS requirements (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    field_name TEXT,
    field_type TEXT,
    min_len INTEGER,
    max_len INTEGER
)
""")

cursor.execute("DELETE FROM requirements")  # जुना डेटा साफ करा (पुन्हा run केल्यास duplicate टाळण्यासाठी)

sample_data = [
    ("First Name", "text", 3, 20),
    ("Email", "email", None, None),
    ("Password", "password", 8, 16),
]

cursor.executemany(
    "INSERT INTO requirements (field_name, field_type, min_len, max_len) VALUES (?, ?, ?, ?)",
    sample_data
)

conn.commit()
conn.close()

print("Database and table created successfully. Sample data inserted.")