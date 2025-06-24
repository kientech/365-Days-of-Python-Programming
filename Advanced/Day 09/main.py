# Coding With Kien - 365 Days of Python Programming
# Advanced - Day 09

# Simple Caching with Decorators
import time
import functools

def cache(func):
    """A simple cache decorator."""
    cache_dict = {}
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Use a tuple of args and sorted kwargs items for the key
        key = (args, tuple(sorted(kwargs.items())))
        if key not in cache_dict:
            print(f"Cache miss for {key}. Running function...")
            cache_dict[key] = func(*args, **kwargs)
        else:
            print(f"Cache hit for {key}. Returning cached result.")
        return cache_dict[key]
    return wrapper

@cache
def slow_function(n):
    """A function that simulates a slow computation."""
    time.sleep(2)
    return n * 2

# First call - should be slow
print(f"Result: {slow_function(5)}")
print("-" * 20)
# Second call with same argument - should be fast
print(f"Result: {slow_function(5)}")
print("-" * 20)
# Third call with different argument - should be slow again
print(f"Result: {slow_function(10)}")

# Example Output:
# Cache miss for ((5,),). Running function...
# Result: 10
# --------------------
# Cache hit for ((5,),). Returning cached result.
# Result: 10
# --------------------
# Cache miss for ((10,),). Running function...
# Result: 20 