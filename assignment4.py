#@author Tobechi Onwenu
#Hunter and Prey game.

import turtle
import random

def main():
    global prey, hunter
    prey = turtle.Turtle() 
    hunter = turtle.Turtle()
    determine_difficulty()
    draw_fence()
    position_prey()
    screen = hunter.getscreen()
    screen.onclick(move_hunter)

def determine_difficulty():
    global difficulty
    level = input('Please Choose your difficulty '+
                  "'easy', 'medium' or 'hard': ")
    if level == 'easy':
        difficulty = 100
    elif level == 'medium':
        difficulty = 50
    else:
        difficulty = 10

def position_prey():
    prey.ht()
    prey.pu()
    prey.turtlesize(1/2)
    prey.shape('turtle')
    prey_x = random.randint(-250,250)
    prey_y = random.randint(-250,250)
    prey.goto(prey_x,prey_y)

       
def draw_fence():
    hunter.penup()
    hunter.goto(-500/2,-500/2)
    hunter.pendown()
    hunter.forward(500)
    hunter.left(90)
    hunter.forward(500)
    hunter.left(90)
    hunter.forward(500)
    hunter.left(90)
    hunter.forward(500)
    hunter.left(90)


def find_distance(prey,hunter):
    prey_x = prey.xcor()
    prey_y = prey.ycor()
    hunter_x = hunter.xcor()
    hunter_y = hunter.ycor()
    distance = (((prey_x - hunter_x)**2)+((prey_y - hunter_y)**2))**0.5
    return distance


def move_hunter(x,y):
    hunter.pu()  
    hunter.goto(x,y)
    hunter.pendown()
    distance = find_distance(prey,hunter)
    if distance >= 0 and distance <= difficulty:
        hunter.pu()
        hunter.home()
        hunter.pd()
        hunter.write('You Won!', align = "center", font =("Arial", 70, "normal"))
        hunter.hideturtle()
    else:
        move_prey()
        
        
def move_prey():
    hunter_distance = find_distance(prey,hunter)
    if hunter_distance > 100:
        prey.stamp()
    else:
        new_x = random.randint((prey.xcor() - 200),(prey.xcor() + 200) )
        new_y = random.randint((prey.ycor() - 200),(prey.ycor() + 200) )
        if new_x <= -250:
            new_x = -250
        if new_x >= 250:
            new_x = 250
        if new_y <= -250:
            new_y = -250
        if new_y >= 250:
            new_y = 250
        prey.goto(new_x,new_y)
            
main()
