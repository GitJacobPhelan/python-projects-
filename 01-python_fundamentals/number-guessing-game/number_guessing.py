"""A number guessing-game where users guess a randomly generated number."""

import random

def play():
    """Run a round of the number-guessing game."""
    random_num = random.randint(1, 100)
    attempts = 0

    while True:
        while True: 
            try:
                guess = int(input("Guess the number between 1 and 100: "))
                break
            except ValueError:
                print("Guess must be a number")  
        if guess > 100 or guess < 1:
            print("Number must be between 1 and 100.")

        elif guess == random_num:
            attempts += 1
            print(f"Correct! You took {attempts} attempts!")
            return
        elif guess > random_num:
            print("Too high!")
            attempts += 1

        elif guess < random_num:
            print("Too low!")
            attempts += 1

playing = True

while playing:
    play()

    while True:
        play_again = input("Play again? (Y / N) ").strip().lower()

        if play_again == "y":
            break
        elif play_again == "n":
            playing = False
            break
        else:
            print("You must enter Y or N")
