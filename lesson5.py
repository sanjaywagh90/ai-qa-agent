# Lesson 5 - AI QA Agent

agent_role = """
You are a Software Testing Assistant.

Your responsibilities are:
1. Understand the software requirement.
2. Identify positive test scenarios.
3. Identify negative test scenarios.
4. Generate clear test cases.
5. Follow the requirement carefully.
"""

requirement = """
First Name is a mandatory text field.
It should accept minimum 3 and maximum 20 alphabets.
"""

print("===== AI QA AGENT =====")

print("\nAgent Role:")
print(agent_role)

print("\nUser Requirement:")
print(requirement)

def generate_test_scenarios(min_len, max_len):
    positive = [
        f"Enter {min_len} alphabets (minimum boundary)",
        f"Enter {max_len} alphabets (maximum boundary)",
        f"Enter valid alphabets within range"
    ]

    negative = [
        "Leave field blank",
        f"Enter {min_len - 1} alphabets (below minimum)",
        f"Enter {max_len + 1} alphabets (above maximum)",
        "Enter numbers instead of alphabets",
        "Enter special characters"
    ]

    return positive, negative


print("===== AI QA AGENT =====")
print("\nAgent Role:")
print(agent_role)

print("\nUser Requirement:")
print(requirement)

positive_cases, negative_cases = generate_test_scenarios(3, 20)

print("\nPositive Scenarios:")
for i, case in enumerate(positive_cases, 1):
    print(f"{i}. {case}")

print("\nNegative Scenarios:")
for i, case in enumerate(negative_cases, 1):
    print(f"{i}. {case}")

