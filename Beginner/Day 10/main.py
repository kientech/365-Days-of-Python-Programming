# Coding With Kien - 365 Days of Python Programming
# Beginner - Day 10

# Number guessing game

import random

number_to_guess = random.randint(1, 100)
guess = None

print("I'm thinking of a number between 1 and 100.")

while guess != number_to_guess:
    try:
        guess = int(input("Take a guess: "))

        if guess < number_to_guess:
            print("Too low!")
        elif guess > number_to_guess:
            print("Too high!")
        else:
            print(f"You got it! The number was {number_to_guess}")
            
    except ValueError:
        print("Invalid input. Please enter a number.")

# Example Run:
#
# I'm thinking of a number between 1 and 100.
# Take a guess: 50
# Too low!
# Take a guess: 75
# Too high!
# Take a guess: 62
# Too low!
# Take a guess: 68
# You got it! The number was 68 