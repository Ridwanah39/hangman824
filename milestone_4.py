# Task 4.2
import random

class Hangman:
    def __init__(self, word_list, num_lives=5):
        self.word = random.choice(word_list).lower()
        self.word_guessed = ['_'] * len(self.word)
        self.num_letters = len(set(self.word))
        self.num_lives = num_lives        
        self.word_list = word_list        
        self.word_list = word_list        
        self.list_of_guesses = []

    def check_guess(self, guess):
        guess = guess.lower()
        if guess in self.word:
            print(f"Good guess! '{guess}' is in the word")
            for idx, letter in enumerate(self.word):
                if letter == guess:
                    self.word_guessed[idx] = guess
            self.num_letters -= 1 
        else:
            self.num_lives -= 1
            print(f"Sorry, '{guess}' is not in the word. Try again.") 
            print(f"Lives remaining: {self.num_lives}")

    def ask_for_input(self):
        while True:
            guess = input("Please enter a single letter:").lower()
            if len(guess) != 1 or not guess.isalpha():
                print("Invalid letter. Please try again")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)
                break 

if __name__ == "__main__":
    word_list = ["Apple", "Banana", "Mango", "Strawberry", "Orange"]
    game = Hangman(word_list)

    while game.num_letters > 0 and game.num_lives > 0:
        print(f"Word to guess: {' '.join(game.word_guessed)}")
        game.ask_for_input()

    if game.num_lives == 0:
        print(f"Game over! The word was '{game.word}'.")
    else:
        print(f"Congratulations! You've guessed the word '{game.word}'.")
