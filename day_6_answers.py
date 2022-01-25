# Exercise 1 - Reeborg's World

# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Alone&url=worlds%2Ftutorial_en%2Falone.json

def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
# draw square
turn_left()
move()
turn_right()
move()
turn_right()
move()
turn_right()
move()

# Exercise 2 - Reeborg's World Hurdle Challenge

# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%202&url=worlds%2Ftutorial_en%2Fhurdle2.json 

def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
   

for i in range(1,7):
    jump()

# While loop - while something_is_true:
  # do something repeatedly
  
# While not - negation of while loop

# For loop - for item in list_of_items:
  # do something repeatedly

# Exercise 3 - Reebog's World Hurdles Challenge with While Loops

# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%203&url=worlds%2Ftutorial_en%2Fhurdle3.json

def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def jump():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
  
while not at_goal():
    if wall_in_front():
        jump()
    else:
      move()

# Exercise 4 - Reebog's World Jumping Over Hurdles with Variable Heights

# http://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%204&url=worlds%2Ftutorial_en%2Fhurdle4.json

def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def jump():
    turn_right()
    move()
    turn_right()
    
while not at_goal():
    if wall_in_front():
        turn_left()
    else:
        move()
    if right_is_clear():
        jump()

# Day 6 Project - Escaping the Maze

# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json

def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def turn_around():
    turn_left()
    turn_left()
    
def jump():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif wall_in_front():
        turn_around()
    else:
        move()