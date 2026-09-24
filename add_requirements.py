# add_requirements.py - Database मध्ये नवीन field requirements ऍड करण्यासाठी

import sqlite3

conn = sqlite3.connect("testing.db")
cursor = conn.cursor()

new_data = [
    ("Age", "number", 18, 60),
    ("Date of Birth", "date", None, None),
    ("Country", "dropdown", None, None),
]

cursor.executemany(
    "INSERT INTO requirements (field_name, field_type, min_len, max_len) VALUES (?, ?, ?, ?)",
    new_data
)

conn.commit()
conn.close()

print("New requirements added successfully.")