# Lesson 8 - Test Case Generator for Multiple Field Types

# ---------- TOOLS FOR TEXT FIELD ----------
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


# ---------- TOOLS FOR EMAIL FIELD ----------
def generate_email_field_cases():
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


# ---------- TOOLS FOR PASSWORD FIELD ----------
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


# ---------- TOOL REGISTRY ----------
available_tools = {
    "text": generate_text_field_cases,
    "email": generate_email_field_cases,
    "password": generate_password_field_cases
}


# ---------- AGENT ----------
class QAAgent:
    def __init__(self, tools):
        self.tools = tools

    def run(self, field_type, **kwargs):
        print(f"\nAgent Thinking: This is a '{field_type}' field. Selecting the right tool...\n")

        tool = self.tools.get(field_type)
        if not tool:
            print(f"No tool found for field type: {field_type}")
            return None

        if field_type == "email":
            positive, negative = tool()
        else:
            positive, negative = tool(kwargs.get("min_len"), kwargs.get("max_len"))

        return positive, negative


# ---------- RUN ----------
agent = QAAgent(tools=available_tools)

# Test 1: Text field
print("===== FIRST NAME FIELD =====")
pos, neg = agent.run("text", min_len=3, max_len=20)
print("Positive:", pos)
print("Negative:", neg)

# Test 2: Email field
print("\n===== EMAIL FIELD =====")
pos, neg = agent.run("email")
print("Positive:", pos)
print("Negative:", neg)

# Test 3: Password field
print("\n===== PASSWORD FIELD =====")
pos, neg = agent.run("password", min_len=8, max_len=16)
print("Positive:", pos)
print("Negative:", neg)