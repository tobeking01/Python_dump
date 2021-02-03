#@Tobechi onwenu
#String Parsing Examples


#Old method
#Single split method. Extracting a host name using find and sstring slicing.

data='From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'

atpos=data.find('@')
print(atpos)   #21

sppos=data.find(' ',atpos)   #find the space after @ word collection
print(sppos) #31

host=data[atpos+1:sppos]
print(host)


#New Method
#The Double Split Pattern

line='From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'

words=line.split()          #All words split to Lists
email=words[1]              #['stephen.marquard@uct.ca.za'] is pulled out because it is in postion 1 after 0 on a list.
pieces=email.split('@')     #email in split to two based on the @ sign: ['stephen.marquard','uct.ac.za']
print(pieces[1])            #Display 'uct.ac.za' as [1] pulls out 1 position in the list above again. Simple.


#***************Using The Regular Expression Method********************

import re

lin='From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
y=re.findall('@([^ ]*)',lin)

#The above code means '@ look for @ sign first then from that point everything in parenthesis ( put in a non-blank list 
# [^ ] ,Note the space after ^ which tells it to pick every word till the first blank space(i.e before S).
#* Add all macthing from position 0=(From)on the list and stop when you find it.note '?' can be added to stop greediness.

print(y[0])        # Display is ['uct.ac.za']. we use[0] to remove the list bracket



#Better code would be
y=re.findall('^From .*@([^ ]*)',lin)
print(y[0])



#****************************Other Examples*************************

#
import re
hand=open('mbox-short.txt')
numlist=list()
for line in hand:
    line=line.rstip()
    stuff=re.findall('^X-DSPAM-Confidence: ([0-9.]+)',line)
    if len(stuff) !=1: continue #This means if the things in stuff is empty continue searching the document until you find one thing.
    num=float(stuff[0])
    numlist.append(num)
print('Maximum: ', max(numlist))   #max(numlist) will print out the largest number in the empty list appended.


#Escape Character
#If you want a special regular character to just behave normally(most of the time) you prefix it wit '\'

import re
x='We just recieved $10.00 for cookies.'
y=re.findall('\$[0-9. ]+',x)
print(y)        #[display$10.00']

    
