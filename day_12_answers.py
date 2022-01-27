#Number Guessing Game Objectives:

import random

logo = (r"""
  _____                   __  __         _  __           __           __
 / ___/_ _____ ___ ___   / /_/ /  ___   / |/ /_ ____ _  / /  ___ ____/ /
/ (_ / // / -_|_-<(_-<  / __/ _ \/ -_) /    / // /  ' \/ _ \/ -_) __/_/ 
\___/\_,_/\__/___/___/  \__/_//_/\__/ /_/|_/\_,_/_/_/_/_.__/\__/_/ (_)  
""")
print(logo)
answer = random.randint(1,101)

def play_easy():
  
  isGameOver = False
  lives = 9
  guess = int(input("Guess a number between 1 and 100: "))
 
  while not isGameOver:
    if guess != answer:
      if guess > answer:
        print("Too high.")
      elif guess < answer:
        print("Too low.")
      lives -= 1
      guess = int(input("Guess a number between 1 and 100: "))
    elif guess == answer:
      print(f"You got it! The answer is {answer}.")

    if lives == 0:
      isGameOver = True
      print("You've run out of guesses, you lose.")

def play_hard():
  
  isGameOver = False
  lives = 4
  guess = int(input("Guess a number between 1 and 100: "))
 
  while not isGameOver:
    if guess != answer:
      if guess > answer:
        print("Too high.")
      elif guess < answer:
        print("Too low.")
      lives -= 1
      guess = int(input("Guess a number between 1 and 100: "))
    elif guess == answer:
      print(f"You got it! The answer is {answer}.")

    if lives == 0:
      isGameOver = True
      print("You've run out of guesses, you lose.")
level = input("Welcome to the Number Guessing Game! I'm thinking of a number between 1 and 100.\nChoose a difficulty. Type 'easy' or 'hard: ")

if level == 'easy':
  play_easy()
elif level == 'hard':
  play_hard()


