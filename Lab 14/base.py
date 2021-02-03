#@author Group 1
# A program to draw the base of a snowman

def draw_base(frank):
    radius = int(input("Enter the radius of the base: "))
    x = int(input("Enter the x value of the base of the snowman: "))
    y = int(input("Enter the y value of the base of the snowman: "))
    frank.pu()
    frank.goto(x, y)
    frank.pd()
    frank.circle(radius)
    y = y + radius
    frank.pu()
    frank.goto(x, y + radius / 2)
    frank.dot(radius//10)
    frank.goto(x, y)
    frank.dot(radius//10)
    return (x, y, radius)
