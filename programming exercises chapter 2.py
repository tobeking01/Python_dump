#@author tobechi onwenu
#programming exercises chapter 2 (1-5)

#1. personal information
print('My name is Tobe')
#others

#2. sales prediction
annual_profit=.23
total_sales=float(input('Enter total sales here: '))
profit=total_sales*annual_profit
print(profit)

#3. pounds to kilograms
mass=float(input('Enter the mass in pounds of the object here; '))
kilograms=mass*.454
print(kilograms)

#4. total purchase
item_one=float(input('Enter item one price: '))
item_two=float(input('Enter item two price: '))
item_three=float(input('Enter item three price: '))
item_four=float(input('Enter item four price: '))
item_five=float(input('Enter item five price: '))
sales_tax=0.07
print('This is the sales tax', sales_tax)
subtotal=item_one+item_two+item_three+item_four+item_five
print('This is the sales tax',subtotal)
after_tax=subtotal*sales_tax
total=subtotal+after_tax
print('This is the sales tax',total)

#5. Distance travelled
print('A car is travelling at 70mph. find distace in:')
speed=70
print('This is the cars speed:',speed)
time_one=6
time_two=10
time_three=15
distance_one=speed*time_one
distance_two=speed*time_two
distance_three=speed*time_three
print('This is distance at time 6 hours;',distance_one,'m')
print('This is distance at time 10 hours;',distance_two,'m')
print('This is distance at time 15 hours;',distance_three,'m')



                 
