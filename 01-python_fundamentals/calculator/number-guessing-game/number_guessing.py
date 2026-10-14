import random
import sys

def play():
    random_num = random.randint(1, 100)
    attempts = 0

    while True:
        guess = int(input("Guess the number between 1 and 100: "))

        if guess > 100 or guess < 1:
            print("Number must be between 1 and 100.")
            continue

        elif guess == random_num:
            attempts += 1
            print(f"Correct! You took {attempts} attempts!")
            return
            
        elif guess > random_num:
            print("Too high!")
            attempts += 1
            continue
        
        elif guess < random_num:
            print("Too low")
            attempts += 1
            continue

while True:
    play()

    play_again = input("Play again? (Y / N) ").strip().lower()

    if play_again != "y":
        break
