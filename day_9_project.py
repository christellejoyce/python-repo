from replit import clear
from art import logo

print(logo)

auction_dict = {}

bidding_finished = False

while not bidding_finished:
  name = input("What is your name?\n")
  bid = int(input("How much is your bid?\n$"))
  auction_dict[name] = bid
  should_continue = input("Are there others who want to bid? 'yes' or 'no'\n")

  def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ''
    for bidder in bidding_record:
      bid_amount = bidding_record[bidder]
      if bid_amount > highest_bid:
        highest_bid = bid_amount
        winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")
  
  if should_continue == "no":
    bidding_finished = True
    find_highest_bidder(auction_dict)
  elif should_continue == "yes":
    clear()