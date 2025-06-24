# Coding With Kien - 365 Days of Python Programming
# Beginner - Day 19

# Tip Calculator

try:
    bill = float(input("What was the total bill? $"))
    tip_percentage = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
    people = int(input("How many people to split the bill? "))

    tip_as_percent = tip_percentage / 100
    total_tip_amount = bill * tip_as_percent
    total_bill = bill + total_tip_amount
    bill_per_person = total_bill / people
    final_amount = round(bill_per_person, 2)

    print(f"Each person should pay: ${final_amount}")

except ValueError:
    print("Invalid input. Please enter valid numbers.")

# Example Input:
# What was the total bill? $124.56
# What percentage tip would you like to give? 12
# How many people to split the bill? 7

# Example Output:
# Each person should pay: $19.93 