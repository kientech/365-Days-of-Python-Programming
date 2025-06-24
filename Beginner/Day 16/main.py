# Coding With Kien - 365 Days of Python Programming
# Beginner - Day 16

# Factorial Calculator

def factorial(n):
    """
    Calculates the factorial of a non-negative integer.
    """
    if n < 0:
        return "Factorial is not defined for negative numbers"
    elif n == 0:
        return 1
    else:
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result

# Example
try:
    num = int(input("Enter a number to calculate its factorial: "))
    print(f"The factorial of {num} is {factorial(num)}")
except ValueError:
    print("Invalid input. Please enter an integer.")

# Input: 5
# Output:
# The factorial of 5 is 120 