# Coding With Kien - 365 Days of Python Programming
# Beginner - Day 18

# Anagram Checker

def are_anagrams(str1, str2):
    """
    Checks if two strings are anagrams of each other.
    """
    # Remove spaces and convert to lowercase to make the check case-insensitive
    # and space-insensitive.
    s1 = str1.replace(" ", "").lower()
    s2 = str2.replace(" ", "").lower()
    
    # Anagrams must have the same length
    if len(s1) != len(s2):
        return False
        
    # Sort the characters of both strings and compare them
    return sorted(s1) == sorted(s2)

# Example
string1 = "Listen"
string2 = "Silent"
if are_anagrams(string1, string2):
    print(f'"{string1}" and "{string2}" are anagrams.')
else:
    print(f'"{string1}" and "{string2}" are not anagrams.')

string3 = "Hello"
string4 = "World"
if are_anagrams(string3, string4):
    print(f'"{string3}" and "{string4}" are anagrams.')
else:
    print(f'"{string3}" and "{string4}" are not anagrams.')

# Output:
# "Listen" and "Silent" are anagrams.
# "Hello" and "World" are not anagrams. 