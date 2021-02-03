
import turtle
import random
def move(x,y):
    turtle.pu()
    turtle.goto(x,y)
    turtle.write(str(x)+','+ str(y))
    turtle.stamp()

screen=turtle.getscreen()
screen.onclick(move)
