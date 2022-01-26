# Exercise 1 - Paint Area Calculator

import math 

def paint_calc(height, width, cover):
    area = height * width
    num_of_cans = math.ceil(area / cover)
    print(f"You'll need {num_of_cans} cans of paint")


# Exercise 2 - Prime Number Checker

def prime_checker(number):
    isPrime = True
    for i in range(2, number):
        if number % i == 0:
            isPrime = False
    if isPrime:
        print ("It's a prime number.")
    else:
        print ("It's not a prime number.")
        
n = int(input("Check this number: "))
prime_checker(number=n)

# Day 8 Project - Caesar Cipher

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(start_text, shift_amount, cipher_direction):
  end_text = ""
  if cipher_direction == "decode":
    shift_amount *= -1
  for char in start_text:
    if char in alphabet:
      position = alphabet.index(char)
      new_position = position + shift_amount
      end_text += alphabet[new_position]
    else:
      end_text += char

  print(f"Here's the {cipher_direction}d result: {end_text}\n")

from art import logo
print(logo)

another_go = 'Yes'

while another_go == 'Yes':

  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  shift = shift % 26

  caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

  another_go = input("\nWould you like to go again? Type 'Yes' for another go. Type 'No' to exit.\n")
