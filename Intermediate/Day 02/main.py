# Coding With Kien - 365 Days of Python Programming
# Intermediate - Day 02

# Check if a string is a palindrome

def is_palindrome(s):
    # remove spaces and convert to lowercase
    s = s.replace(" ", "").lower()
    return s == s[::-1]

string = "A man a plan a canal Panama"
if is_palindrome(string):
    print(f'"{string}" is a palindrome.')
else:
    print(f'"{string}" is not a palindrome.')

# Input: "A man a plan a canal Panama"
# Output: "A man a plan a canal Panama" is a palindrome. 