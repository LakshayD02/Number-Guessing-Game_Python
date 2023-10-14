import random

random_number = random.randint(1, 50)
attempts = 0

print("Number Guessing Game!")
print("I've selected a random number between 1 and 50.")

while True:
    try:
        user_guess = int(input("Enter your guess: "))
        attempts += 1

        if user_guess < 1 or user_guess > 50:
            print("Please enter a valid number between 1 and 50.")
        elif user_guess < random_number:
            print("Too low! Try again.")
        elif user_guess > random_number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You've guessed the number {random_number} in {attempts} attempts.")
            break
    except ValueError:
        print("Invalid input. Please enter a valid number.")

