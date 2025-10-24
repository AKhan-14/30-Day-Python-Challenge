# The Challenge: The program generates a secret random number between 1 and 100. 
# The user has to guess it. 
# After each guess, the program tells the user if their guess was too high or too low.

# Step 1: The Random Engine

"""

import random
secret_number = random.randint(0,100)
print(f"The secret number is {secret_number}. ")

"""

# Step 2: The Core Game Loop

"""

import random
secret_number = random.randint(0,100)
print(secret_number)

while True:
    while True:
        guess = input("What do you think the number is? ")
        try:
            guess = float(guess)
            break
        except ValueError:
            print("That's not a valid number. Please try again.")
    if guess < secret_number:
        print("Too low, guess again. ")
        continue
    elif guess > secret_number:
        print("Too high, guess again. ")
        continue
    elif guess == secret_number:
        print("Congratulations! You guessed the secret number!")
        break

"""

# Step 3: Refinement and Features

import random

while True:
    difficulty = input("Pick a difficulty, easy or hard? ").lower()
    if difficulty == "easy":
        max_number = 50
        print("The maximum number has been set to 50.")
        break
    elif difficulty == "hard":
        max_number = 1000
        print("The maximum number has been set to 1000.")
        break
    else:
        print("Invalid input. Please type 'easy' or 'hard'.")

secret_number = random.randint(0,max_number)
# print(secret_number)

guess_counter = 0

while True:
    while True:
        guess = input("What do you think the number is? ")
        try:
            guess = int(guess)
            guess_counter = guess_counter + 1
            print(f"You have guessed a total of {guess_counter} times. ")
            break
        except ValueError:
            print("That's not a valid number. Please try again.")
            
    if guess < secret_number:
        print("Too low, guess again. ")
        continue
    elif guess > secret_number:
        print("Too high, guess again. ")
        continue
    elif guess == secret_number:
        print("Congratulations! You guessed the secret number!")
        break
