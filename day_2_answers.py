# Exercise 1 - Data Types

two_digit_number = input("Type a two digit number: ")

a = two_digit_number[0]
b = two_digit_number[1]
print(int(a)+int(b))

# Exercise 2 - BMI Calculator

height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")

print (round(float(weight) / (float(height) ** 2)))

# Exercise 3 - Life in Weeks

age = input("What is your current age?")

x = (90 - int(age)) * 365
y = (90 - int(age)) * 52
z = (90 - int(age)) * 12

print(f"You have {x} days, {y} weeks, and {z} months left.")

# Day 2 project - Tip Calculator

print("Welcome to the tip calculator!\n")
bill = input("What was the total bill?\n $")
tip_percent = int(input("How much tip (in percentage) would you like to give? 10, 12 or 15?\n")) / 100 + 1 
people = input("How many people to split the bill?\n")

total = round(int(bill) * int(tip_percent) / int(people), 2)

print(f"Each person should pay ${total}.")