import art
print(art.logo)


def find_highest_bidder(bidding_dictionary):
    """
    This function determines the highest bidder from a dictionary of bids.
    """
    winner = ""
    highest_bid = 0

    max(bidding_dictionary)

    for bidder in bidding_dictionary:
        bid_amount = bidding_dictionary[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder

    print(f"The winner is {winner} with a bid of ${highest_bid}")


bids = {}
coninue_bidding = True
while continue_bidding:
    name = input("What is your name?: ")
    price = int(input("What is your bid?: $"))
    bids[name] = price
    should_continue = input("Are there any other bidders? Type 'yes' or 'no'. \n").lower()
    if should_continue == "no":
        should_continue = False
        find_highest_bidder(bids)
    elif should_continue == "yes":
        print("\n" * 20)
