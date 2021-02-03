#chapter three questions


#test_average.py
'''
HIGH_SCORE=95
num=int(input('Enter 95: '))
num2=int(input('Enter 94: '))
num3=int(input('Enter 96: '))
average=(num+num2+num3)/3
print('average is:',average)
if average>=HIGH_SCORE:
 print('congratulation')

'''


#checkpont page 139 charpter 3

'''
x=0
y=20
if y==20:
    print(x)
'''

'''
sales=float(input('Enter the amount in sales: '))
print(sales)
if sales>=10000:
    commissionRate=.2
    total_sales=(.2*sales)+sales
    print(total_sales)

'''
'''
#auto repair chris page 141

base_hours=40
ot_multiplier=1.5
hours=float(input('Enter hours worked here: '))
pay_rate=float(input('Enter the hourly pay rate: '))
if hours>base_hours:
    overtime_hours=hours-base_hours
    overtime_pay=overtime_hours*pay_rate*ot_multiplier
    gross_pay=base_hours*pay_rate+overtime_pay
else:
    gross_pay=hours*pay_rate
print('The gross pay is $',format(gross_pay,',.2f'),sep='')
'''
'''

#Comparing strings
#password.py
password=input('Enter the password: ')
if password=='tobe':
    print('Password accepted')
else:
    print('Wrong password entered, try again please.')


#sort_names.py
name1=input('Enter full name (last  name first): ')
name2=input('Enter another full name (last  name first): ')
print('Here are the names, listed alphabetically.')
if name1<name2:
    print(name1)
    print(name2)
else:
    print(name2)
    print(name1)
'''

'''
if 'z'<'a':
    print('z is less than a.')
else:
    print('z is not less than a.')
'''


'''
#loan_qualifier.py
MIN_SALARY=30000.0
MIN_YEARS=2
salary=float(input('Enter your annual salary:'))
years_on_job=int(input('Enter the number of '+
                       'years employed: '))
if salary>=MIN_SALARY:
    if years_on_job>=MIN_YEARS:
        print('you qualify for the loan.')
    else:
        print('You must have been employed',
              'for at least', MIN_YEARS,
              'years to qualify.')
else:
    print('you must earn at least $',format(MIN_SALARY,',.2f'),
          ' per year to qualify.',sep='')
'''


#*************************************************HOW TO ADD NUMBERS TOGETHER USING SEP='' LINE 98***********************************************



#Grader.py
'''
A_SCORE=90
B_SCORE=80
C_SCORE=70
D_SCORE=60
score=int(input('Enter your test score: '))
if score>=A_SCORE:
    print('Your grade is A.')
else:
    if score>=B_SCORE:
        print('Your grade is B.')
    else:
        if score>=C_SCORE:
            print('Your grade is C.')
        else:
            if score>=D_SCORE:
                print('Your grade is D.')
            else:
                print('Your grade is F.')
'''

#checkpoint 3.13

'''
number=int(input('Enter number here: '))
if number==1:
    print('one')
else:
    if number==2:
        print('two')
    else:
        if number==3:
            print('three')
        else:
            print('unknown')

if number==1:
    print('one')
elif number==2:
    print('two')
elif number==3:
    print('three')
else:
    print('unknown')

'''

#laon_qualifier2.py the "and" opend

'''
MIN_SALARY=30000.0
MIN_YEARS=2
salary=float(input('Enter your annual salary:'))
years_on_job=int(input('Enter the number of '+
                       'years employed: '))
if salary>=MIN_SALARY and years_on_job>=MIN_YEARS:
    print('You qualify for the loan')
else:
    print('You do not qualify for this loan.')
'''

#laon_qualifier2.py the "or" opend
'''

MIN_SALARY=30000.0
MIN_YEARS=2
salary=float(input('Enter your annual salary:'))
years_on_job=int(input('Enter the number of '+
                       'years employed: '))
if salary>=MIN_SALARY or years_on_job>=MIN_YEARS:
    print('You qualify for the loan')
else:
    print('You do not qualify for this loan.')

'''

#Checkpoint 3.6 page 161
#3.18
'''
speed=float(input('Enter the speed value here: '))
if speed>=0 and speed<=200:
    print('The value is accurate.')


#3.19
speed=float(input('Enter the speed value here: '))
if speed<=0 or speed>=200:
    print('The value is not accurate.')
    
'''

#
