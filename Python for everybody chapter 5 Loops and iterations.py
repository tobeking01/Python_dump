#@Author Tobechi Onwenu
#Python for everybody chapter 5. Loops and iteration


#**************INDEFINITE LOOPS. The 'while' loop**********************

#while loops are called "indefinite loops" because they keep going until a logical condition is false
#It acts like the if statement but repeats a question while the iteration is true or false.

#1. for example; Repeated steps while n>0 is true
'''
n=5
while n>0:
    print(n)
    n=n-1    #this takes away 1 from n every time the loop runs until 0 then stops.
print(n,',Blastoff')


#2. Getting out of a loop or continuing a loop
#'continue' is used to tell the while loop to jump back to the beginneg of the while toop again
#'break' is used to jump all codes left in the while loop

#Example

while True:
    line=input("# + number or 'done' here: ")
    if line[0]=='#':
        continue
    if line=='done':
        break
    print(line)
print('done')

'''

#************ DEFINITE LOOPS. The 'for' loop ***********

#If you want to run through a list of numbers,characters in strings,strings in a sntence e.t.c or anything that has a definite ending we use the for loop
#We say that Definite loops iterate through the members of aset

#examples:
#1.
'''
for i in [5,4,3,2,1]:
    print(i)
print('Blastoff')


#2.
friends=['Joseph', 'Glenn', 'Sally']
for friend in friends:
    print('Happy New year',friend)
print('done')

#3.

# Lookig at 'in' ...
#the in iterable variable "iterates" through the sequence(ordered set)
#the block(body) of code is executed once for each value in the sequence.
#Note for loops are preferable to while loops as they are cleaner, precise and use less codess.


#4. Loop Idioms
# Making smart lopps demand knowing something about the whole loop for something that sees one loop at a time
#for this we use smart loops to:
#set some variable to initial value
#look for a variable
#update a variable
#do something to a variable
# display a variable

print('Before')
for thing in (9,41,12,13,74,15):
    print(thing)
print('After')


#5. Counting in a loop
count=0
print('before', count)
for thing in (9,41,12,3,74,151):
    count=count+1
    print(count,'. ', thing,sep='')
print('After',count)

#6. Summing in a loop

total=0
print('Before',total)
for thing in (9,41,12,3,74,15):
    total=total+thing
    print(total,thing)
print('After',total)




#7. Finding the average in a loop
count=0
total=0
print('Count \t Values \t Total ')
print('----------------------------------------')
for thing in (9,41,12,3,74,15):
    count=count+1
    total=total+thing
    avg=total/count
    print(count,'\t ',thing,'\t        ',total)
print('Average is ',format(avg,'.2f'))
print('Done')

'''
#8. Seaching using Boolean varaibles
#find the biggest and smallest number using the 'None' function in for loops

print('Find the biggest number')
biggest= None
print('Before')
for numbers in (9,41,12,13,74,15):
    if biggest is None:
        biggest=numbers
    elif numbers>biggest:
        biggest=numbers
    print(biggest,numbers)
print('After, Biggest is ',biggest)


print('Find the smallest number')
smallest= None
print('Before')
for numbers in (9,41,12,13,74,15):
    if smallest is None:
        smallest=numbers
    elif numbers<smallest:
        smallest=numbers
    print(smallest,numbers)
print('After, Smallest is ',smallest)


#***********  'IS' AND 'IS NOT' STATEMENTS ARE STRONGER THAN EQUALS... USE SPARINNGL
#ONLY USE ON BOOLEANS (TRUE/FAALSE) AND
#ON 'NONE' TYPES.
