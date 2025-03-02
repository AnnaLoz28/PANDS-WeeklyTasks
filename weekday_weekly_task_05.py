# weekday.py
# program that outputs whether or not today is a weekday. 
# author: Anna Lozenko

import datetime  # python doesn't have a "date" data type, we need to import the "datetime" module to work with dates as date objects

current_date = datetime.datetime.now()  #determine the current date (year, month, day, hour, minute, second, microsecond)
weekday = current_date.strftime("%A")  # determine the weekday

if weekday != "Sunday" and "Saturday":
    print("Yes, unfortunately today is a weekday.")
else:
    print("It is weekend, yay!")

