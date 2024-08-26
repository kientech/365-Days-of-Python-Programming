# 365 Days of Python Programming
# Author: KienTech


def reverse_string(input_string):
    """
    This function takes a string as input and returns the string reversed.

    Parameters:
    input_string (str): The string to be reversed.

    Returns:
    str: The reversed string.
    """
    # Reverse the string using slicing
    reversed_string = input_string[::-1]

    return reversed_string


if __name__ == "__main__":
    original_string = "Hello, World!"
    reversed_string = reverse_string(original_string)
    print("Original string:", original_string)
    print("Reversed string:", reversed_string)
