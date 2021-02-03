#@Author Tobechi Onwenu
#Lab 25 Eight ball machine.

import turtle
import random

def main():
    eight = turtle.Turtle()
    eight.speed(34)
    tell_fortune(eight)

def tell_fortune(ball):
    answers = ['Yes, of course!','Without a doubt, yes.','You can count on it.','For sure!','Ask me later.',"I'm not sure.","I can't tell you right now","I'll tell you after my nap",'No way!',"I don't think so.",'Without a doubt, no.','The answer is clearly NO.']
    def get_response(x,y):
        ball.goto(0,0)
        ball.begin_fill()
        ball.color('black')
        ball.circle(100)
        ball.end_fill()
        ball.goto(10,100)
        ball.color('white')
        ball.write(answers[random.randint(0,11)])
    screen = ball.getscreen()
    screen.onclick(get_response)


main()
    

#Assignment 5 use for list
#I would integrate list method to the below section of my three choice question
# for my game Rock, Paper, Scissors.


'''
def computer_choose():
    global choice
    computer = random.randint(1,3)
    if computer == 1:
        choice = 'rock'
    elif computer == 2:
        choice = 'paper'
    else:
        choice = 'scissors'
'''
