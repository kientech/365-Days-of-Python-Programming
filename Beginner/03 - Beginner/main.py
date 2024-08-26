# Coding With Kien - 365 Days of Python Programming
# Beginner - Oct 18, 2023

# How to calculate sum of numbers from 1 to n

n = int(input("Enter a number: "))
sum = 0

for i in range(1, n + 1):
    sum += i

print("Sum of numbers: ", sum)

# Input: Enter a number: 3
# Output: Sum of numbers: 6
