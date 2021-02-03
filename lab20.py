#@ Author Tobechi onwenu
# turtle race

import turtle
import random

def main():
    global blue_turtle, green_turtle
    blue_turtle = turtle.Turtle()
    green_turtle = turtle.Turtle()
    screen = blue_turtle.getscreen()
    screen.onclick(move)
    draw_game()


def draw_game():
    blue_turtle.pu()
    blue_turtle.goto(100,200)
    blue_turtle.right(90)
    blue_turtle.pd()
    blue_turtle.forward(400)
    blue_turtle.pu()
    blue_turtle.goto(-200,100)
    blue_turtle.left(90)
    blue_turtle.shape('turtle')
    blue_turtle.color('blue')
    green_turtle.pu()
    green_turtle.goto(-200,-100)
    green_turtle.shape('turtle')
    green_turtle.color('green')

def move(x,y):
    distance = 100
    while blue_turtle.xcor() <= 100 and green_turtle.xcor() <= 100:
        blue_turtle.forward(random.randint(50,100))
        green_turtle.forward(random.randint(50,100))
    if blue_turtle.xcor() >= 100:
        blue_turtle.write('Winner')
    else:
        if green_turtle.xcor() >= 100:
            green_turtle.write('Winner')
        

    
    

main()    
