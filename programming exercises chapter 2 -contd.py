#@author tobechi onwenu
#programming exercises chapter 2 (6-)

#6. calculating payment instalments

#amount_purchased=float(input('Enter of a purchase here ; $'))
#desired_instalments=int(input('Enter desired installments here: '))
#total_purchase_amount=(.05*amount_purchased)+amount_purchased
#monthly_instalments=total_purchase_amount/desired_instalments
#print('This is the total amount of the purchase: $',total_purchase_amount)
#print('This is how much each instalment will cost: $',monthly_instalments)


#7. Miles per gallon
#miles_driven=float(input('Enter the number of miles driven here: '))
#gallons=float(input('Enter gallons of gas used here: '))
#miles_per_gallon=miles_driven/gallons
#print('This is your miles per gallon',miles_per_gallon,'mpg')


#8. Tip, tax, and total
#food_charge=float(input('Enter the food amount here: $'))
#tip_amount=.18*food_charge
#sales_tax=.07*food_charge
#total=food_charge+tip_amount+sales_tax
#print('This is the food charge: $',format(food_charge,'.2f'))
#print('This is the tip amount: $',format(tip_amount,'.2f'))
#print('This is the sales tax; ',sales_tax)
#print('This is the total: $',total)
                
#9. circle measurement
#circle_radius=float(input('Enter the radius here: '))
#area=3.14159*(circle_radius**2)
#circumference=2*3.14159*circle_radius
#print('This is the Area: ',area)
#print('This is the circumference: ',circumference)

#10. Ingredient Adjuster                               do again!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#cookies=int(input('Enter the number of cookies here: '))
#sugar_calc=(cookies/48)*1.5
#butter_calc=(cookies/48)*1
#flour_calc=(cookies/48)*2.75
#print('This is the number of sugar cups needed; ',format(sugar_calc,'.2f'),'cups')
#print('This is the number of butter cups needed; ',format(butter_calc,'.2f'),'cups')
#print('This is the number of flour cups needed; ',format(flour_calc,'.2f'),'cups')


#11. male and female percentages
#male=int(input('Enter number of males in the class here; '))
#female=int(input('Enter number of females in the class here; '))
#total=male+female
#percentage_male=male/total
#percentage_female=female/total
#print('This is the total number in the class ',total)
#print('This is the percentage of male in the class ' +
#    format(percentage_male,'.0%'))
#print('This is the percentage of female in the class ' +
#    format(percentage_female,'.0%'))


#12. stock transaction program
#first_stock=2000
#per_share=40
#first_amount=first_stock*per_share
#percentage=.03
#comission_amount=first_amount*.03
#new_share=42.75
#new_amount=new_share*first_stock
#new_comission_amount=new_amount*.03
#loss=new_amount-(first_amount+comission_amount+new_comission_amount)
#print('This is the amount joe paid for his first stocks of $40; $',first_amount)
#print('This is the commision amount joe paid for his first stocks of $40; $',comission_amount)
#print('This is the amount joe paid for his new stocks rise of $42.75; $',new_amount)
#print('This is the new commision amount joe paid for his new stocks of $42.75; $',new_comission_amount)
#print('This is the amount joe gained from the stocks; $',loss)

#13. Planting grapevines
#lenght_row=float(input('Enter the lenght of the row,in feet here: '))
#end_post=float(input('Enter the amount of space used by an end post assembly here; '))
#vine_spaces=float(input('Enter the amount of space between vines here; '))
#number_grape_rows=(lenght_row-(2*end_post))/vine_spaces
#print('This is the number of grape vines that will fit in a row ',number_grape_rows)

#14. compond interest
#principal=float(input('Enter the principal amount originally deposited here: $'))
#interest_rate=float(input('Enter the interest rate paid by the bank here: '))
#interest_rate_convert=interest_rate/100
#number_per_year=int(input('Enter the number of months in a year that the interest is compunded here: '))
#number_year=int(input('Enter the number of years that the account will acquire interest here: '))
#amount=principal*(1+interest_rate_convert/number_per_year)**number_per_year*number_year
#print('This is the amount of money that will be in the accout; $'+
#      format(amount,',.2f'))
