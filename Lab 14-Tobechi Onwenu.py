#@author Tobechi Onwenu 
# A Funtion to draw the left arm on a snowman. Group 4.

def draw_left_arm(tobe, x, y, radius):
    tobe.pu()
    tobe.home()
    tobe.goto(x, y)
    tobe.left(25)
    tobe.forward(radius)
    tobe.pd()
    tobe.pensize(radius//8)
    tobe.forward(radius)
    tobe.right(30)
    tobe.forward(radius/3)
    tobe.backward(radius/3)
    tobe.left(60)
    tobe.forward(radius/3)

'''
import turtle

tobe=turtle.Turtle()
x=0
y=0
radius=100

draw_left_arm(tobe,x,y,radius)
'''
