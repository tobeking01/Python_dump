#@Author Tobechi Onwenu
#Python for everybody chapter 4, Functions

#1. Building our own functions
#We create our own functions using the def keyword followed by optional parameters in parenthesis.
#we indent the body of the function
#This defines the function but does not execute the body of the function.
#It just remembers
#To execute we use def variable()

#A simple funtion
'''
x=5
print('Hello')
def print_lyrics():                                 #
    print("I'm a lumberjack, and I'm okay.")        #a funtion is defined
    print('I sleep all night and I work all day.')  #
print('Yo')
print_lyrics() #The function can be invoked as many times as posible(store and reuse pattern)
x=x+2
print(x)


#2. Arguments in funtions
#An argument is a value we pas into the function as its input when we call the funtion
#We use arguments so we can direct the function to do different kinds of work when we call it as different times
#We put the arguments in parentheses after the name of the funtion
big=max('Hello world') #max finds the lexically biggest number value in a set of word Answer=w
print(big)
'''
'''
#3. Parameters in functions
#A parameter is a variable which we use in the function definition.
#It is a "handle" that allows the code in the function to access the argumnets  for a particular funtion invocation.

lang=input("Enter 'es' for spanish\n"+
           "Enter 'fr' for french\n"+
           "Enter 'en' for English\n"+
           'Here please: ')
def greet(lang):
    if lang=='es':
        print('Hola')
    elif lang=='fr':
        print('Bonjour')
    else:
        print('Hello')
greet(lang)

'''
#4. Return values in functions
#Often a function will take its arguments, do some computation, and return a value to be used as the value of the function
#call in the calling expression. The return keyword is used for this.

def greet():
    return"Hello"
print(greet(), 'Glenn')
print(greet(),"Sally")


#A fruitful function is one that produces a result(or return value)
#The return staement ends the function execution and "sends back" the results of the function



lang=input("Enter 'es' for spanish\n"+
           "Enter 'fr' for french\n"+
           "Enter 'en' for English\n"+
           'Here please: ')
def greet(lang):
    if lang=='es':
        return 'Hola'
    elif lang=='fr':
        return 'Bonjour'
    else:
        return 'Hello'
print(greet(lang),'Glenn')
print(greet(lang), 'Jack')
'''

#5. Multiple Parameters/Arguments
# We can define more than one parameter in the function definition
# We  simply add more arguments when we call the function
#We match the number and order of arguments and parameters

def add_two(a,b):
    added=a+b
    return added
x=add_two(3,5)
print(x)

first=100
def pecentage():
    per=.03
    return per
inc=first*pecentage()
print(inc)

first=100
def pecentage():
    per=.03
    return ''  #This empty void can be used to stop a code from executing.
inc=first*pecentage()   #
print(inc)              # both codes do not execute.


'''
