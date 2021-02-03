#@author Tobechi Onwenu 
# A program to draw the left arm on a snowman


import turtle

tobe=turtle.Turtle()
x=0
y=0
radius=100
def draw_left_arm(tobe,x, y, radius):
    tobe.pu()
    tobe.home()
    tobe.goto(x, y)
    tobe.left(160)
    tobe.forward(radius)
    tobe.pd()
    tobe.forward(radius/2)
    tobe.right(70)
    tobe.forward(radius/2)
    tobe.right(20)
    tobe.forward(radius/3)
    tobe.backward(radius/3)
    tobe.left(60)
    tobe.forward(radius/3)
    
draw_left_arm(tobe,x,y,radius)

