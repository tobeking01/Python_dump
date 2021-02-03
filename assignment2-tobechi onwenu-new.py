#@author Tobechi Onwenu
#Print a bar chart showing the results of a survey

'''
Steps:
import turtle
draw reference box
calculate percentages
calculate width
draw red,green,blue and orange bars
position numbers and write
done.

'''

width=float(input('Enter the width of the bar chart here: '))
height=float(input('Enter the height of the bar chart here: '))
red=float(input('Enter the number of people who picked red here: '))
green=float(input('Enter the number of people who picked green here: '))
blue=float(input('Enter the number of people who picked blue here: '))
orange=float(input('Enter the number of people who picked orange here: '))


import turtle
my_turtle=turtle.Turtle()
my_turtle.pu()
#set screen size
my_turtle.setpos(-width/2,-height/2)
my_turtle.pd()
my_turtle.color('grey')
my_turtle.fd(width)
my_turtle.lt(90)
my_turtle.fd(height)
my_turtle.lt(90)
my_turtle.fd(width)
my_turtle.lt(90)
my_turtle.fd(height)


#calculate percentage red
########################################total=red+green+blue+orange
red_per=(red/100)*height
green_per=(green/100)*height
blue_per=(blue/100)*height
orange_per=(orange/100)*height
####################################orange_per=(orange/total)*100

#calculate width
#bar_width=.2*width
bar_width=width/5

#draw red bar
my_turtle.begin_fill()
my_turtle.color('red')
my_turtle.backward(red_per)
my_turtle.lt(90)
my_turtle.forward(bar_width)
my_turtle.right(90)
my_turtle.forward(red_per)
my_turtle.end_fill()

#equal space calc
equal_space=(width-(4*bar_width))/3

#cont'd draw green bar
my_turtle.pu()
my_turtle.lt(90)
my_turtle.fd(equal_space)
my_turtle.pd()
my_turtle.begin_fill()
my_turtle.color('green')
my_turtle.lt(90)
my_turtle.fd(green_per)
my_turtle.rt(90)
my_turtle.fd(bar_width)
my_turtle.rt(90)
my_turtle.fd(green_per)
my_turtle.end_fill()


#draw blue bar
my_turtle.pu()
my_turtle.lt(90)
my_turtle.fd(equal_space)
my_turtle.pd()
my_turtle.begin_fill()
my_turtle.color('blue')
my_turtle.lt(90)
my_turtle.fd(blue_per)
my_turtle.rt(90)
my_turtle.fd(bar_width)
my_turtle.rt(90)
my_turtle.fd(blue_per)
my_turtle.end_fill()


#draw orange bar
my_turtle.pu()
my_turtle.lt(90)
my_turtle.fd(equal_space)
my_turtle.pd()
my_turtle.begin_fill()
my_turtle.color('orange')
my_turtle.lt(90)
my_turtle.fd(orange_per)
my_turtle.rt(90)
my_turtle.fd(bar_width)
my_turtle.rt(90)
my_turtle.fd(orange_per)
my_turtle.end_fill()


#writing positon for red
my_turtle.pu()
my_turtle.rt(90)
my_turtle.fd(width)

#calc red writing point
red_writing=red_per+5
green_writing=green_per+5
blue_writing=blue_per+5
orange_writing=orange_per+5

#cont'd
my_turtle.rt(90)
my_turtle.fd(red_writing)
my_turtle.color('red')
my_turtle.write(format(red_per,'.1f',))


#writing position for green
my_turtle.pu()
my_turtle.bk(red_writing)
my_turtle.rt(90)
my_turtle.fd(bar_width+equal_space)
my_turtle.lt(90)
my_turtle.fd(green_writing)
my_turtle.color('green')
my_turtle.write(format(green_per,'.1f',))

#writing position for blue
my_turtle.pu()
my_turtle.bk(green_writing)
my_turtle.rt(90)
my_turtle.fd(bar_width+equal_space)
my_turtle.lt(90)
my_turtle.fd(blue_writing)
my_turtle.color('blue')
my_turtle.write(format(green_per,'.1f',))


#writing for position orange

my_turtle.pu()
my_turtle.bk(blue_writing)
my_turtle.rt(90)
my_turtle.fd(bar_width+equal_space)
my_turtle.lt(90)
my_turtle.fd(orange_writing)
my_turtle.color('orange')
my_turtle.write(format(green_per,'.1f',))

turtle.done()

