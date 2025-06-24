# Coding With Kien - 365 Days of Python Programming
# Intermediate - Day 09

# Directory Tree Lister
import os

def list_directory_tree(startpath):
    for root, dirs, files in os.walk(startpath):
        level = root.replace(startpath, '').count(os.sep)
        indent = ' ' * 4 * (level)
        print(f'{indent}{os.path.basename(root)}/')
        subindent = ' ' * 4 * (level + 1)
        for f in files:
            print(f'{subindent}{f}')

# Start from the parent directory of the script's location
# to give a more interesting tree.
start_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
print(f"Directory tree for: {start_path}\n")
list_directory_tree(start_path)

# Example output will depend on the directory structure where this script is run.
# It will look something like this:
#
# Intermediate/
#     Day 01/
#         main.py
#     Day 02/
#         main.py
#     ... 