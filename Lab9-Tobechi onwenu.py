#@author Tobechi Onwenu
#A bar chart of proportioned red,blue and purple values.


chart_height=float(input('Enter the height of the chart here: '))
chart_width=float(input('Enter the width of the chart here: '))
red_prop=float(input('Enter the red proportion value between 0 and 1 here: '))
blue_prop=float(input('Enter the blue proportion value between 0 and 1here: '))
purple_prop=float(input('Enter the purple proportion value between 0 and 1 here: '))
import turtle
bar_turtle=turtle.Turtle()
red_height=red_prop*chart_height
blue_height=blue_prop*chart_height
purple_height=purple_prop*chart_height
bar_width=chart_width/3
def goto_center():
    bar_turtle.pu()
    bar_turtle.goto(-chart_width/2,-chart_height/2)
    bar_turtle.pd()
def draw_outline():
    bar_turtle.pensize(3)
    bar_turtle.color('black')
    bar_turtle.forward(chart_width)
    bar_turtle.lt(90)
    bar_turtle.fd(chart_height)
    bar_turtle.lt(90)
    bar_turtle.fd(chart_width)
    bar_turtle.lt(90)
    bar_turtle.fd(chart_height)
def draw_red_box():
    bar_turtle.pensize(0)
    bar_turtle.color('red')
    bar_turtle.begin_fill()
    bar_turtle.bk(red_height)
    bar_turtle.lt(90)
    bar_turtle.fd(bar_width)
    bar_turtle.rt(90)
    bar_turtle.fd(red_height)
    bar_turtle.end_fill()
def draw_blue_box():
    bar_turtle.pensize(0)
    bar_turtle.color('blue')
    bar_turtle.begin_fill()
    bar_turtle.bk(blue_height)
    bar_turtle.lt(90)
    bar_turtle.fd(bar_width)
    bar_turtle.rt(90)
    bar_turtle.fd(blue_height)
    bar_turtle.end_fill()
def draw_purple_box():
    bar_turtle.pensize(0)
    bar_turtle.color('purple')
    bar_turtle.begin_fill()
    bar_turtle.bk(purple_height)
    bar_turtle.lt(90)
    bar_turtle.fd(bar_width)
    bar_turtle.rt(90)
    bar_turtle.fd(purple_height)
    bar_turtle.end_fill()
    #bar_turtle.hideturtle()
    turtle.done()
def draw_chart():
    goto_center()
    draw_outline()
    draw_red_box()
    draw_blue_box()
    draw_purple_box()
    goto_center()
    draw_outline()
draw_chart()
