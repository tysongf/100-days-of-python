import os
import gavel


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


clear()

print(gavel)
print("Welcome to the Blind Auction System!")

bids = {}
more_bidders = "y"
while more_bidders == "y":
    clear()
    print(gavel.logo)
    name = input("Bidder name: ")
    bid = int(input("Bid $: "))
    bids[name] = bid
    more_bidders = input("More Bidders? y / n: ")

highest_bid = {"amt": 0}
for b in bids:
    if bids[b] > highest_bid["amt"]:
        highest_bid = {"name": b, "amt": bids[b]}

clear()
print(gavel.logo)
print("And the winner is...")
print(f"{highest_bid['name']} with a bid of ${highest_bid['amt']:.2f}\n")
