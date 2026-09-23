# Lesson 9 - SQL Tool

import sqlite3


def fetch_requirements_from_db():
    conn = sqlite3.connect("testing.db")
    cursor = conn.cursor()

    cursor.execute("SELECT field_name, field_type, min_len, max_len FROM requirements")
    rows = cursor.fetchall()

    conn.close()

    # प्रत्येक row ला वाचायला सोपं dictionary बनवू
    requirements = []
    for row in rows:
        requirements.append({
            "field_name": row[0],
            "field_type": row[1],
            "min_len": row[2],
            "max_len": row[3]
        })

    return requirements


# ---------- TOOL REGISTRY ----------
available_tools = {
    "fetch_requirements": fetch_requirements_from_db
}

print("Agent Thinking: I need to read requirements from the database...\n")

requirements = available_tools["fetch_requirements"]()

print("Requirements fetched from database:\n")
for req in requirements:
    print(req)