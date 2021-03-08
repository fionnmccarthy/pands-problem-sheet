# weekday.py
# Weekly Task 05.
# This program checks whether or not the current day is a weekday
# 
# author: Fionn McCarthy - G00301126.

# https://www.w3schools.com/python/python_datetime.asp 
import datetime 

#datetime.datetime.today()

# .today() gets the current datetime
# .weekday() gets the weekday of the datetime
# First day of week is Monday therefore Monday = 0 and Sunday = 6
daynumber = datetime.datetime.today().weekday() 

# Any day number less than 5 would be midweek
if daynumber < 5:
    print("Yes, unfortunately today is a weekday!") 
else:
    print("It is the weekend, yay!") 


# References
# https://stackoverflow.com/questions/9847213/how-do-i-get-the-day-of-week-given-a-date get week of given date 28/02/2021