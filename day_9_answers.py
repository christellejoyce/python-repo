# Exercise 1 - Grading Program

student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}

student_grades = {}

for key in student_scores:
    if student_scores[key] in range (91,101):
        student_grades[key] = "Outstanding"  
    elif student_scores[key] in range (81,91):
        student_grades[key] = "Exceeds Expectations"
    elif student_scores[key] in range (71,81):
        student_grades[key] = "Acceptable"
    elif student_scores[key] <= 70:
        student_grades[key] = "Fail"

print(student_grades)

# Exercise 2 - Dictionary in List

travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]

def add_new_country(country_name, visit_times, cities_name):
    new_country = {}
    new_country["country"] = country_name
    new_country["visits"] = visit_times
    new_country["cities"] = cities_name
    travel_log.append(new_country)

add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)

# Day 9 Project - Silent Auction Program

from replit import clear

logo = (r'''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
''')
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
