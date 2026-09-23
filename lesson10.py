# Lesson 10 - Full Agent Pipeline (DB + Field Tools combined)

import sqlite3


# ---------- SQL TOOL ----------
def fetch_requirements_from_db():
    conn = sqlite3.connect("testing.db")
    cursor = conn.cursor()
    cursor.execute("SELECT field_name, field_type, min_len, max_len FROM requirements")
    rows = cursor.fetchall()
    conn.close()

    requirements = []
    for row in rows:
        requirements.append({
            "field_name": row[0],
            "field_type": row[1],
            "min_len": row[2],
            "max_len": row[3]
        })
    return requirements


# ---------- FIELD-TYPE TOOLS ----------
def generate_text_field_cases(min_len, max_len):
    positive = [
        f"Enter {min_len} alphabets (minimum boundary)",
        f"Enter {max_len} alphabets (maximum boundary)",
        "Enter valid alphabets within range"
    ]
    negative = [
        "Leave field blank",
        f"Enter {min_len - 1} alphabets (below minimum)",
        f"Enter {max_len + 1} alphabets (above maximum)",
        "Enter numbers instead of alphabets",
        "Enter special characters"
    ]
    return positive, negative


def generate_email_field_cases(min_len=None, max_len=None):
    positive = [
        "Enter valid email (e.g. user@example.com)",
        "Enter email with subdomain (e.g. user@mail.example.com)"
    ]
    negative = [
        "Leave field blank",
        "Enter email without @ symbol",
        "Enter email without domain (e.g. user@)",
        "Enter email with spaces",
        "Enter email with special characters not allowed"
    ]
    return positive, negative


def generate_password_field_cases(min_len, max_len):
    positive = [
        f"Enter valid password with {min_len}-{max_len} chars, uppercase, number, special char",
        "Enter password exactly at minimum length with all required character types"
    ]
    negative = [
        "Leave field blank",
        f"Enter password below {min_len} characters",
        f"Enter password above {max_len} characters",
        "Enter password without uppercase letter",
        "Enter password without number",
        "Enter password without special character"
    ]
    return positive, negative


field_tools = {
    "text": generate_text_field_cases,
    "email": generate_email_field_cases,
    "password": generate_password_field_cases
}


# ---------- AGENT ----------
class QAAgent:
    def __init__(self, field_tools):
        self.field_tools = field_tools

    def run(self):
        print("===== QA AGENT STARTED =====\n")
        print("Agent Thinking: Fetching requirements from database...\n")

        requirements = fetch_requirements_from_db()

        final_report = []

        for req in requirements:
            field_name = req["field_name"]
            field_type = req["field_type"]
            min_len = req["min_len"]
            max_len = req["max_len"]

            print(f"Agent Thinking: '{field_name}' is a '{field_type}' field. Selecting tool...")

            tool = self.field_tools.get(field_type)
            if not tool:
                print(f"  No tool available for field type: {field_type}\n")
                continue

            positive, negative = tool(min_len, max_len)

            final_report.append({
                "field_name": field_name,
                "positive": positive,
                "negative": negative,
                "total": len(positive) + len(negative)
            })

        return final_report


# ---------- RUN ----------
agent = QAAgent(field_tools)
report = agent.run()

print("\n===== FINAL TEST CASE REPORT =====\n")

grand_total = 0
for item in report:
    print(f"Field: {item['field_name']}")
    print("Positive Cases:")
    for case in item["positive"]:
        print(f"  - {case}")
    print("Negative Cases:")
    for case in item["negative"]:
        print(f"  - {case}")
    print(f"Total for this field: {item['total']}\n")
    grand_total += item["total"]

print(f"GRAND TOTAL TEST CASES (all fields): {grand_total}")