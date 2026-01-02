import random

def number_guessing_game():
    """
    A number guessing game
    """
    generate_number = random.randint(1, 100)
    guess = None
    number_of_attempts = 0

    while guess != generate_number:
        try:
            guess_number = input("Enter your guess: ")
            guess = int(guess_number)
            number_of_attempts += 1

            if guess < generate_number:
                print("Too low, try again.\n")
            elif guess > generate_number:
                print("Too high, try again.\n")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a whole number.")

    print(f"You guessed the number {generate_number} correctly in {number_of_attempts} attempts!\n")

number_guessing_game()