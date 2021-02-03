#@author Tobechi Onwenu
#Chapter 5. Functions.... Starting out with python... Local, Global Variables and global constants. 


#local variable: Anything you assign a value to a variable inside a function,
#You create a local variable.
#It cannot be seen by another function.
'''
#for example:
def main():
    get_name()          #The name input does not execute. NO ACCESS.
    print('Hello')

def get_name():
    name=input('Enter name here: ')     #name is the local variable for this function.
main()



#Arguments and Parameters
#An argument is any piece of data that is passed into a function when the funtion
#is called.

#show_double(value)   #value is an example of an argument.

#A parameter is a variable that recieves an argument that is passed into the function.
#*******************NOTE: Theargument is interchageable with each other based on last to be in argument form.
#Example:

def main():
    value=5
    show_double(value)      #value is an example of an argument HERE.


def show_double(number):     #value is an example of an parameter HERE.
    result=number*2
    print(result)

main()       #Solution=10.   

#Passing an argument to a function
# 5-7. cups_to_ounces.py

# This program converts cups to fluid ounces.

def main():
	# Display the intro screen
	intro()
	# Get the number of cups.
	cups_needed = int(input('Enter the number of cups: '))
	# Convert the cups to ounces.
	cups_to_ounces(cups_needed)         #note the subtitution done with parameters and arguments together. cups_needed replaces cups in function.

# The intro function displays an Introductory screen.
def intro():
	print('This program converts measurements')
	print('in cups to fluid ounces. For your')
	print('references the formula is:')
	print(' 1 cup = 8 fluid ounces')
	print()

# The cups_to_ounces function accepts a number of
# cups and displays the equivalent number of ounces.
def cups_to_ounces(cups):
	ounces = cups * 8
	print('That converts to', ounces, 'ounces.')

# Call the main function
main()


#Passing multiple Arguments
#5-8. multiple_args.py

# This program demonstrates a function that accepts
# two arguments.

def main():
    print('The sum of 12 and 45 is')
    show_sum(12, 45)
# The show_sum function accepts two arguments
# and displays their sum.
def show_sum(num1, num2):
    result = num1 + num2
    print(result)
    
#call the main function
main()


# 5-9 String_args.py
#This program demonstrates passing two strings
#arguments to a function

def main():
    first_name=input('Enter your first name: ')
    last_name=input('Enter your last name: ')
    print('Your name reversed is')
    reverse_name(first_name,last_name)
def reverse_name(first,last):
    print(last,first)

#call main funtion
main()




# 5-11. Keyword arguments

# This program demonstrates keyword arguments.

def main():
    #show the amount of simple interest, using 0.01 as
    #interest rate per period, 10 as the number of periods
    #and $10,000 as principal
    show_interest(rate=0.01, periods=10, principal=10000.0)

def show_interest(principal, rate, periods):
    interest= principal * rate * periods
    print('The simple interest will be $', format(interest,'.2f'),sep='')

main()
'''
# 5.6 Global Variables and global constants
# A Global variable is accessible to all functions in a program file.

#Program 3-7 (global1.py)
# Create a global variable.
my_value = 10

# The show_value function prints
# the value of the global variable.
def show_value():
    print(my_value)

# Call the show_value function.
show_value()

#The assignment statement in line 2 creates a variable named my_value. Because this
#statement is outside any function, it is global. When the show_value function executes, the
#statement in line 7 prints the value referenced by my_value.


# Declaring variables.
#An additional step is required if you want a statement in a function to assign a value to a global
#variable. In the function you must declare the global variable, as shown in Program 3-14.

#Program 3-14 (global2.py)

# Create a global variable.
number = 0

def main():
    global number
    number = int(input('Enter a number: '))
    show_number()

def show_number():
    print('The number you entered is', number)

# Call the main function.
main()

#***************IT IS BETTER TO USE LOCAL VARIABLES THAN GLOBAL IN PROGRAMMING AS THEY MAKE DEBUGGING VERY HARD**************************


#Global constant are very much encouraged though. 

# GLOBAL CONSTANTS
# The following is used as a global constant
# the contribution rate.


CONTRIBUTION_RATE = 0.05        #global constant

def main():
    gross_pay = float(input('Enter the gross pay: '))
    bonus = float(input('Enter the amount of bonuses: '))
    show_pay_contrib(gross_pay)
    show_bonus_contrib(bonus)

# The show_pay_contrib function accepts the gross
# pay as an argument and displays the retirement
# contribution for that amount of pay.
def show_pay_contrib(gross):
    contrib = gross * CONTRIBUTION_RATE
    print('Contribution for gross pay: $',format(contrib, ',.2f'),sep='')

# The show_bonus_contrib function accepts the
# bonus amount as an argument and displays the
# retirement contribution for that amount of pay.
def show_bonus_contrib(bonus):
    contrib = bonus * CONTRIBUTION_RATE
    print('Contribution for gross pay: $',format(contrib,',.2f'),sep='')

# Call the main function.
main()

#First, notice the global declaration in line 3:
#CONTRIBUTION_RATE = 0.05
#CONTRIBUTION_RATE will be used as a global constant to represent the percentage of an
#employee’s pay that the company will contribute to a retirement account. It is a common
#practice to write a constant’s name in all uppercase letters. This serves as a reminder that
#the value referenced by the name is not to be changed in the program


