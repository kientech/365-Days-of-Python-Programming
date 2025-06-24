# Coding With Kien - 365 Days of Python Programming
# Intermediate - Day 07

# Rock, Paper, Scissors Game
import random

def play_game():
    choices = ["rock", "paper", "scissors"]
    computer_choice = random.choice(choices)
    
    user_choice = input("Enter your choice (rock, paper, scissors): ").lower()
    
    if user_choice not in choices:
        print("Invalid choice!")
        return

    print(f"Your choice: {user_choice}")
    print(f"Computer's choice: {computer_choice}")

    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        print("You win!")
    else:
        print("You lose!")

play_game()

# Example Run:
# Enter your choice (rock, paper, scissors): rock
# Your choice: rock
# Computer's choice: scissors
# You win! 