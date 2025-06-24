# Coding With Kien - 365 Days of Python Programming
# Beginner - Day 14

# Check if a number is even or odd

try:
    num = int(input("Enter a number: "))
    if num % 2 == 0:
        print(f"The number {num} is Even.")
    else:
        print(f"The number {num} is Odd.")
except ValueError:
    print("Invalid input. Please enter an integer.")

# Example 1 Input:
# Enter a number: 4
# Example 1 Output:
# The number 4 is Even.

# Example 2 Input:
# Enter a number: 7
# Example 2 Output:
# The number 7 is Odd. 