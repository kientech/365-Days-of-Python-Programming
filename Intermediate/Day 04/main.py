# Coding With Kien - 365 Days of Python Programming
# Intermediate - Day 04

# Read and write to a CSV file
import csv

# Data to be written to the CSV file
data = [
    ["Name", "Age", "City"],
    ["John", 30, "New York"],
    ["Peter", 22, "London"],
    ["Anna", 28, "Paris"]
]

filename = "people.csv"

# Writing to a CSV file
with open(filename, "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(data)

print(f"Data has been written to {filename}")

# Reading from a CSV file
with open(filename, "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

# Output:
# Data has been written to people.csv
# ['Name', 'Age', 'City']
# ['John', '30', 'New York']
# ['Peter', '22', 'London']
# ['Anna', '28', 'Paris'] 