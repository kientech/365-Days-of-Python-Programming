# Coding With Kien - 365 Days of Python Programming
# Advanced - Day 02

# Use a generator to produce Fibonacci numbers

def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

fib = fibonacci_generator()

print("First 10 Fibonacci numbers:")
for _ in range(10):
    print(next(fib))

# Output:
# First 10 Fibonacci numbers:
# 0
# 1
# 1
# 2
# 3
# 5
# 8
# 13
# 21
# 34 