#@author Tobechi Onwenu
#A bar chart of proportioned red,blue and purple values.
import turtle
        
def goto_center():
    bar_turtle.pu()
    bar_turtle.goto(-chart_width/2,-chart_height/2)
    bar_turtle.pd()
def draw_outline():
    bar_turtle.color('black')
    bar_turtle.forward(chart_width)
    bar_turtle.lt(90)
    bar_turtle.fd(chart_height)
    bar_turtle.lt(90)
    bar_turtle.fd(chart_width)
    bar_turtle.lt(90)
    bar_turtle.fd(chart_height)
def draw_box(color,height,width):
    bar_turtle.color(color)
    bar_turtle.begin_fill()
    bar_turtle.bk(height)
    bar_turtle.lt(90)
    bar_turtle.fd(width)
    bar_turtle.rt(90)
    bar_turtle.fd(height)
    bar_turtle.end_fill()
def draw_chart():
    goto_center()
    draw_outline()
    draw_box('red',red_height,bar_width)
    draw_box('blue',blue_height,bar_width)
    draw_box('purple',purple_height,bar_width)
    bar_turtle.lt(90)
    goto_center()
    draw_outline()
def main():
    global chart_height,bar_turtle,chart_width,red_height,blue_height,purple_height,bar_width
    chart_height=float(input('Enter the height of the chart here: '))
    chart_width=float(input('Enter the width of the chart here: '))
    red_prop=float(input('Enter the red proportion value between 0 and 1 here: '))
    blue_prop=float(input('Enter the blue proportion value between 0 and 1here: '))
    purple_prop=float(input('Enter the purple proportion value between 0 and 1 here: '))
    bar_turtle=turtle.Turtle()
    red_height=red_prop*chart_height
    blue_height=blue_prop*chart_height
    purple_height=purple_prop*chart_height
    bar_width=chart_width/3
    bar_turtle.pu()
    draw_chart()
main()
