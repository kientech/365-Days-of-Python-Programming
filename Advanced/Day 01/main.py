# Coding With Kien - 365 Days of Python Programming
# Advanced - Day 01

# Implement a decorator to time function execution
import time

def timer_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Execution time of {func.__name__}: {end_time - start_time:.4f}s")
        return result
    return wrapper

@timer_decorator
def my_function(n):
    sum = 0
    for i in range(n):
        sum += i
    return sum

my_function(1000000)

# Example Output:
# Execution time of my_function: 0.0567s 