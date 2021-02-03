#@author Tobechi Onwenu
#(1)Exaples of code with no formatting.
#(2)How a floating point works
#(3)Exaples of code with number formatted.
#(4)The sep='' function.
#(5)How a number can be displayed as currency.





#(1)Exaples of code with no formatting.
#First with no_formatting.py
amount_due=5000
monthly_payment=amount_due/12
print('The monthly payment is', monthly_payment)

#(2)How a floating point works
print(format(12345.6789, '.2f'))

print(format(12345.6789, ".1f"))

print(format(12345.6789, ',.2f'))


#(3)Exaples of code with number formatted.
#Number can be formatted
amount_due=5000.0
monthly_payment=amount_due/12
print('The monthlty payment is',format(monthly_payment,'.2f'))


#(4)The sep='' function.
#It brings toghether words in a string without spaces
print('one','two','three')
print('one','two','three',sep='')
print('one','two','three',sep='***')


#(5)How a number can be displayed as currency.
#Number can be displayed as currency
monthly_pay=5000.0
annual_pay=monthly_pay*12
print('Your annual pay is $',format(annual_pay,',.2f'),sep='')
