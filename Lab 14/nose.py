#@author Group 8
# A program to draw a nose on a snowman

def draw_nose(franklin, x_coord, y_coord, radius):
    franklin.pu()
    franklin.home()
    franklin.goto(x_coord + radius// 2, y_coord - radius // 3)
    franklin.color("orange")
    franklin.shape("triangle")
    franklin.shapesize(radius/80, radius/10)
