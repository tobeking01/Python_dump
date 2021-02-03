#@Author Tobechi Onwenu
#Lab 13- use mouse to write two random x and y coordinates with mouse.

import turtle
import random

def move(x,y):
    skyline.pu()
    new_x,new_y=jumble_numbers(x,y)
    skyline.goto(new_x,new_y)
    skyline.write('('+str(new_x)+','+str(new_y)+')')
    skyline.goto(x,y)
    skyline.write('('+str(x)+','+str(y)+')')

def start_over(x,y):
    screen.resetscreen()

def jumble_numbers(x,y):
    scramble_x=x+random.randint(-100,100)
    scramble_y=y+random.randint(-100,100)
    return scramble_x,scramble_y
    
def main():
    global skyline
    skyline=turtle.Turtle()
    screen=skyline.getscreen()
    screen.bgcolor('yellow')
    screen.onclick(move)
    screen.onclick(start_over,3)   
main()
