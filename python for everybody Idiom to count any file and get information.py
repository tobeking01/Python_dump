#@Author Tobechi Onwenu
#Using dictionaries
#simplified counting with get()

#we can use get() and provide a default value of zero when the key
#is not yet in the dictionary and then just add one


#counting any number of word in a document and show histogram
'''
#1. version 1
print('Version 1')
counts=dict()
names=['dave', 'susan', 'dave', 'jack','susan']
for name in names:
    counts[name]=counts.get(name,0)+1
print(counts)

#this loop goes on for ever in a file.


#********BETTER COUNTING PATTERN FOR HISTOGRAM********
#2, Version 2 for counting patterns

print('Version 2 counts words and values in any text')
counts=dict()
print('Enter a line of text: ')
line=input('')

words=line.split()

print('Words:',words)

print('counting...')
for word in words:
    counts[word]=counts.get(word,0)+1
print('counts',counts)




#3. Best version that = Good for file inputs...

name=input('Enter file: ')
handle=open(name)

counts=dict()
for line in handle:
    words=line.split()
    for word in words:
        counts[word]=counts.get(word,0)+1
bigcount=None
bigword=None
for word,count in counts.items():
    if bigcount is None or count>bigcount:
        bigword=word
        bigcount=count

print(bigword,bigcount)
'''



#***********************PLAY AROUND*****************************************
'''
counts=dict()
paper=input('Input paper Data here: ')
words=paper.split()
print('Words:',words)
print('counting...')
for word in words:
    counts[word]=counts.get(word,0)+1
print('counts',counts)
'''

paper=input('Input paper Data here: ')

counts=dict()
for line in paper:
    words=line.split()
    for word in words:
        counts[word]=counts.get(word,0)+1
bigcount=None
bigword=None
smallcount=None
smallword=None
for word,count in counts.items():
    if bigcount is None or count>bigcount:
        bigword=word
        bigcount=count
for word,count in counts.items():
    if smallcount is None or count<smallcount:
        smallword=word
        smallcount=count

print(smallword,smallcount)
print(bigword,bigcount)
