# 365 Days of Python Programming
# Author: KienTech

def generate_multiplication_table():
    """
    This function generates and prints the multiplication table from 1 to 10.
    """
    print("Multiplication Table (1 to 10)\n")

    # Print the top row (1 to 10)
    print("    ", end="")
    for i in range(1, 11):
        print(f"{i:4}", end="")
    print("\n" + "-" * 45)

    # Generate the table
    for i in range(1, 11):
        print(f"{i:2} |", end="")  # Row label with separator
        for j in range(1, 11):
            print(f"{i * j:4}", end="")  # Product of i and j
        print()  # Newline after each row


if __name__ == "__main__":
    generate_multiplication_table()
