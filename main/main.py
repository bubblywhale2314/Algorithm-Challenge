import random

def guess_number():
    number_to_guess = random.randint(0, 1000)
    attempts = 0

    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 0 and 1000. Can you guess it?")

    while True:
        user_guess = input("Enter your guess (or 'exit' to quit): ")

        if user_guess.lower() == 'exit':
            print("Goodbye!")
            break

        try:
            user_guess = int(user_guess)
        except ValueError:
            print("Please enter a valid number or 'exit'.")
            continue

        attempts += 1

        if user_guess < number_to_guess:
            print("Too low! Try again.")
        elif user_guess > number_to_guess:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You've guessed the number {number_to_guess} in {attempts} attempts.")
            break

if __name__ == "__main__":
    guess_number()
