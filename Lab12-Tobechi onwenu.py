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
    draw_box(favorite_color1,red_height,bar_width)
    draw_box(favorite_color2,blue_height,bar_width)
    draw_box(favorite_color3,purple_height,bar_width)
    bar_turtle.lt(90)
    goto_center()
    draw_outline()
def main():
    global chart_height,bar_turtle,chart_width,red_height,blue_height,purple_height,bar_width, favorite_color1,favorite_color2,favorite_color3
    chart_height=float(input('Enter the height of the chart here: '))
    chart_width=float(input('Enter the width of the chart here: '))
    color1_prop=float(input('Enter the first color proportion value between 0 and 1 here: '))
    color2_prop=float(input('Enter the second colors proportion value between 0 and 1here: '))
    color3_prop=float(input('Enter the third colors proportion value between 0 and 1 here: '))
    favorite_color1=input('Please enter your 1st favorite color here: ')
    favorite_color2=input('Please enter your 2nd favorite color here: ')
    favorite_color3=input('Please enter your 3rd favorite color here: ')

    bar_turtle=turtle.Turtle()
    red_height=color1_prop*chart_height
    blue_height=color2_prop*chart_height
    purple_height=color3_prop*chart_height
    bar_width=chart_width/3
    bar_turtle.pu()
    draw_chart()
main()
