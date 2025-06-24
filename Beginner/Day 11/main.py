# Coding With Kien - 365 Days of Python Programming
# Beginner - Day 11

# Count words in a string

def count_words(text):
    """
    Counts the number of words in a given string.
    """
    words = text.split()
    return len(words)

# Example
string_to_count = "This is a sample sentence for counting words."
word_count = count_words(string_to_count)
print(f"The string is: '{string_to_count}'")
print(f"Number of words: {word_count}")

# Input:
# "This is a sample sentence for counting words."
# Output:
# The string is: 'This is a sample sentence for counting words.'
# Number of words: 8 