import random

word_list =  ["Apple", "Banana", "Mango", "Strawberry", "Orange"]

secret_word = random.choice(word_list).lower() 
guessed_letter = []

# Task 3.6
def check_guess(guess):
    guess = guess.lower()
    if guess in secret_word:
        print(f"Good guess! '{guess}' is in the word.")
        return True
    else:
        print(f"Sorry, '{guess}' is not in the word. Try again.")
        return False 

def request_letter():
    return input("Please enter a single letter: ")

def validate_guess(guess):
    return len(guess) == 1 and guess.isalpha()

def ask_for_input():
    while True:
        guessed_letter = request_letter()
        if validate_guess(guessed_letter):
            return guessed_letter
        else:
            print("Invalid letter. Please, enter a single alphabetical character.")

# Main game loop
def play_game():
    while True:
        guess = ask_for_input()  # Ask for user input
        if guess in guessed_letter:
            print(f"You've already guessed '{guess}'. Try a different letter.")
        else:
            guessed_letter.append(guess)  # Add the valid guess to guessed letters
            if check_guess(guess):
                if all(letter in guessed_letter for letter in secret_word):  # Check if all letters are guessed
                    print(f"Congratulations! You've guessed the word: {secret_word}")
                    break

if __name__ == "__main__":
    play_game()
    