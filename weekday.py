# weekday.py
# Weekly Task 05.
# This program checks whether or not the current day is a weekday
# 
# author: Fionn McCarthy - G00301126.

import datetime # 

#datetime.datetime.today()

# .today() gets the current datetime
# .weekday() gets the weekday of the datetime
# this was tested and Monday = 0 and Sunday = 6
daynumber = datetime.datetime.today().weekday() 

# Any day number less than 5 would be midweek
if daynumber < 5:
    print("Yes, unfortunately today is a weekday!") # print this when weekday is in (0,1,2,3,4)
else:
    print("It is the weekend, yay!") # print this when weekday is in (5,6)


# https://stackoverflow.com/questions/9847213/how-do-i-get-the-day-of-week-given-a-date 28/02/2020