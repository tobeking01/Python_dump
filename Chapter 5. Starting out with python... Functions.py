#@author Tobechi Onwenu
#Chapter 5. Functions.... Starting out with python... 

#5.1 function_demo.py
#This program demonstrates a function
#First we define a function named message
#we define a function using the function header and the block.

def message():              #*****Function Header*******
    print('I am Arthur.')           #***       ***
    print('King of the Bristons.')  #****BLOCK****

#call the function
message()


#5.2 two_functions.py
#This program has two functions. first we
#define the main function.

def main():
    print('I have a message for you.')
    message()
    print('Goodbye')

#next we define the message function.
def message():
    print('I am Arthur.')
    print('King of the Britons.')

#call the main function
main()

# This program displays step-bystep instructions
# for disassembling an Acme dryer.
# The main function performs the program's main #logic.
def main():
  # Display the start-up message.
  startup_message()
  input('Press Enter to see Step 1.')           #***********NOTE: You can use the input fintion to pause the program******
  # Display step 1.
  step1()
  input('Press Enter to see Step 2.')           #***********NOTE: You can use the input fintion to pause the program******
  # Display step 2.
  step2()
  input('Press Enter to see Step 3.')           #***********NOTE: You can use the input fintion to pause the program******
  # Display step 3.
  step3()
  input('Press Enter to see Step 4.')           #***********NOTE: You can use the input fintion to pause the program******
  # Display step 4.
  step4()
  
# The startup_message function displays the 
# program's initial message on the screen.
def startup_message():
  print('This program tells you how to')
  print('disassemble an Acme laundry dryer.')
  print('There are 4 steps in the process.')
  print()
  
# The step1 function displays the instructions
# for step 1.
def step1():
  print('Step 1: Unplug the dryer and')
  print('move it away from the wall.')
  print()
  
# The step2 function displays the instructions
# for step 2.
def step2():
  print('Step 2: Remove the six screws')
  print('from the back of the dryer.')
  print()
  
# The step3 function displays the instructions
# for step 3.
def step3():
  print('Step 3: Remove the back panel')
  print('from the dryer.')
  print()
  
# The step4 function displays the instructions
# for step 4.
def step4():
  print('Step 4: Pull the top of the')
  print('dryer stright up.')
  
# Call the main function to begin the program.
main()
