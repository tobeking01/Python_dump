#@author Jessica Maistrovich
# A program to draw a snowman
import turtle
from base import draw_base
from midsection import draw_midsection
from right_arm import draw_right_arm
from left_arm import draw_left_arm
from head import draw_head
from hat import draw_hat
from scarf import draw_scarf
from nose import draw_nose

def main():
    franklin = turtle.Turtle()
    x_coord, y_coord, radius = draw_base(franklin)
    x_coord, y_coord, radius = draw_midsection(franklin, x_coord, y_coord, radius)
    draw_right_arm(franklin, x_coord, y_coord, radius)
    draw_left_arm(franklin, x_coord, y_coord, radius)
    x_coord, y_coord, radius = draw_head(franklin, x_coord, y_coord, radius)
    draw_hat(franklin, x_coord, y_coord, radius)
    draw_scarf(franklin, x_coord, y_coord, radius)
    draw_nose(franklin, x_coord, y_coord, radius)





