# Coding With Kien - 365 Days of Python Programming
# Beginner - Day 15

# Find the largest of three numbers

def find_largest(num1, num2, num3):
    if (num1 >= num2) and (num1 >= num3):
        largest = num1
    elif (num2 >= num1) and (num2 >= num3):
        largest = num2
    else:
        largest = num3
    return largest

# Example
a = 10
b = 25
c = 15

largest_number = find_largest(a, b, c)
print(f"The numbers are {a}, {b}, and {c}.")
print(f"The largest number is {largest_number}.")

# Input: 10, 25, 15
# Output:
# The numbers are 10, 25, and 15.
# The largest number is 25. 