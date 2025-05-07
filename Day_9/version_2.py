import art
print(art.logo)

bid_log = {}

bidding = True

while bidding:
    name = input("What is your name? ")
    bid_price = int(input("What is your bid price? $"))
    bid_log[name] = bid_price

    other_bidders = input("Are there any other bidders? Type 'yes' or 'no'. \n").lower()
    if other_bidders == "no":
        bidding = False

# Find the highest bidder
highest_bidder = max(bid_log, key=bid_log.get)
highest_bid = bid_log[highest_bidder]

print(f"The winner is {highest_bidder} with a bid of ${highest_bid}.")

