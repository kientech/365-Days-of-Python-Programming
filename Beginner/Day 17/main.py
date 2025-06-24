# Coding With Kien - 365 Days of Python Programming
# Beginner - Day 17

# Vowel Counter

def count_vowels(s):
    """
    Counts the number of vowels in a given string.
    """
    vowels = "aeiouAEIOU"
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count

# Example
input_string = "Hello World, this is a test string."
vowel_count = count_vowels(input_string)
print(f"The string is: '{input_string}'")
print(f"Number of vowels: {vowel_count}")

# Input: "Hello World, this is a test string."
# Output:
# The string is: 'Hello World, this is a test string.'
# Number of vowels: 8 