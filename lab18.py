#@author Tobechi onwenu
#Turtle game of chance landing on a box.

import turtle
import random

def position_turtle():
    up_turtle.pu()
    up_turtle.speed(8)
    up_turtle.goto(0,-400/2)
    up_turtle.pd()
    up_turtle.fd(100)
    up_turtle.left(90)
    up_turtle.fd(400)
    up_turtle.left(90)
    up_turtle.fd(100)
    up_turtle.left(90)
    up_turtle.fd(400)
    up_turtle.left(90)

    up_turtle.pu()
    up_turtle.shape('turtle')
    up_turtle.color('blue')
    up_turtle.goto(-200,100)
    up_turtle.pd()

    down_turtle.pu()
    down_turtle.speed(8)
    down_turtle.shape('turtle')
    down_turtle.color('green')
    down_turtle.goto(-200,-100)
    down_turtle.pd()
    
def move_turtle(x,y):
    up_turtle.pu()
    down_turtle.pu()
    up_move = random.randint(100,300)
    down_move = random.randint(100,300)
    up_turtle.forward(up_move)
    down_turtle.forward(down_move)
    up_turtle.pendown()
    down_turtle.pendown()
    if up_move >= 200 and down_move >= 200:
        up_turtle.write('Tie')
        down_turtle.write('Tie')
    elif up_move >= 200 and down_move !=200:
        up_turtle.write('Winner')
        down_turtle.write('Bummer')
    elif up_move != 200 and down_move >=200:
        up_turtle.write('Bummer')
        down_turtle.write('Winner')
    else:
        up_turtle.write('Bummer')
        down_turtle.write('Bummer')        
        

def main():
    global up_turtle, down_turtle
    up_turtle=turtle.Turtle()
    down_turtle=turtle.Turtle()
    position_turtle()
    screen = up_turtle.getscreen()
    screen = down_turtle.getscreen()
    screen.onclick(move_turtle)
    
main()


