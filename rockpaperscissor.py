# Rock paper scissor game 

import random

# Function to recieve user choice

def get_user_choice():
    while True:
        user_choice = input("Choose rock, paper, or scissors: ").lower()
        if user_choice in ['rock', 'paper', 'scissors']:
            return user_choice
        else:
            print("Invalid choice. Please choose rock, paper, or scissors.")

# Function for computer choice using random function

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

# Evaluating both choices

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "tie"
    elif (
        (user_choice == 'rock' and computer_choice == 'scissors') or
        (user_choice == 'scissors' and computer_choice == 'paper') or
        (user_choice == 'paper' and computer_choice == 'rock')
    ):
        return "user"
    else:
        return "computer"

# Basic structure

def main():
    user_score = 0
    computer_score = 0

    print("Welcome to Rock-Paper-Scissors Game!")

    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()

        print(f"User's choice: {user_choice}")
        print(f"Computer's choice: {computer_choice}")

        winner = determine_winner(user_choice, computer_choice)

        if winner == "user":
            print("You win!")
            user_score += 1
        elif winner == "computer":
            print("Computer wins!")
            computer_score += 1
        else:
            print("It's a tie!")

        print(f"User's score: {user_score}, Computer's score: {computer_score}")

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()
