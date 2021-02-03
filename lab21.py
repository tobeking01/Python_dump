#@ Author Tobechi onwenu
# lab 21 assignment

import turtle

def main():
    rar = turtle.Turtle()
    draw_circle(rar)
    rar.pu()
    rar.goto(200,0)
    rar.pd()
    rar.color('red')
    draw_vortex(rar)

def draw_circle(hey):
    for all in ('red', 'orange', 'green', 'black', 'yellow', 'blue'):
        hey.color(all)
        hey.circle(60)
        hey.left(25)
    
def draw_vortex(jack):
    lines = int(input("Enter the number of circles to be drawn here: "))
    for x in range (lines,(lines*10),10):
        jack.circle(x)
        

main()
