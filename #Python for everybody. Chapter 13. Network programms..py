#@author Tobechi Onwenu
#Python for everybody. Chapter 13. Network programms.


#To get into any network we use the http port 80 mostly to call the server.

#********** An HTTP Request in Python to connect to a network browser*******
'''
import socket

mysock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd= 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if (len(data) <1):
        break
    print(data.decode())
mysock.close()


#************************Done*****************************

#http://www.py4e.com/book.php


#^^^^^^^^^^^^^^^^^^^^^^^^^UTF-8 is recommended practice for encoding    data to be exchanged between systems.*******************

#*********** Making HTTP Easier With urllib *********
#Since HTTP is so common, we have a library that does all the socket work
#for us and makes web pages look like a file


#Using urllib in python to web browse.

import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
for line in fhand:
    print(line.decode().strip())
    

#****** Like a File... To make a dictionary of a web page*************

import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')

counts = dict()                 # Make dictionary.
for line in fhand:
    words = line.decode().split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1
print(counts)



# Reading Web Pages

import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen('http://www.dr-chuck.com/page1.htm')
for line in fhand:
    print(line.decode().strip())

'''

#***********using beautiful soup software for easy web scrapping***********************

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url = input('Enter - ')         # input any url to grab all web links associted with that address.
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags
tags = soup('a')
for tag in tags:
    print(tag.get('href', None))
