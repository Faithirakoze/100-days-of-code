import random
from art import logo

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

def compare(u_score, c_score):
    if u_score == c_score:
        return "Draw"
    elif c_score == 0:
        return "Lose, opponent has a Blackjack"
    elif u_score == 0:
        return "Win with a Blackjack"
    elif u_score > 21:
        return "You went over. You lose"
    elif c_score > 21:
        return "Opponent went over. You win"
    elif u_score > c_score:
        return "You win"
    else:
        return "You lose"

def play_game():
    print(logo)
    user_cards = []
    computer_cards = []
    computer_score = -1
    user_score = -1
    is_game_over = False

    for _ in range(2): #To add two random values to the user and computer list
        user_cards.append(deal_card())#call the function deal_card()
        computer_cards.append(deal_card())

    while not is_game_over: #the score will need to be rechecked and recalculated with with every new card until the game ends.
        user_score = calculate_score(user_cards)#call the function calculate_score()
        computer_score = calculate_score(computer_cards)
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21: #if the user or computer has a blackjack or if if the user's score is over 21, the game is over.
            is_game_over = True
        else: #if the game has not ended and the user wants to draw another card or else end the game.
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17: #The computer gets to draw another card
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))

    while input("Do you want to play a game of Blackjack? Type 'y' or 'no': ") == "y":
        print("\n" * 20)
        play_game()

play_game()