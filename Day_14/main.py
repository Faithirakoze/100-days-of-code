#!/usr/bin/python3

import random
from game_data import data
from art import logo, vs


def compare_followers():

    score = 0
    game_should_continue = True
    print(logo)
    comparison_2 = random.choice(data)

    while game_should_continue:

        #Making the account at position B to become the next account at position A.
        comparison_1 = comparison_2
        comparison_2 = random.choice(data)

        print(f"Compare A: {comparison_1['name']}, a {comparison_1['description']}, from {comparison_1['country']}.")
        print(vs)
        print(f"Against B: {comparison_2['name']}, a {comparison_2['description']}, from {comparison_2['country']}.")

        #Ask user for a guess
        user_guess = input("Who has more followers? Type 'A' or 'B'?: ")
        if user_guess == "A" and comparison_1['follower_count'] > comparison_2['follower_count']:
            score += 1
            print(f"You're right. Current score: {score}")
        elif user_guess == "B" and comparison_2['follower_count'] > comparison_1['follower_count']:
            score += 1
            print(f"You're right. Current score: {score}")
        else:
            print(f"Sorry, that's wrong. Final score: {score}")
            game_should_continue = False

compare_followers()
