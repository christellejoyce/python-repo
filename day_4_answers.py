# Exercise 1 - Heads or Tails

import random 
	 
random01 = random.randint(0,1)
if random01 == 1:
    print('Heads')
else:
    print('Tails')

# Exercise 2 - Banker Roulette

import random

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

n = int(len(names)) - 1
number = int(random.randint(0,n))
print(f'{names[number]} is going to buy the meal.')

# Exercise 3 - Treasure map

row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")

column = int(position[0])
row = int(position[1])
map[row - 1][column - 1] = "X"

print(f"{row1}\n{row2}\n{row3}")


# Day 4 Project - Rock Paper Scissors

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

import random
player = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

choices = [rock, paper, scissors]

if player == 0:
  print(f"You chose:{choices[0]}")
elif player == 1:
  print(f"You chose:{choices[1]}")
elif player == 2:
  print(f"You chose:{choices[2]}")

computer = random.randint(0,2)
print(f"Computer chose:{choices[computer]}")

players = [player, computer]

if player == computer:
  print("It's a draw.")
elif player > computer:
  print("You win.")
  if player == 2 and computer == 0:
    print("You lose.")
else:
  print("You lose.")