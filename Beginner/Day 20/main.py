# Coding With Kien - 365 Days of Python Programming
# Beginner - Day 20

# Reverse a list without using the .reverse() method

def reverse_list(items):
    """
    Reverses a list using slicing.
    """
    return items[::-1]

# Example
my_list = [1, 2, 3, 4, 5]
reversed_list = reverse_list(my_list)

print(f"Original list: {my_list}")
print(f"Reversed list: {reversed_list}")

# --- Alternative using a loop ---
def reverse_list_loop(items):
    new_list = []
    for i in range(len(items) - 1, -1, -1):
        new_list.append(items[i])
    return new_list

reversed_list_loop_version = reverse_list_loop(my_list)
print(f"Reversed list (loop version): {reversed_list_loop_version}")


# Output:
# Original list: [1, 2, 3, 4, 5]
# Reversed list: [5, 4, 3, 2, 1]
# Reversed list (loop version): [5, 4, 3, 2, 1] 