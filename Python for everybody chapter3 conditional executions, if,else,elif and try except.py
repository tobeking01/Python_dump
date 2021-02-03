#@Tobechi Onwenu
#Python for everybody chapter3 conditional executions, if,else,elif and try/except

#1. Comparism operators
'''
x=5
print('If x=5 then these statements are true')
if x==5:
    print('Equals 5')
if x>4:
    print('Greater than 4')
if x>=5:
    print('Greater than or Equals 5')
if x<=5:
    print('Less than or Equals 5')
if x !=6:
    print('Not equal 6')


#2. One - way decisions (best when you use 'if' statements).
x=5
if x==5:
    print('yes')
if x==6:
    print('yes again')

x=5
print(x)
if x>2:
    print('Bigger than 2')
print('Done with 2')
for i in range(5):
    print(i)
    if i>2:
        print('Bigger than 2')
    print('Done with i ',i)
print('All done')

#3. Two way decison( bset if you use the 'if' 'else' statement)
#only use for 'either' or 'or' situations
x=4
print(x)
if x>2:
    print('Bigger than 2')
else:
    print('Smaller than 2')
print('All done')


#4. Multi-way(make multiple decisions using the 'if','elif'....'else' statement
print('Note the elif ends whenever the first question certifies '+
      'so be careful with placement')
print('Example 1')
x=20
print(x)
if x<20:
    print('x is Small')
elif x<10:
    print('x is Medium')
else:
    print('x is Large')
print('All done')

print('Example 2, Note the sequence of question'+
      'How they follow in value')
x=100
print('x is ',x)
if x<2:
    print('x is Small')
elif x<10:
    print('x is Medium')
elif x<20:
    print('x is Big')
elif x<40:
    print('x is Large')
elif x<100:
    print('x is Huge')
else:
    print('x is Ginormous')



#4. The try/except Structure
print('Insurance policy for every code')
print('Examples below')
word='Hello World'
try:
    istr=int(word)# if a integer was entered print function still execute.
except:
    istr=-1
print('First is ',word)

word='123'
try:
    istr=str(word)# if a string was entered print function still execute.
except:
    istr=-1
print('Second is ',word)

word=input('Enter a word or number here: ')
try:
    istr=int(word) #if word entered is integer except u can use 'str(word)' or just 'word' too.
except:
    istr=-1  #it blows up here but continues to print regardles
print('Input is ',word)

#Becareful with the scope of coverage on try/except
#for example
word='Bob'
try:
    print('Hello')
    inst=int(word)#The code is converted to integer and trigger except
    print('There')#So therefore this code never got to run
except:
    inst=input('here:')
    print('input is ',inst)
print('Do instructions ',inst)
print(word)


'''
#5. Examples of real data usage of try and except
print('Try and except code to request only integers.')
bad_input=input('Enter a letter instead of a number: ')
try:
    ival=int(bad_input) #word checked if integer blow but goes to except
except:
    ival=-1 #except makes ival the integer -1
if ival>0:
    print('Nice work')  #because -1 is less than 0 not working
else:
    print('Not a number!') #does this line instead
    good_input=input('Must Enter a number now: ')
    print('Number entered is',good_input)
print('Input entered is ',bad_input)
