#@Tobechi onwenu
#chapter 3 answers cont'd page 176

#11. book club points

'''
books=int(input('Enter the number of books purchased here: '))
if books==0:
    print('Number of points earned is 0')
else:
    if books==2:
        print('Number of points earned is 5')
    else:
        if books==4:
            print('Number of points earned is 15')
        else:
            if books==6:
                print('Number of points earned is 30')
            else:
                if books==8:
                    print('Number of points earned is 60')

'''

#12. Software sales
'''
packages=int(input('Enter the number of packages purchased here: '))
x=99
discount1=.01*99
discount2=.02*99
discount3=.03*99
discount4=.04*99
discount_amount1=99-(.01*99)
discount_amount2=99-(.02*99)
discount_amount3=99-(.03*99)
discount_amount4=99-(.04*99)
if packages>=10 and packages<=19:
    print('You qualify for a 10% discount worth $',format(discount1,',.2f'),' and your total amount is $',format(discount_amount1,',.2f'),sep='')
else:
    if packages>=20 and packages<=49:
        print('You qualify for a 20% discount worth $',format(discount2,',.2f'),' and your total amount is $',format(discount_amount2,',.2f'),sep='')
    else:
        if packages>=50 and packages<=99:
            print('You qualify for a 30% discount worth $',format(discount3,',.2f'),' and your total amount is $',format(discount_amount3,',.2f'),sep='')
        else:
            if packages>=100:
                print('You qualify for a 40% discount worth $',format(discount4,',.2f'),' and your total amount is $',format(discount_amount4,',.2f'),sep='')

'''
#13. Shipping charges
'''
weight=float(input('Enter the weight of the package here: '))
pound1=1.50*weight
pound2=3.00*weight
pound3=4.00*weight
pound4=4.75*weight
if weight<=2:
    print('Shipping charges is $',format(pound1,',.2f'),sep='')
else:
    if weight>2 and weight<=6:
        print('Shipping charges is $',format(pound2,',.2f'),sep='')
    else:
        if weight>6 and weight<=10:
            print('Shipping charges is $',format(pound3,',.2f'),sep='')
        else:
            if weight>10:
                print('Shipping charges is $',format(pound4,',.2f'),sep='')
'''
#14. Body mass index
'''
weight=float(input('Enter your weigth here: '))
height=float(input('Enter your heigth here: '))
BMI=weight*(703/(height**2))
if BMI>=18.5 and BMI<=25:
    print('Your BMI index is ',format(BMI,'.1f'),'and your weight is optimal.')
else:
    if BMI<18.5:
        print('Your BMI index is ',format(BMI,'.1f'),'and you are underweight.')
    else:
        if BMI>25:
            print('Your BMI index is ',format(BMI,'.1f'),'and you are overweight.')

'''

#15. time calculator
'''
seconds=int(input('Enter a number of seconds here: '))
minutes=seconds//60
minute_remainder=seconds%60
hour=seconds//3600
hour_mremainder=(seconds//60)%60
hour_sremainder=seconds%60
day=seconds//86400
day_hremainder=(seconds//3600)%24
day_mremainder=(seconds//86400)%1440
day_sremainder=(seconds//86400)%86400
if seconds>=60 and seconds<3600:
    print('you entered ',minutes,'min and',minute_remainder,'s')
else:
    if seconds>=3600 and seconds<86400:
        print('You entered ',hour,'hour, ',hour_mremainder,'min and',hour_sremainder,'s')
    else:
        if seconds>=86400:
            print('You entered ',day,'days',day_hremainder,'hours',day_mremainder,'minutes and ',day_sremainder,'s')
        
'''

#16. February days
'''
print('This program calcutaes for leap years')
year=int(input('Enter a year here: '))
if year%4==0:
    if year%100==0 and year%400 !=0:
        print('Leap year')
    else:
        print('Not a leap year')

'''


'''
year=int(input('Enter year here: '))
lp=year/100
lp2=year/400
if lp=='yes':
    if lp2=='yes':
        print(leap)
'''

#17. Wi fi diagnostic tree
'''
wifi_prob=input('Do you have a wifi problem Yes or No? ')
if wifi_prob=='no':
    print('goodbye')
else:
    if wifi_prob=='yes':
        print('Reboot the computer and try to connect')
        answer1=input('did that fix the problem? ')
    if answer1=='yes':
        print('Goodbye')
    else:
        if answer1=='no':
            print('Reboot the router and try to connect')
            answer2=input('Did that fix the problem? ')
        if answer2=='yes':
            print('goodbye')
        else:
            if answer2=='no':
                print('Make sure the cables between the router and modem are plugged in firmly')
                answer3=input('Did that fix the problem? ')
            if answer3=='yes':
                print('Goodbye')
            else:
                if answer3=='no':
                    print('Move the router to a new location and try to connect')
                    answer4=input('Did that fix the router? ')
                if answer4=='yes':
                    print('Goodbye')
                else:
                    if answer4=='no':
                        print('Buy a new router')
'''

#18. Resturant selector
'''
print('Welcome to our resturant selector app')
print('Please answer yes or no to the following')
answer1=input('Is anyone in your party a vegetarian? ')
answer2=input('Is anyone in your party a vegetarian? ')
answer3=input('Is anyone in your party a vegetarian? ')
if answer1=='yes' and answer2=='yes' and answer3=='yes':
    print('Here are your resturant choices: \n Corner Cafe \n The Chef\'s Kitchen')
else:
    if answer1=='no' and answer2=='no' and answer3=='no':
        print('Here are your resturant choices:\n Joes\'s Gourmet Burgers')
    else:
        if answer1=='yes' and answer2=='no' and answer3=='no':
            print('Here are your resturant choices:\n Mama\'s Fine Italian')
        else:
            if answer1=='yes' and answer2=='no' and answer3=='yes':
                print('Here are your resturant choices:\n Mian Street Pizza Company\n Corner Cafe\n The Chef\'s Kitchen')

'''
for a in range(30):
    x=(2/29)-(1/30)
    print(x)
    
