#@Tobechi Onwenu
#Reading files

#1. Opening a file

#To open a file we use a variable(handle) to attach the open() function.

handle=open(filename,mode) #This returns a manipulation to handle the file

#mode is optional 'r' if you plan to read the file and 'w' if you plan to write
# E.g:

fhand=open('mbox.txt','r')

#2. File processing

#we use the \n in code to move lines to the next line
#A document works in the same way with \n at end of each line
#A text file can be thought of as a sequence of lines


#3. The Almighty For Loop Again in file procesing.

fhand=open('mbox.txt')
for words in fhand:
    print(words)

#4. Counting lines in a file
fhand=open('mbox.txt')
count=0
for line in fhand:
    count=count+1
    print('Line count: ',count)


#5. Reading the *Whole* File
#we can read the whole file(newlines and all) into a single string.

fhand=open('mbox-short.txt')
all=fhand.read()
print(len(all)) #print the number count of all individual characters.

print(all[:20]) #print the first 20 word in lenght(including spacings.)


#*******************6. Searching through a file******************************


# we use the if statement in the for loop to only print lines that meet
# some criteria.


#1st Method

fhand=open('mbox-short.txt')
for line in fhand:
    line=line.rstrip() #This is used to strip the extra at the enof the text thereby alighning the lines better.
    if line.startswith('From:'):
        print(line)     #Note the print call is aligned.


#2nd Method Using the 'if not' argument and continue

fhand=open('mbox-short.txt')
for line in fhand:
    line=line.rstrip() #This is used to strip the extra at the enof the text thereby alighning the lines better.
    if not line.startswith('From:'):
        continue
    print(line)  #Note the print call is indent is One step back.        


#3rd Method Using 'in' to select line

fhand=open('mbox-short.txt')
for line in fhand:
    line=line.rstrip()
    if not '@uct.ac.za' in line:    # I LOVE THIS
        continue                    #   STATEMENT.
    print(line)


#Extra Prompt for a file name
fname=input('Enter the file name: ')
fhand=open(fname)

#Bad File Names-How to solve with try and except

fname=input('Enter the file name: ')
try:
    fhand=open(fname)
except:
    print('File cannot be opened: ',fname)
    quit()


#Extra
fname=input('Enter the file name: ')
try:
    fhand=open(fname)
except:
    print('File cannot be opened: ',fname)
    quit()

count=0
for line in fhand():
    if line.startswith('Subject:'):
        count=count+1
print('There were',count,'lines with Subjects: in',fname)
