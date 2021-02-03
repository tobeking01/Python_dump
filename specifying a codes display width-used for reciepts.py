#@author Tobechi Onwenu
#Secifying a codes display width(used in orfering reciepts)

# this gives a width display of 12 for the code with a commar
print('The number is',format(12345.6789,'12,.2f'))


# this gives a width display of 12 for the code
print('The number is', format(12345.6789,'12.2f'))

#This program displays numbers with arranged column and 2 decimal points alligned
num1=127.89945
num2=3465.148
num3=3.776
num4=264.821
num5=88.081
num6=799.9999
num7=99.99

#display each number in a field of 7 space with 2 decimal places.
print(format(num1,'7.2f'))
print(format(num2,'7.2f'))
print(format(num3,'7.2f'))
print(format(num4,'7.2f'))
print(format(num5,'7.2f'))
print(format(num6,'7.2f'))
print(format(num7,'7.2f'))

#other variations of num1
print('These are other variations of num1')
print(format(num1,'7.1f'))
print(format(num1,'7.3f'))
print(format(num1,'7.5f'))

