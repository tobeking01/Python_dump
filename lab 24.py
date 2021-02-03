#@author Tobechi Onwenu
#Lab 24

import turtle

def main():
    square = turtle.Turtle()
    square.hideturtle()
    square.speed(9)
    create_design(square)

def create_design(draw):
    for square in range (5,156,3):
        for side in range (4):
            draw.forward(square)
            draw.left(90)
main()    


#Game name: Rock, paper, scissors game.
