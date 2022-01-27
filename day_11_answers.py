############### Blackjack Project #####################

import random
from replit import clear
logo = (r"""
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
""")

def play_blackjack():
  print(logo)

  game_end = False

  # Deal cards
  def deal_cards():
    ''' Returns a random card.'''
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

  user_cards = []
  dealer_cards = []
  players = [user_cards, dealer_cards]

  for player in players:
    for i in range(2):
      player.append(deal_cards())

  # Calculate score
  def calculate_score(l1):
    ''' Calculates the sum of the scores in the list.'''
    if sum(l1) == 21 and len(l1) == 2:
      return 0
    elif 11 in l1 and sum(l1) > 21:
      place11 = l1.index(11)
      l1[place11] = 1
    return sum(l1)

  while not game_end:

    user_score = calculate_score(user_cards)
    dealer_score = calculate_score(dealer_cards)

    print(f"Your cards: {user_cards}, current score: {user_score}")
    print(f"Dealer's cards: {dealer_cards}, current score: {dealer_score}")

    if user_score == 0 or dealer_score == 0 or user_score > 21:
      game_end = True
    else:
      draw_another = input("Draw another card? 'yes' or 'no':\n")
      if draw_another == 'yes':
        user_cards.append(deal_cards())
      else:
        game_end = True

    while dealer_score != 0 and dealer_score < 17:
      dealer_cards.append(deal_cards())
      dealer_score = calculate_score(dealer_cards)

    def compare(user_score, dealer_score):
      if user_score == dealer_score:
        print("Push. It's a draw.")
      elif dealer_score == 0:
        print('Dealer wins with Blackjack. You lose. 😔')
      elif user_score == 0:
        print("You win with Blackjack. 🥳")
      elif user_score > 21:
        print("Bust! You lose. 😔")
      elif dealer_score > 21:
        print("Dealer's bust! You win. 🥳")
      else:
        if user_score > dealer_score:
          print("You win. 🥳")
        elif user_score < dealer_score:
          print("You lose. 😔")

    if game_end:
      compare(user_score,dealer_score)
      if input("Do you want to play Blackjack again? 'yes' or 'no':\n") == 'yes':
        clear()
        play_blackjack()
        
play_blackjack()
