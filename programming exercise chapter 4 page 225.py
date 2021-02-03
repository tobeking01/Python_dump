#@author Tobechi Onwenu
#chapter 4 programming exercises page 225

#1. Bug collector
'''
print('This is a loop to calculate the bugs collected over 5 days')
count=0.0
for days in range(5):
    bugs=int(input('Enter number of bugs collected here: '))
    count+=bugs
    print(count)
    
'''
#2. calories burned
'''
print('A loop to display number of calories'+
      ' burned per time on a treadmill')
print('Time\tCalories burned')
print('----------------------')
for time in range(10,31,5):
    cal=4.2*time
    print(time,'mins\t',cal,'calories',sep='')
'''

#3. Lap Times
'''
fastest=0.0
slowest=0.0
add=0.0
num=int(input('Enter the number of times run around the track: '))
for laps in range(num):
    lap_time=float(input('Enter the lap times here: '))
    if lap_time<=fastest or fastest==0.0:
        fastest=lap_time
    if lap_time>=slowest or slowest==0.0:
        slowest=lap_time  
    add+=lap_time
print('fastest is ',fastest)
print('slowest is ',slowest)
avg=add/num
print('Average is ',avg)

'''        

#4. distance travelled
'''
print('This program displays the distance travelled over time')
speed=int(input('What is the speed of the vehicle in MPH? '))
time=int(input('How many hours has it travelled? '))
print('Hour\tDistance Travelled')
print('-------------------------')
for num in range(1,time+1,1):
    distance=num*speed
    print(num,'\t',distance)
'''    
#5. Average rainfall
'''
years=int(input('Enter the number of years here: '))
cal=0.0
month=12
num_month=0.0
for x in range(years):
    print('Enter details for year',x+1,'here')
    for time in range(1,month+1,1):
        data=float(input('Enter the inches in ranfall for month1 here: '))
        cal+=data
    avg=cal/12
    num_month+=12
print('Months\tTotal inches of rainfall\tavg rainfall per month')
print('---------------------------------------------------')
print(num_month,'\t','\t',cal,'\t','\t','\t',avg)
'''
#6. Miles to kilometers table
'''
print('A table changing miles to Kilometer')
print('Miles\tKilometer')
print('-----------------')
for mile in range(10,81,10):
    km_calc=1.60934*mile
    print(mile,'\t',format(km_calc,'.2f'))
'''
#7. pennies for pay
'''
add_one=0.0
add_two=0.0
total_penny=0.0
print('This program calculates how much you make per day for a penny')
num=int(input('Enter number of days to work here: '))
print('Days\tSalary')
print('------------')
for one in range(1,3):
    add_one+=one
    print(one,'\t',one)
for penny in range(3,num+1):
    pennies=penny+penny
    add_two+=pennies
    print(penny,'\t',pennies)
total_penny=add_one+add_two
total_penny/=100
print('The total pay is $',format(total_penny,'.2f'),'cents',sep='')
'''

#8. average world lenght
'''
total_letters=0.0
total_words=0.0
word=''
print('This program calculates the avreage lenght of words')
word=input('Enter word here; ')
while word !=(''):
    total_letters+=len(word)
    total_words+=1
    word=input('Enter word here: ')
avg=total_letters/total_words
print(total_letters)
print(total_words)
print(avg)
'''

#9. ocean levels
'''
print('This shows how high the oceans will rise each year')
print('Year\tRise in Sea Level')
print('....................')
per_year=1.6
for mili in range(1,26,1):
    year=mili*per_year
    print(mili,'\t',format(year,'.1f'),'milimeters')
'''
#10. tuition increase
'''
print('This program calculates an annual 3% inc for 5 years')
tuition=8000
per=.03
total=(tuition*per)+tuition
print('Year one tuition is: $',format(tuition,'.2f'),sep='')
print('Year two tuition is: $',format(total,'.2f'),sep='')
for next in range(5):
    total=(tuition*per)+tuition
for next in ('three','four','five'):
    per_inc=.03*total
    total=total+per_inc
    print('year ',next,' tuition is: $',format(total,'.2f'),sep='')

'''
#11. Sleep debt
'''
print('This program calculates sleep for 7 days')
desirable=8*7
total=0.0
for days in range(7):
    sleep_day=int(input('Enter the hours slept: '))
    total+=sleep_day
    final=total-desirable
    if final>=0 :
        print('I am so jealous')
'''

#12. Calculating the factorial of a number
'''
ad=1
num=int(input('Enter a nonnegative integer number here: '))
for n in range(1,num+1):
    ad*=n
    print(ad)
'''
#13. population
'''
print('Tihs app predicts the approx population of organisms')
start=int(input('What is the starting number of organisms? '))
avg_inc=float(input('What is the average daily inc in %? '))
daily_mul=int(input('What is the number of days left to multiply? '))
per=avg_inc/100
all=0.0
print('Day Approximate\tPopulation')
print('----------------------------')
print('1\t\t ',start)
for day in range(2,daily_mul+1):
    start=start+(start*per)
    print(day, "\t\t ",start)

'''



#test
word=''
while word <='          ':
    word=input("words: ")
else:
    print('bye')
