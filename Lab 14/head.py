#@author Group 5
# A program to draw the head and face of a snowman

def draw_head(mini, x, y, radius):
    mini.pu()
    mini.pensize(1)
    mini.home()
    y = y + radius
    mini.goto(x, y)
    radius = 2 * radius // 3
    mini.pd()
    mini.circle(radius)
    y = y + radius
    mini.pu()
    mini.goto(x, y)
    mini.forward(radius // 3)
    mini.dot(radius // 4)
    mini.backward(2 * radius // 3)
    mini.dot(radius // 4)
    return(x, y, radius)
    
