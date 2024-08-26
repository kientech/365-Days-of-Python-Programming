# 365 Days of Python Programming
# Author: KienTech

def find_even_numbers(numbers):
    """
    This function takes a list of integers as input and returns a list of all even numbers in the input list.

    Parameters:
    numbers (list): A list of integers.

    Returns:
    list: A list containing all the even numbers from the input list.
    """
    even_numbers = []
    for number in numbers:
        if number % 2 == 0:
            even_numbers.append(number)

    return even_numbers


if __name__ == "__main__":
    numbers_list = [10, 15, 20, 25, 30, 35, 40, 45, 50]
    even_numbers = find_even_numbers(numbers_list)
    print("Even numbers in the list:", even_numbers)
