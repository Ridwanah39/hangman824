import random 

def get_random_fruit(fruit_list):
    return random.choice(fruit_list)

def validate_input(user_input):
    if len(user_input) == 1 and user_input.isalpha():
        return True
    return False

def main():
    # List of favorite fruits
    fruit_list = ["Apple", "Banana", "Mango", "Strawberry", "Orange"]
    
    # Get a random fruit from the list
    random_fruit = get_random_fruit(fruit_list)
    print(f"Randomly selected fruit: {random_fruit}")  # Optional: Display the selected fruit for testing

    # Ask the user for a single letter input
    guess = input("Please enter a single letter: ")

    # Validate the user's input
    if validate_input(guess):
        print("Good guess!")
    else:
        print("Oops! That is not a valid input.")

# Entry point for the script
if __name__ == "__main__":
    main()