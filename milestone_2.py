# Task 2
import random 

# Task 1
word_list = ["Apple", "Banana", "Mango", "Strawberry", "Orange"]

# Task 2
word = random.choice(word_list)

# Task 3: Ask the user for a single letter input
guess = input("Please enter a single letter: ")

# Task 4: Validate the user's input
if len(guess) == 1 and guess.isalpha():
    print("Good guess!")
else:
    print("Oops! That is not a valid input.")


