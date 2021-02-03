#@Tobechi Onwenu
#Programming exercises chapter 3 page 173

#1.Number analyser
'''
number=int(input('Enter any number here: '))
if number>0:
    print('positive')
else:
    if number<0:
        print('negative')
    else:
        if number==0:
            print('Zero')
if number>=0:
    print("Even")
else:
    print('Odd')

#2. Area of rectangles

lenght1=float(input('Enter the lenght of the first rectangle here: ;'))
width1=float(input('Enter the width of the first rectangle here: ;'))
lenght2=float(input('Enter the lenght of the second rectangle here: ;'))
width2=float(input('Enter the width of the second rectangle here: ;'))
area1=lenght1*width1
area2=lenght2*width2
if area1>area2:
    print('Area1 has the greatest area ',area1)
else:
    if area2>area1:
        print('Area2 has the greatest area ',area2)
    else:
        print('The areas are the same ')

#3. Quater of the year

month=int(input("Enter any Month in number form here: "))
if month<=3:
    print('The Month is in the first quarter.')
else:
    if month>4 and month<6:
        print('The Month is in the second quarter.')
    else:
        if month>=7 and month<=9:
            print('The Month is in the third quarter.')
        else:
            if month>10 and month<12:
                print('The Month is in the forth quarter.')
            else:
                print('error')



#4. roman numerals
number=int(input('Enter a number from 1-10 here: '))
if number==1:
    print('I')
else:
    if number==2:
        print('II')
    else:
        if number==3:
            print('III')
        else:
            if number==4:
                print('IV')
            else:
                if number==5:
                    print('V')
                else:
                    if number==6:
                        print('VI')
                    else:
                        if number==7:
                            print('VII')
                        else:
                            if number==8:
                                print('VIII')
                            else:
                                if number==9:
                                    print('IX')
                                else:
                                    if number==10:
                                        print('X')
                                    else:
                                        print('error')


#5. Mass and Weight
mass=float(input('Enter the mass of the object here; '))
weight=mass*9.8
if weight>500:
    print("The object is too heavy")
else:
    if weight<100:
        print('The object is too light')


#6. Magic dates
month=int(input('Enter a month in numbers here: '))
day=int(input('Enter a day in numbers here: '))
year=int(input('Enter a year in two digit form here: '))
calc=month*day
if year==calc:
    print('The date is magic')
else:
    print('The date is not magic')
'''
'''
#7. Grade calculator
test=int(input('Enter your test scores here: '))
exam=int(input('Enter your exam scores here: '))
score=test+exam
if not(test>=0 and test<=25):
    print('error')
else:
    if not(exam>=0 and exam<=50):
        print("error")
    else:
        if score>=50 and exam>=25:
            print('You passed the class.')
        else:
            if score<50 or exam<25:
                print('You failed the class.')
            else:
                if score>80:
                    print('You recieved a Distinction.')
                else:
                    if score>50 and score<59:
                        print('You passed.')
                    else:
                        if score<80 and score>60:
                            print('You get a Credit Grade.')
                        else:
                            if score<60:
                                print('You get a Pass Grade')
                            else:
                                print("This is yours points: ",score)
                        
'''
'''
#8. Hot Dog Cookout calculator
people=int(input("Enter the number of people attending: "))
number_dogs=int(input('Enter the number of hot dogs per person: '))
total=people*number_dogs
even=total/10
odd=total/8
leftover_dogs=total%10
leftover_buns=total%8
if odd>even:
    print('This is the number of hot dog packages needed ',format(even,'.0f'))
    print("This is the number of hot dog packages leftover ",format(leftover_dogs,'.0f'))
    print('This is the number of hot dog buns packages needed ',format(odd,'.0f'))
    print("This is the number of hot dog buns packages leftover ",format(even,'.0f'))

'''

#9. Roulette wheel colors
'''
num=int(input('Enter a number from 0 -36 here: '))
if num==0:
    print('The pocket is green.')
else:
    if num==1:
        print('The pocket is red.')
    else:
        if num==2:
            print('The pocket is black.')
        else:
            if num==3:
                print('The pocket is red.')
            else:
                if num==4:
                    print('The pocket is black.')
                else:
                    if num==5:
                        print('The pocket is red.')
                    else:
                        if num==6:
                            print('The pocket is black.')
                        else:
                            if num==7:
                                print('The pocket is red.')
                            else:
                                if num==8:
                                    print('The pocket is black.')
                                else:
                                    if num==9:
                                        print('The pocket is red.')
                                    else:
                                        if num==10:
                                            print('The pocket is black.')
                                        else:
                                            if num==11:
                                                print('The pocket is black.')
                                            else:
                                                if num==12:
                                                    print('The pocket is red.')

                                                else:
                                                        if num==13:
                                                            print('The pocket is black.')
                                                        else:
                                                            if num==14:
                                                                print('The pocket is red.')
                                                            else:
                                                                if num==15:
                                                                    print('The pocket is black.')
                                                                else:
                                                                    if num==16:
                                                                        print('The pocket is red.')
                                                                    else:
                                                                        if num==17:
                                                                            print('The pocket is black.')
                                                                        else:
                                                                            if num==18:
                                                                                print('The pocket is red.')
                                                                            else:
                                                                                if num==19:
                                                                                    print('The pocket is red.')
                                                                                else:
                                                                                    if num==20:
                                                                                        print('The pocket is black.')
                                                                                    else:
                                                                                        if num==21:
                                                                                            print('The pocket is red.')
                                                                                        else:
                                                                                            if num==22:
                                                                                                print('The pocket is black.')
                                                                                            else:
                                                                                                if num==23:
                                                                                                    print('The pocket is red.')
                                                                                                else:
                                                                                                    if num==24:
                                                                                                        print('The pocket is black.')
                                                                                                    else:
                                                                                                        if num==25:
                                                                                                            print('The pocket is red.')
                                                                                                        else:
                                                                                                            if num==26:
                                                                                                                print('The pocket is black.')
                                                                                                            else:
                                                                                                                if num==27:
                                                                                                                    print('The pocket is red.')
                                                                                                                else:
                                                                                                                    if num==28:
                                                                                                                        print('The pocket is black.')
                                                                                                                    else:
                                                                                                                        if num==29:
                                                                                                                            print('The pocket is black.')
                                                                                                                        else:
                                                                                                                            if num==30:
                                                                                                                                print('The pocket is red.')
                                                                                                                            else:
                                                                                                                                if num==31:
                                                                                                                                    print('The pocket is black.')
                                                                                                                                else:
                                                                                                                                    if num==32:
                                                                                                                                        print('The pocket is red.')
                                                                                                                                    else:
                                                                                                                                        if num==33:
                                                                                                                                            print('The pocket is black.')
                                                                                                                                        else:
                                                                                                                                            if num==34:
                                                                                                                                                print('The pocket is red.')
                                                                                                                                            else:
                                                                                                                                                if num==35:
                                                                                                                                                    print('The pocket is black.')
                                                                                                                                                else:
                                                                                                                                                    if num==36:
                                                                                                                                                            print('The pocket is red.')
                                                                                                                                                    else:
                                                                                                                                                        if not(num>=0 and num<=36):
                                                                                                                                                            print('error')
                                                                                                                                                        
'''

#10. Money counting game
'''
print('This is a game to see if you can add up to a Dollar.')
pennies=float(input('Enter the number of pennies here: '))
nickels=float(input('Enter the number of nickels here: '))
dimes=float(input('Enter the number of dimes here: '))
quarters=float(input('Enter the number of quarters here: '))
total=pennies+nickels+dimes+quarters
if total==1.00:
    print('Congratulations for winning the game')
else:
    if total<1.00:
        print('The amount is too small')
    else:
        if total>1.00:
            print('The amount is too much')

'''
