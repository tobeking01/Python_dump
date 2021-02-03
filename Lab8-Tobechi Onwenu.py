#@author Tobechi onwenu
#Draw a solid rectangle in python

'''

Question:
Read in a height, width, and color and use
those values to draw a solid rectangle
in Python.

Plan:
-get the inputs for height, width and color named: height,width and color_fill
-open idle in python
-import turtle into the idle
-rename turtle to personal variable named: my_turtle
-write the code to draw a filled rectangle using the variables
-run the program using f5.

'''


height=float(input('Enter the height of the rectangle here: '))
width=float(input('Enter the width of the rectangle here: '))
fill_color=input('Enter the color of the rectangle here: ')
import turtle
my_turtle=turtle.Turtle()

my_turtle.pu()
my_turtle.setpos(-300,200)
my_turtle.color(fill_color)
my_turtle.pd()
my_turtle.begin_fill()
my_turtle.fd(width)
my_turtle.rt(90)
my_turtle.fd(height)
my_turtle.rt(90)
my_turtle.fd(width)
my_turtle.rt(90)
my_turtle.fd(height)
my_turtle.end_fill()
my_turtle.pu()
turtle.done()
