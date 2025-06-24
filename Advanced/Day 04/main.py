# Coding With Kien - 365 Days of Python Programming
# Advanced - Day 04

# Basic multithreading example
import threading
import time

def print_numbers():
    for i in range(5):
        print(i)
        time.sleep(1)

def print_letters():
    for letter in "abcde":
        print(letter)
        time.sleep(1)

# Create two threads
thread1 = threading.Thread(target=print_numbers)
thread2 = threading.Thread(target=print_letters)

# Start the threads
thread1.start()
thread2.start()

# Wait for both threads to finish
thread1.join()
thread2.join()

print("Done!")

# Example Output (the order of numbers and letters may vary):
# 0
# a
# 1
# b
# 2
# c
# 3
# d
# 4
# e
# Done! 