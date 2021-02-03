#@author Tobechi Onwenu
#Chapter 5. Functions part 3, Return function.... Starting out with python... 
'''

#Introduction to Value-Returning Functions: Generating Random Numbers
#CONCEPT: A value-returning function is a function that returns a value back to the
#part of the program that called it. Python, as well as most other programming languages, provides a library of prewritten
#functions that perform commonly needed tasks. These libraries typically contain a function
#that generates random numbers.

#A value-returning function is a special type of function. It is like a simple function in the
#following ways.
#   • It is a group of statements that perform a specific task.
#   • When you want to execute the function, you call it.

#Standard Library Functions and the import Statement
#Python, as well as most other programming languages, comes with a standard library of
#functions that have already been written for you. These functions, known as library functions, make a programmer’s job easier
#because they perform many of the tasks that programmers commonly need to perform.


#In order to call a function that is stored in a module, you have to write an import statement at the top of your program.
#An import statement tells the interpreter the name of the
#module that contains the function.

#Because you do not see the internal workings of library functions, many programmers think
#of them as 'black boxes'.

#Generating Random Numbers
#Random numbers are useful for lots of different programming tasks. The following are just
# few examples.

#• Random numbers are commonly used in games. For example, computer games that
#  let the player roll dice use random numbers to represent the values of the dice.
#  Programs that show cards being drawn from a shuffled deck use random numbers to
#  represent the face values of the cards.
#• Random numbers are useful in simulation programs. In some simulations, the computer must randomly decide
#  how a person, animal, insect, or other living being will
#  behave. Formulas can be constructed in which a random number is used to determine
#  various actions and events that take place in the program.
#• Random numbers are useful in statistical programs that must randomly select data for
#  analysis.
#• Random numbers are commonly used in computer security to encrypt sensitive data.
#Python provides several library functions for working with random numbers. These functions are stored in a module named random in the standard library.
#To use any of these functions you first need to write this import statement at the top of your program:

import random     #call a library function random into the program

#Examples
#Program 5-1 (random_numbers.py)
# This program displays a random number
# in the range of 1 through 10.

import random

def main():
    # Get a random number.
    number = random.randint(1, 10)      # find a random number between 1 and 10 and put it into variable number.
    # Display the number.
    print('The number is', number)

# Call the main function.
main()


# Program 5-2 (random_numbers2.py)
# This program displays five random
# numbers in the range of 1 through 100.
import random

def main():
    for count in range(5):
        # Get a random number.
        number = random.randint(1, 100) #A random number in the range of 1 through 100 will be assigned to the number variable.
        print(number)

# Call the main function.
main()

#Program 5-3 (random_numbers3.py)
# This program displays five random without the use of a variable.
# numbers in the range of 1 through 100.

import random

def main():
    for count in range(5):
        print(random.randint(1, 100))

# Call the main function.
main()



#Program 5-4 (dice.py)
# This program the rolling of dice.
import random

# Constants for the minimum and maximum random numbers
MIN = 1
MAX = 6

def main():
    #Create a variable to control the loop.
    again= 'y'

    #Simulate rolling the dice.
    while again == 'y' or again == 'Y':
        print('Rolling the dice...')
        print('Their values are:')
        print(random.randint(MIN, MAX))
        print(random.randint(MIN, MAX))
        #extra
        print("Random 1-10 times 2=",random.randint(1,10)*2)
        #Do another roll of the dice?
        again = input('Roll them again? (y = yes): ')


#Call the main function.
main()

'''

