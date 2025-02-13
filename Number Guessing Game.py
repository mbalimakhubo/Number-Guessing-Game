#This is a Number Guessing Game

import random

def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    print("I have picked a random number between 1 and 100. Can you guess it?")
    
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    attempts = 0
    guessed_correctly = False
    
    while not guessed_correctly:
        try:
            # Get the user's guess
            guess = int(input("Enter your guess: "))
            attempts += 1
            
            # Check the user's guess
            if guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You've guessed the number {secret_number} correctly in {attempts} attempts!")
                guessed_correctly = True
        except ValueError:
            print("Invalid input! Please enter a valid number.")
    
    print("Thanks for playing!")

# Run the game
if __name__ == "__main__":
    number_guessing_game()
