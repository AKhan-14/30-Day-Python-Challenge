# The Challenge: Create the classic Hangman game. 
# The computer picks a word, and the user guesses letters. 
# The user has a limited number of incorrect guesses.

# Step 1: The Foundation - Setting Up the Game State

"""
import random

max_guesses = 6
word_list = ["python","javascript","developer", "google"]
print(random.choice(word_list))

correct_guesses = set()
incorrect_guesses = set()
"""

# Step 2: The Display - Showing Progress to the User

"""
import random

max_guesses = 7
word_list = ["python","javascript","developer", "google"]
# print(random.choice(word_list))

correct_guesses = set()
incorrect_guesses = set()

secret_word = random.choice(word_list)
display_list = []

for letter in secret_word:
    if letter in correct_guesses:
        correct_guesses.add(letter)
        display_list.append(letter)
    else:
        incorrect_guesses.add(letter)
        display_list.append("_")

display_list = " ".join(display_list)
print(display_list)
"""

# Step 3: The Engine - The Main Game Loop & Input Validation

"""
import random

lives = 7
# word_list = ["python","javascript","developer", "google"]
# print(random.choice(word_list))
correct_guesses = set()
incorrect_guesses = set()
secret_word = "python"

while lives > 0:
    display_list = []
    for letter in secret_word:
        if letter in correct_guesses:
            display_list.append(letter)
        else:
            display_list.append("_")

    print(f"The word so far: {" ".join(display_list)}")
    print(f"Incorrect guesses: {len(incorrect_guesses)}")
    print(f"Lives remaining: {lives}")
    
    while True:
        guess = input("Guess a letter: ").lower().strip()
        if len(guess) != 1:
            print("Invalid input. Please enter exactly one letter.")
        elif not guess.isalpha():
            print("Invalid input. Please enter a letter, not a number or symbol.")
        elif guess in correct_guesses or guess in incorrect_guesses:
            print("You've already guessed that letter. Try a different one.")
        else:
            break
"""

# Step 4: The Logic - Processing a Valid Guess

import random

lives = 7
word_list = ["python","javascript","developer", "google"]
# print(random.choice(word_list))
correct_guesses = set()
incorrect_guesses = set()
secret_word = random.choice(word_list)

while lives > 0 and set(secret_word) != correct_guesses:
    display_list = []
    for letter in secret_word:
        if letter in correct_guesses:
            display_list.append(letter)
        else:
            display_list.append("_")

    print(f"The word so far: {" ".join(display_list)}")
    print(f"Incorrect guesses: {len(incorrect_guesses)}")
    print(f"Lives remaining: {lives}")
    
    while True:
        guess = input("Guess a letter: ").lower().strip()
        if len(guess) != 1:
            print("Invalid input. Please enter exactly one letter.")
        elif not guess.isalpha():
            print("Invalid input. Please enter a letter, not a number or symbol.")
        elif guess in correct_guesses or guess in incorrect_guesses:
            print("You've already guessed that letter. Try a different one.")
        else:
            break

    if guess in secret_word:
        correct_guesses.add(guess)
    elif guess not in secret_word:
        incorrect_guesses.add(guess)
        lives -= 1

    if lives > 0 and set(secret_word) == correct_guesses:
        print("Yh you won shun")
    elif lives == 0:
        print(f"Unlucky buddy, the word was '{secret_word}'")