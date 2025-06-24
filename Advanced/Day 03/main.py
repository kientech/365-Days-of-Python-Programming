# Coding With Kien - 365 Days of Python Programming
# Advanced - Day 03

# Create a context manager for file handling
from contextlib import contextmanager

@contextmanager
def open_file(filename, mode):
    try:
        f = open(filename, mode)
        yield f
    finally:
        f.close()

with open_file("sample.txt", "w") as f:
    f.write("This is a test.")

with open_file("sample.txt", "r") as f:
    print(f.read())

# Output:
# This is a test. 