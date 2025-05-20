import random

num = list(range(1, 101))
computer_number = random.choice(num)
print(f"Computer guessed a number between 1 and 100.")  # Don't reveal the answer

def num_guess():
    attempts = 10

    while attempts > 0:
        print(f"You have {attempts} attempts remaining to guess the number.")
        try:
            guess_number = int(input("Make a guess: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if guess_number < computer_number:
            print("Too low.\n")
        elif guess_number > computer_number:
            print("Too high.\n")
        else:
            print(f"You got it! The answer was {computer_number}")
            return  # Exit the function if guessed correctly

        attempts -= 1

    print(f"Game over. The correct number was {computer_number}")

num_guess()
