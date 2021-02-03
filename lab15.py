#@author Tobechi Onwenu
# Lab 15. Write a program to draw a face using function statements

import turtle

def draw_mouth(smile):
    if smile == 'yes'or smile == 'YES':
        face.penup()
        #face.setpos(0,0)
        face.goto(-50,100)
        face.pendown()
        #face.right(45)
        face.circle(50,180)
    else:
        if smile == 'no'or smile == 'NO':            
            face.penup()
            face.goto(-50,100)
            face.pendown()
            #face.left(90)
            face.forward(110)
        
def draw_eyes(opened):
    if opened == 'yes'or opened == 'YES':
        face.penup()   
        face.goto(-90,180)
        face.pendown()
        face.circle(30)
        face.penup()   
        face.goto(80,180)
        face.pendown()
        face.circle(30)     
    else:
        if opened == 'no'or opened == 'NO':
            face.penup()   
            face.goto(-90,180)
            face.pendown()
            face.forward(30)
            face.penup()   
            face.goto(80,180)
            face.pendown()
            face.forward(30)
            
def draw_nose(draw):
    if draw == 'yes' or draw == 'YES':
        face.penup()   
        face.goto(0,150)
        face.pendown()
        face.right(90)
        face.forward(30)       

def draw_face(smile,opened,draw):
    face.penup()
    face.goto(0,0)
    face.pendown()
    face.circle(150)
    draw_eyes(opened)
    draw_nose(draw)
    draw_mouth(smile)
    face.hideturtle()
    
def main():
    global face
    print('This program draws a smilley face or a frowny face. \n' +
          "Answer 'yes' or 'no'")
    smile=input('Do you want a smile on the face?: ')
    opened=input('Do you want the eyes open?: ')
    draw=input('Do you want a nose on the face?: ')
    face=turtle.Turtle()
    draw_face(smile,opened,draw)

main()
    
