#@author Group 6
# A program to draw a scarf on a snowman

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

def draw_scarf(franklin, x_coord, y_coord, radius):
    franklin.pu()
    franklin.home()
    franklin.goto(x_coord - radius, y_coord - 5 * radius // 4)
    franklin.pd()
    draw_rectangle(franklin, "red", radius // 2, 2 * radius)
    franklin.forward(5 * radius // 4)
    franklin.right(60)
    draw_rectangle(franklin, "red", radius // 2, 2 * radius)
