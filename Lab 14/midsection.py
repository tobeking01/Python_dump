#@author Group 2
# A program to draw the midsection of a snowman

def draw_midsection(ben, x, y, radius):
    ben.pu()
    dot_size = radius // 10
    y = y + radius
    ben.goto(x, y)
    ben.pd()
    radius = 2 * radius // 3
    ben.circle(radius)
    y = y + radius
    ben.pu()
    ben.goto(x, y - radius // 3)
    ben.dot(dot_size)
    ben.goto(x, y + radius // 3)
    ben.dot(dot_size)
    return x, y, radius
