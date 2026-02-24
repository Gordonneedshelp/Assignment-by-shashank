# Name: Param Jaiswal
# Branch: CSE Data Science Branch
import random

# Number Guessing Game

"""
LOGIC:
1. Uses the 'random' module to pick a secret number between 1 and 100.
2. Sets a limited number of attempts (e.g., 7) for the user.
3. Implements an inner 'while' loop to process guesses and decrement the attempt counter.
4. Compares the user's guess to the secret number and provides 'Too high' or 'Too low' hints.
5. If the correct number is guessed, it breaks the loop; otherwise, it reveals the answer after all attempts are exhausted.
6. Asks the user if they want to play another round to restart the process.
"""

while True:
    number = random.randint(1, 100)
    attempts = 7
    guessed = False

    print("\nGuess the number between 1 and 100")

    while attempts > 0:
        try:
            guess = int(input("Enter guess: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        attempts -= 1

        if guess == number:
            print("Correct! You guessed it.")
            guessed = True
            break
        elif guess > number:
            print("Too high!")
        else:
            print("Too low!")

        print("Attempts left:", attempts)

    if not guessed:
        print("You failed. Number was:", number)

    play_again = input("Play again? (yes/no): ").lower()
    if play_again != "yes":
        print("Thanks for playing!")
        break