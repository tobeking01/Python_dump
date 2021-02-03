#@author Tobechi onwnenu
#python for everyone

#1. Looking inside strings
'''
print('using the index square brackets -- [] -- to get into strings')
print('for example')
fruit='banana'
letter=fruit[1]
print(letter)
print(fruit[4])
x=1
y=4
t=fruit[y+1]
w=fruit[x-1]
print(w)
print(t,'end')
for letters in fruit:
    print(letters,end='')
'''

#2. strings have lenght
'''
print('the built-in fintion -- len -- gives us the length of a string')
print('for example')
fruit='banana'
x=len(fruit)
print(x)
'''

#3. Looping Through a Strings indivual numbers
'''
print('we can use a while statement'+
      'and an iteration varialbe, and '+
      'the len function to loop inside letters'+
      'and index')
print('for example')
fruit='banana'
index=0
while index<len(fruit):
    letter=fruit[index]
    print(index,letter)
    index=index+1
'''
#4. Looping and counting
'''
print('This is a loop to count the number of times a letter occurs')
word='banana'
count=0
for letter in word:
    if letter=='a':
        count=count+1
print(count)
'''

#5. Slicing Strings
'''
print('The colon operator is used to slice chunks of stringd')
print('Monty Python')
print('01234567891011')
s='Monty Python'
print(s[0:4])
print(s[6:7])
print(s[6:20])
print(s[:2])
print(s[8:])
print(s[:])
'''

#6. string concatenation
'''
a='hello'
b=a+'there'
print(b)
c=a+' '+'there'
print(c)
'''

#7. using 'in' as a logical operator in strings
'''
fruit='banana'
'n' in fruit
print('yes')
if 'm' in fruit:
    print('yes')
else:
    print('no')
if 'a' in fruit:
    print('found it!')
'''

#8. String comparison
'''
word='banana'
if word=='banana':
    print('All right, bananas.')
if word<'banana':
    print('Your word,'+word+',comes before banana.')
elif word>'banana':
    print('Your word,'+word+',comes after banana.')
else:
    print('All right, banana.')
'''

#9. String Library
'''
greet='HELLO BOB'
zap=greet.lower()
print(greet)
print(greet.lower())
print(zap)
print('Hi TheRe i WaNNa Let You Go'.lower())
print('Hi TheRe i WaNNa Let You Go'.upper())
print('Hi TheRe i WaNNa Let You Go. today is your LAST day'.capitalize())
print(type(greet))
print(dir(greet))

#10 seaching a string
print('searching in a string')
print('banana')
print('012345')
fruit='banana'
pos=fruit.find('na')
print(pos)
aa=fruit.find('z')
print(aa)

#11. search and replace
greet='Hello Bob'
rep=greet.replace('Bob','Jane')
print(rep)
rep=greet.replace('o','x')
print(rep)


#12. Stripping Whitespace
greet='    Hello Bob   '
print(greet.lstrip())
print(greet.rstrip())
print(greet.strip())
'''

#13. prefixes string boolean
'''
line='please have a nice day'
if line.startswith('please'):
    print('Yes it starts with please')
if line.startswith('p'):
    print('yes')
else:
    print('no')
'''

#14. Parsing and extracting
'''
print('print the school name from the word below')
print(' From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008')
data='From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'

#first find the @ sign
first_position=data.find('@')
print(first_position)
#second find the space after the @ sign
second_position=data.find(' ',first_position)
print(second_position)
#display everything form first pos+1 to second pos
school_name=data[first_position+1:second_position]
print(school_name)
'''

