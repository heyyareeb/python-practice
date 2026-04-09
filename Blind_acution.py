# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}




# TODO-3: Whether if new bids need to be added

# TODO-4: Compare bids in dictionary
import art
print(art.logo)
def highest_bidder(bidding_dict):
    highest_bid = 0
    winner = ""

    max(bidding_dict)

    for bidder in bidding_dict:
        bid_amount = bidding_dict[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder

    print(f"The winner is {winner} with a bid of ${highest_bid}")


bids = {
}
continue_bid= True
while continue_bid:
    name = input("Enter your name: ")
    price = int(input("Enter your bid: "))
    bids[name]= price
    should_bid = input("If there are other user who want to bid: yes/no - \n")
    if should_bid == "no":
        continue_bid= False
        highest_bidder (bids)
    elif should_bid == "yes":
        print("\n"*22)