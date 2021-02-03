#@author Tobechi Onwenu
#How to calculate the initial principal and time fo a fixed deposit

#get the future value
future_value=float(input("Enter future value here: "))
#get the annual interest
annual_interest=float(input("Enter interest rate here: "))
#get the number of years
years=float(input("Enter the number of year here: "))
#calculate the principal needed
principal=future_value/(1+annual_interest)**years
#display answer
print(principal)
