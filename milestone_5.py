import random

class Hangman:
    def __init__(self, word_list, num_lives=5):
        self.word = random.choice(word_list).lower()
        self.word_guessed = ['_'] * len(self.word)
        self.num_letters = len(set(self.word))  # Unique letters in the word
        self.num_lives = num_lives
        self.list_of_guesses = []

    def _update_word_guessed(self, guess):
        for idx, letter in enumerate(self.word):
            if letter == guess:
                self.word_guessed[idx] = guess

    def check_guess(self, guess):
        guess = guess.lower()
        if guess in self.word:
            print(f"Good guess! '{guess}' is in the word.")
            self._update_word_guessed(guess)
            self.num_letters -= 1
        else:
            self.num_lives -= 1
            print(f"Sorry, '{guess}' is not in the word. Try again.")
            print(f"Lives remaining: {self.num_lives}")

    def _validate_guess(self, guess):
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid letter. Please enter a single alphabetical character.")
            return False
        if guess in self.list_of_guesses:
            print("You already tried that letter!")
            return False
        return True

    def ask_for_input(self):
        while True:
            guess = input("Please enter a single letter: ").lower()
            if self._validate_guess(guess):
                self.check_guess(guess)
                self.list_of_guesses.append(guess)
                break


# Task 5.1
def play_game(word_list):
    num_lives = 5
    game = Hangman(word_list, num_lives)

    # Start the game loop
    while True:
        if game.num_lives == 0:
            print(f"You lost! The word was '{game.word}'.")
            break
        elif game.num_letters > 0:
            print(f"Word to guess: {' '.join(game.word_guessed)}")
            game.ask_for_input()
        else:
            print(f"Congratulations! You've won the game! The word was '{game.word}'.")
            break

# Step 2: Call the play_game function to start the game
if __name__ == "__main__":
    word_list = ["apple", "banana", "mango", "strawberry", "orange"]
    play_game(word_list)
