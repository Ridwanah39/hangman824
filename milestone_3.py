# Task 2
import random

word_list =  ["Apple", "Banana", "Mango", "Strawberry", "Orange"]

secret_word = random.choice(word_list)

# Task 3.3
def check_guess(guess):
    guess = guess.lower()
    if guess in secret_word:
        print(f"Good guess! '{guess}' is in the word.")
    else:
        print(f"Sorry, '{guess}' is not in the word. Try again.")

def ask_for_input():
    while True:
        guess = input("Please enter a single letter: ")
        
        if len(guess) == 1 and guess.isalpha():
           check_guess(guess)
           break 
        else:
            print("Invalid letter. Please, enter a single alphabetical character.")

ask_for_input() 