#@Author Tobechi Onwenu
#lab 16 program to draw a circle of different colors

import turtle

def main():
    color = int(input('Enter a number between 1 through 6: '))
    group2 = turtle.Turtle()
    draw_item(group2, color)

def draw_item(group2, color):
    group2.pu()
    group2.goto(0,-50)
    group2.pd()
    group2.pensize(10)
    if color == 1:
        group2.color('red')
    elif color == 2:
        group2.color('orange')
    elif color == 3:
        group2.color('yellow')
    elif color == 4:
        group2.color('green')
    elif color == 5:
        group2.color('blue')
    elif color == 6:
        group2.color('purple')
    group2.circle(100)

main()

