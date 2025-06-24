# Coding With Kien - 365 Days of Python Programming
# Intermediate - Day 06

# Read from and write to a JSON file
import json

# Data to be written to a JSON file
data = {
    "name": "John Doe",
    "age": 30,
    "isStudent": False,
    "courses": [
        {"title": "History", "credits": 3},
        {"title": "Math", "credits": 4}
    ]
}

filename = "data.json"

# Writing to a JSON file
with open(filename, 'w') as f:
    json.dump(data, f, indent=4)

print(f"Data has been written to {filename}")

# Reading from a JSON file
with open(filename, 'r') as f:
    loaded_data = json.load(f)

print("\nData loaded from JSON file:")
print(loaded_data)
print(f"Name: {loaded_data['name']}")

# Output:
# Data has been written to data.json
#
# Data loaded from JSON file:
# {'name': 'John Doe', 'age': 30, 'isStudent': False, 'courses': [{'title': 'History', 'credits': 3}, {'title': 'Math', 'credits': 4}]}
# Name: John Doe 