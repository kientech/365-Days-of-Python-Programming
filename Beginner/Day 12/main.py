# Coding With Kien - 365 Days of Python Programming
# Beginner - Day 12

# Temperature converter (Celsius to Fahrenheit and vice versa)

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

# Example
celsius_temp = 25
fahrenheit_temp = fahrenheit_to_celsius(celsius_temp)
print(f"{celsius_temp}°C is equal to {fahrenheit_temp:.2f}°F")

fahrenheit_temp = 77
celsius_temp = fahrenheit_to_celsius(fahrenheit_temp)
print(f"{fahrenheit_temp}°F is equal to {celsius_temp:.2f}°C")

# Input: 25°C, 77°F
# Output:
# 25°C is equal to 77.00°F
# 77°F is equal to 25.00°C 