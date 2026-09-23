import json

requirement = {
    "field_name": "First Name",
    "field_type": "Text",
    "min_length": 3,
    "max_length": 20,
    "mandatory": True
}

print("Field Name:", requirement["field_name"])
print("Minimum Length:", requirement["min_length"])
print("Maximum Length:", requirement["max_length"])
print("Mandatory:", requirement["mandatory"])

json_data = json.dumps(requirement, indent=4)

print("\nJSON Format:")
print(json_data)