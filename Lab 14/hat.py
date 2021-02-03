#@author Group 6
# A program to draw a hat for a snowman

def draw_rectangle(mini, color, height, width):
    mini.color(color)
    mini.begin_fill()
    mini.forward(width)
    mini.left(90)
    mini.forward(height)
    mini.left(90)
    mini.forward(width)
    mini.left(90)
    mini.forward(height)
    mini.left(90)
    mini.end_fill()

def draw_hat(mini, x, y, radius):
    mini.pu()
    mini.home()
    mini.goto(x - radius, y + radius // 2)
    mini.pd()
    draw_rectangle(mini, "black", radius // 2, 2 * radius)
    mini.pu()
    mini.goto(x - 3 * radius // 4, y +  3 * radius // 4)
    mini.pd()
    draw_rectangle(mini, "black", radius, 3 * radius // 2)
    
