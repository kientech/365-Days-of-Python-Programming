# Coding With Kien - 365 Days of Python Programming
# Advanced - Day 12

# Object-Oriented Programming - Simple Banking System

class Account:
    def __init__(self, account_number, owner_name, balance=0.0):
        self.account_number = account_number
        self.owner_name = owner_name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount:.2f}. New balance: ${self.balance:.2f}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount:.2f}. New balance: ${self.balance:.2f}")
        else:
            print("Withdrawal amount must be positive and not exceed the balance.")

    def get_balance(self):
        return self.balance

    def __str__(self):
        return f"Account [{self.account_number}] - Owner: {self.owner_name}, Balance: ${self.balance:.2f}"


# Example Usage
acc1 = Account("12345", "John Doe", 1000.0)
print(acc1)

acc1.deposit(500.50)
acc1.withdraw(200.0)
acc1.withdraw(2000.0) # This should fail

print("-" * 20)

acc2 = Account("67890", "Jane Smith")
print(acc2)
acc2.deposit(100)
print(f"Final balance for {acc2.owner_name}: ${acc2.get_balance():.2f}")

# Output:
# Account [12345] - Owner: John Doe, Balance: $1000.00
# Deposited $500.50. New balance: $1500.50
# Withdrew $200.00. New balance: $1300.50
# Withdrawal amount must be positive and not exceed the balance.
# --------------------
# Account [67890] - Owner: Jane Smith, Balance: $0.00
# Deposited $100.00. New balance: $100.00
# Final balance for Jane Smith: $100.00 