#@author Tobechi Onwenu
#Chapter 4 Algoritm Workbench page 225

#1.
'''
print('A while loop for multiples of 10 and less than 100')
num=float(input('Enter a number here: '))
product=num*10
while product<100:
    print(product)
'''

#2.
'''
print('A while loop to add two numbers together')
answer='y'
while answer=='y':
    num1=float(input('Enter first number here: '))
    num2=float(input('Enter second number here: '))
    sum=num1+num2
    print("sum is: ",sum)
    answer=input('Do you want to perform again, y or n: ')
'''

#3.
'''
print('A for loop to display odd numbers in range 1 to 100')
for num in range(1,101,+2):
    print(num,end=',')
'''
# answer 4 and 5#############
'''
#4.
text=int('')
while text<10:
    word=input('Type a word here: ')
    text=text+word
    print(text)
    word=input('Type a word here: ')
'''
'''
,,,
#5. 
print('Total of the following numbers')
total=0.0
start=1/30
end=30/1
for num in range(start,end,1):
#for num in range(1,30,1):
    total=total+num
    print(total)
'''
#7.
'''
print('Numbers\tMultiplication')
print('------------------------')
for num in range(1,10+1):
    for x in range(1,10+1):
        mul=x*1
        total=num*mul
        print(num,'*',mul,'=',total)

'''
#8.
enter=float(input('Enter a positive non-zero number here: '))
while enter<0:
    print('error; the score cannot be less than negative zero')
    enter=float(input('Enter the right number: '))
    print(enter)
