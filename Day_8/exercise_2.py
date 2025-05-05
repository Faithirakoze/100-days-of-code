#!/usr/bin/python3

def calculate_love_score(name1, name2):
    combined_names = (name1 + name2).lower()

    true_count = 0 # Keeps track of the total number of times the letters of TRUE appear in both names
    for letter in "true":
        true_count += combined_names.count(letter) # Adds each count to the running total

    love_count = 0
    for letter in "love":
        love_count += combined_names.count(letter)

    love_score = int(f"{true_count}{love_count}") # Both digits are joined together not added numerically
    print(love_score)


calculate_love_score("Kanye West", "Kim Kardashian")
