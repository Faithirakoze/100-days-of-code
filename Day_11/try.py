import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

blackjack = True
while blackjack:

    your_cards = random.choices(cards, k=2)
    print(f"Current score: {your_cards[0] + your_cards[1]}")
    computer = random.choices(cards, k=2)

    print(f"Computer's first card: {computer[0]}")

    print(input("Type 'y' to get another card, type 'n' to pass: "))
    print(f"Your cards:{your_cards.append(random.choice(cards))}, current score: {sum(your_cards)}")
