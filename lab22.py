#@Author Tobechi Onwenu
#lab 22

import turtle
import random



def main():
    hello = turtle.Turtle()
    guess_number(hello)

def guess_number(hi):
    total = 0
    count = 0
    window = hi.getscreen()
    guess = int(window.textinput("Let's play a game", "Guess a number between 1 and 100"))
    while guess != -1:
        hidden_number = random.randint(1,100)
        count += 1
        total += 1
        if guess == hidden_number and count < 10:
            hi.write('Congratulations you guessed right')
        elif guess != hidden_number and count < 10 and guess < hidden_number:
            window = hi.getscreen()
            guess = int(window.textinput(" Too low try again!", "Guess a number between 1 and 100"))
            print(guess)
            print(hidden_number)
        elif guess != hidden_number and count < 10 and guess > hidden_number:
            window = hi.getscreen()
            guess = int(window.textinput(" Too high try again!", "Guess a number between 1 and 100"))
            print(guess)
            print(hidden_number)
        elif guess != hidden_number and count < 10:
            hi.write('Too bad you guessed wrong 10 times. YOU LOOSE.')
      

main()




'''
def capture_input(hi):
    window = hi.getscreen()
    name = window.textinput("You Just Won A Billion Dollars","Enter your name here: ")
    hi.write(name)
'''
