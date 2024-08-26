# Coding With Kien - 365 Days of Python Programming
# Beginner - Oct 17, 2023

# A Part of Big Project - Tips Calculation  

print("Welcome to the tip calculator!")

bill = float(input("What is the total bill amount?\n$:"))
tip = int(input("How much tip would you like to give?\nPercent:"))
split = int(input("How many people to split the bill?\nPeople:"))

total = ("{:.2f}".format((((bill * (tip / 100)) + bill) / split)))

print(f"Each person should pay: ${total}")

# Input: 
#     Welcome to the tip calculator!
#     What is the total bill amount?
#     $:124
#     How much tip would you like to give?
#     Percent:20
#     How many people to split the bill?
#     People:4
# Output:
#     Each person should pay: $37.20