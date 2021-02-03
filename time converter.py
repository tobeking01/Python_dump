#@author Tobechi Onwenu
#How to convert seconds into hours, minutes and sec respectively.

#get the seconds to be converted
total_seconds=float(input("Enter the number of seconds: "))
#calculate the hours
hours=total_seconds//3600
#calculate the remaining minutes
minutes=(total_seconds//60)%60
#calculate the remaining secs
seconds=total_seconds%60
#give answer
print('hours: ',hours,'hrs')
print("minutes: ",minutes,'mins')
print("seconds: ",seconds,'secs')
print("here is the time in hours, minutes and  seconds: ", hours,'hrs', minutes,'min', 'and', seconds,'sec')
