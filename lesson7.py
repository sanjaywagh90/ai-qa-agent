# Lesson 7 - QA Agent (Rule-based, without real AI yet)

# ---------- ROLE ----------
agent_role = """
You are a Software Testing Assistant.
Your job is to analyze a requirement and generate test cases.
"""

# ---------- TOOLS ----------
def generate_positive_cases(min_len, max_len):
    return [
        f"Enter {min_len} alphabets (minimum boundary)",
        f"Enter {max_len} alphabets (maximum boundary)",
        "Enter valid alphabets within range"
    ]


def generate_negative_cases(min_len, max_len):
    return [
        "Leave field blank",
        f"Enter {min_len - 1} alphabets (below minimum)",
        f"Enter {max_len + 1} alphabets (above maximum)",
        "Enter numbers instead of alphabets",
        "Enter special characters"
    ]


def count_test_cases(positive, negative):
    return len(positive) + len(negative)


available_tools = {
    "generate_positive_cases": generate_positive_cases,
    "generate_negative_cases": generate_negative_cases,
    "count_test_cases": count_test_cases
}


# ---------- AGENT ----------
class QAAgent:
    def __init__(self, role, tools):
        self.role = role
        self.tools = tools

    def run(self, requirement_text, min_len, max_len):
        print("===== QA AGENT STARTED =====")
        print("\nRole:")
        print(self.role)

        print("Requirement:")
        print(requirement_text)

        # Agent decides which tools to call
        print("\nAgent Thinking: I need positive and negative test cases.\n")

        positive = self.tools["generate_positive_cases"](min_len, max_len)
        negative = self.tools["generate_negative_cases"](min_len, max_len)
        total = self.tools["count_test_cases"](positive, negative)

        # Final structured output
        result = {
            "positive_cases": positive,
            "negative_cases": negative,
            "total_cases": total
        }
        return result


# ---------- RUN ----------
requirement = """
First Name is a mandatory text field.
It should accept minimum 3 and maximum 20 alphabets.
"""

agent = QAAgent(role=agent_role, tools=available_tools)
output = agent.run(requirement, min_len=3, max_len=20)

print("\n----- FINAL OUTPUT -----")
print("\nPositive Cases:")
for case in output["positive_cases"]:
    print("-", case)

print("\nNegative Cases:")
for case in output["negative_cases"]:
    print("-", case)

print(f"\nTotal Test Cases: {output['total_cases']}")