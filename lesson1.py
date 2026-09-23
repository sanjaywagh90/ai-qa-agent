def get_qa_scenarios():
    scenarios = [
        "Enter numbers in First Name field",
        "Enter special characters",
        "Leave First Name blank",
        "Enter less than 3 alphabets",
        "Enter more than 20 alphabets"
    ]

    return scenarios


result = get_qa_scenarios()

print(result)