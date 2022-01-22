# Exercise 1 - Odd or Even

number = int(input("Which number do you want to check? "))

if int(number) % 2 == 0:
    print(f"{number} is an even number.")
else:
    print(f"{number} is an odd number.")

# Exercise 2 - BMI 2.0

height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

BMI = weight / (height ** 2)

if BMI > 35:
    print(f"Your BMI is {round(BMI)}, you are clinically obese.")
elif BMI > 30:
    print(f"Your BMI is {round(BMI)}, you are obese.")
elif BMI > 25:
    print(f"Your BMI is {round(BMI)}, you are slightly overweight.")
elif BMI > 18.5:
    print(f"Your BMI is {round(BMI)}, you have a normal weight.")
else:
    print(f"Your BMI is {round(BMI)}, you are underweight.")

# Exercise 3 - Leap Year

year = int(input("Which year do you want to check? "))

if year % 4 == 0:
    if year % 100 != 0:
        print("Leap year.")
    elif year % 400 == 0:
        print("Leap year.")
else:
    print("Not leap year.")

# Exercise 4 - Pizza Order Practice

print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

if size == "S":
    bill = int(15)
    if add_pepperoni == "Y":
        bill += 2
elif size == "M":
    bill = int(20)
    if add_pepperoni == "Y":
        bill += 3
elif size == "L":
    bill = int(25)
    if add_pepperoni == "Y":
        bill += 3

if extra_cheese == "Y":
    bill += 1
print(f"Your final bill is: ${bill}.")

# Exercise 5 - Love Calculator

print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

n = name1 + name2
n = n.lower()
true = n.count('t') + n.count('r') + n.count('u') + n.count('e')
love = n.count('l') + n.count('o') + n.count('v') + n.count('e')
score = int(str(true) + str(love))

if score < 10 or score > 90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif score > 40 or score < 50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")

# Day 3 Project - Treasure Hunt

print(r'''

                    |
                    |
                    A
                  _/X\_
                  \/X\/
                   |V|
                   |A|
                   |V|
                  /XXX\
                  |\/\|
                  |/\/|
                  |\/\|
                  |/\/|
                  |\/\|
                  |/\/|
                 IIIIIII
                 |\/_\/|
                /\// \\/\
                |/|   |\|
               /\X/___\X/\
              IIIIIIIIIIIII
             /`-\/XXXXX\/-`\
           /`.-'/\|/I\|/\'-.`\
          /`\-/_.-"` `"-._ \-/\
         /.-'.'           '.'-.\
        /`\-/               \-/`\
     _/`-'/`_               _`\'-`\_
    `"""""""`                `""""""`
''')
print("Welcome to Chasse au Trésor.")
print("Your mission is to find the treasure hidden within the heart of France.") 

#Write your code below this line 👇
cab = input("You have landed at l'Aéroport Charles de Gaulle in Paris. Which cab do you ride to your hotel? Type 'Red' or 'Blue'. \n")
if cab == 'Red' or cab == 'red':
  print("You arrive safely at Hôtel Le Presbytère and drop off all baggage.")
  crossroad = input("Upon exiting, you arrive at a crossroad. Where do you want to go? Type 'Left' or 'Right'.\n")
  if crossroad == 'Left' or crossroad == 'left':
    print("In front of you is la Tour Eiffel.")
    hole = input("Do you dig a hole under the tower now or do you wait until it's dark? Type 'Now' or 'Wait'\n")
    if hole == "Wait" or hole == "wait":
      print("Congratulations! You found and secured the treasure. Well done.")
    else:
      print("You are caught by la police and are arrested. Game over.")
  else:
    print("You are run over by a scooter. Game over.")
else:
  print("You are conned by the taxi driver and forced to hand over all belongings. Game over.")
  