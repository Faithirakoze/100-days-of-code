import random

def deal_card():
    """Returns a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    """Take a list of cards and return the score calculated from the cards"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0       # Represents a Blackjack meaning that the player wins

    if 11 in cards and sum(cards) > 21: # Checks if the player has an Ace value of 11 and if their score is over 21, the sum changes. i.e. The Ace has a value of 1 or 11
        cards.remove(11)
        cards.append(1)

    return sum(cards)

user_cards = []
computer_cards = []
is_game_over = False

for _ in range(2): #To add two random values to the user and computer list
    user_cards.append(deal_card())
    computer_cards.append(deal_card())

user_score = calculate_score(user_cards)
computer_score = calculate_score(computer_cards)
print(f"Your cards: {user_cards}, current score: {user_score}")
print(f"Computer's first card: {computer_cards[0]}")

if user_score == 0 or computer_score == 0 or user_score > 21: #if the user or computer has a blackjack or if if the user's score is over 21, the game is over.
    is_game_over = True