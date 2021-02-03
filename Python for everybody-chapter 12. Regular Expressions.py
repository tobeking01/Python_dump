#@Tobechi Onwenu
#Python for everybody. Regular expressions chapter 12. 

#We call regular expressions in our program using the "import re"
#We the search using the "re.search() to find string matches

'''
Python Regular Expression Quick Guide

^        Matches the beginning of a line
$        Matches the end of the line
.        Matches any character
\s       Matches whitespace
\S       Matches any non-whitespace character
*        Repeats a character zero or more times
*?       Repeats a character zero or more times 
         (non-greedy)
+        Repeats a character one or more times
+?       Repeats a character one or more times 
         (non-greedy)
[aeiou]  Matches a single character in the listed set
[^XYZ]   Matches a single character not in the listed set
[a-z0-9] The set of characters can include a range
(        Indicates where string extraction is to start
)        Indicates where string extraction is to end

''' 
#************1. Using re.search() like find()*************

#For example: Using the find() to display lines with 'From:' in it

hand=open('mbox-short.txt')
for line in hand:
    line=line.rstrip()  #removes the end \n
    if line.find('From')>=0:    
        print(line)     #Only prints lines with 'From:' in it


#Displaying the lines with 'From:' in it but in the regular expression technique

import re

hand=open('mbox-short.txt')
for line in hand:
    line=line.rstrip()
    if re.search('From:',line):
        print(line)



#**************2. Using re.search() like startswith()***********

hand=open('mbox-short.txt')
for line in hand:
    line=line.rstrip()
    if line.startswith('From:'):
        print(line)



import re

hand=open('mbox-short.txt')
for line in hand:
    line=line.rstrip()
    if re.search('^From:',line):
        print(line)
        


#3. Matching and extracting data using regular expressions.
#re.search() returns a true or false and matches the expression
#re.findall() extracts all matching strings

#****************Various exaples of using findall() in regular expressions.****

# finding number values in a file
import re

x=('My 2 favorite numbers are 19 and 42')
y=re.findall('[0-9]+',x)
#Above RE means find all expressions with a digit number from [0-9] (that's 0,1,2,3,4,5,6,7,8,9)
#then '+' repeat the charecter search throughout the document to findall with [0-9] all in ,x.
print(y)      #Answer['2','9','42']



#Non-Greedy Matching using the ? character

import re

x='From: Using the : character'
y=re.findall('^F.+?:',x)
#Above RE means findall that '^'starts with First character F. '.' means with more than one character like with the expression 'Fr..'
#then '+' add all match sets to a list in y from x. The '?' stop the search from adding extra words in cases of extra similar xters.
#':' is just an extra character from "From':'".
print(y)      #Display ['From:']


#Fine-Tuning String Extraction
#You can refine the match for re.findall() with parenthesis

x='From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008
y=re.findall('\S+@\S+',x) 
#the above RE means 
print(y)        #Display ['stephen.marquard@uct.ac.za'] 

#OR
y=re.findall('^From (\S+@\S+)',x)
#Above RE means find all words with '^' start with 'From' put a spcace the all the words aftre that have @ in between them with
#with no space between them.
print(y)

