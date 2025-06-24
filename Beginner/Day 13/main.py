# Coding With Kien - 365 Days of Python Programming
# Beginner - Day 13

# Simple Interest Calculator

def simple_interest(principal, rate, time):
    """
    Calculates simple interest.
    """
    return (principal * rate * time) / 100

# Example
p = 1000  # Principal
r = 5     # Rate of interest
t = 2     # Time in years

interest = simple_interest(p, r, t)
print(f"Principal: ${p}")
print(f"Rate: {r}%")
print(f"Time: {t} years")
print(f"Simple Interest: ${interest}")
print(f"Total amount: ${p + interest}")

# Input: Principal=1000, Rate=5, Time=2
# Output:
# Principal: $1000
# Rate: 5%
# Time: 2 years
# Simple Interest: $100.0
# Total amount: $1100.0 