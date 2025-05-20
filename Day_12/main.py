import random

num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]
computer_number = random.choice(num)
print(f"Computer guessed: {computer_number}")

def num_guess():
    right_guess = False
    attempts = 10

    while not right_guess:
        print(f"You have {attempts} attempts remaining to guess the number")
        guess_number = int(input("Make a guess: "))
        attempts -= 1

        if guess_number < computer_number:
            print("Too low.\nGuess again.\n")
            print(f"You have {attempts} attempts remaining to guess the number")
            num_guess()
        elif guess_number > computer_number:
            print("Too high.\nGuess again")
            print(f"You have {attempts} attempts remaining to guess the number")
            num_guess()
        else:
            print(f"You got it! The answer was {computer_number}")
            right_guess = True

num_guess()
