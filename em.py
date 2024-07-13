import random
def guess_the_number():
    number_to_guess = random.randint(1, 100)
    attempts = 0
    print("Welcome to  Number Guessing Game")
    print("I have selected a number between 1 and 100. Can you guess what it is?")

    while True:
        guess = input("Enter your guess number: ")
        if not guess.isdigit():
            print("Please enter a valid number.")
            continue

        guess = int(guess)
        attempts += 1

        if guess < number_to_guess:
            print("Too low! Try again.")
        elif guess > number_to_guess:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed the number in {attempts} attempts.")
            break


if __name__ == "__main__":
    guess_the_number()
