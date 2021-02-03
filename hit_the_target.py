import turtle

#named constants

SCREEN_WIDTH=600            #screen size
SCREEN_HEIGHT=600           #shcreen height
TARGET_LLEFT_X=100          #target_lower-left x
TARGET_LLEFT_Y=250          #target_lower_left y
TARGET_WIDTH=25             #width of the target
FORCE_FACTOR=30             #arbituary force factor
PROJECTILE_SPEED=1          #projectiles animation speed
NORTH=90                    #angle of north direction
SOUTH=270                   #angle of south direction
EAST=0                      #angle of east direction
WEST=180                    #angle of west direction

#setuo the window
turtle.setup(SCREEN_WIDTH, SCREEN_HEIGHT)

#draw the target
turtle.hideturtle()
turtle.speed(0)
turtle.penup()
turtle.goto(TARGET_LLEFT_X, TARGET_LLEFT_Y)
turtle.pendown()
turtle.setheading(EAST)
turtle.forward(TARGET_WIDTH)
turtle.setheading(NORTH)
turtle.forward(TARGET_WIDTH)
turtle.setheading(WEST)
turtle.forward(TARGET_WIDTH)
turtle.setheading(SOUTH)
turtle.forward(TARGET_WIDTH)
turtle.penup()

#center the turtle
turtle.goto(0,0)
turtle.setheading(EAST)
turtle.showturtle()
turtle.speed(PROJECTILE_SPEED)

#GET THE ANGLE AND FORCE FROM THE USER
angle=float(input('Enter the projectiles angle: '))
force=float(input('Enter the launch force (1-10): '))

#calculate the distance
distance=force*FORCE_FACTOR

#set the heaading
turtle.setheading(angle)

#launch the projectile
turtle.pendown()
turtle.forward(distance)

#did it hit the target
if (turtle.xcor()>=TARGET_LLEFT_X and
    turtle.xcor()<=(TARGET_LLEFT_X+TARGET_WIDTH) and
    turtle.ycor()>=TARGET_LLEFT_Y and
    turtle.ycor()<=(TARGET_LLEFT_Y+TARGET_WIDTH)):
        print('Target hit')
else:
    print("you missed the target.")
