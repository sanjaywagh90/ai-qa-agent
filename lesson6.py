# Lesson 6 - Tools

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


# ---- Tool Registry ----
# AI Agent ला माहीत असायला हवं की कोणती tools उपलब्ध आहेत
available_tools = {
    "generate_positive_cases": generate_positive_cases,
    "generate_negative_cases": generate_negative_cases,
    "count_test_cases": count_test_cases
}

print("Available Tools:")
for tool_name in available_tools:
    print("-", tool_name)