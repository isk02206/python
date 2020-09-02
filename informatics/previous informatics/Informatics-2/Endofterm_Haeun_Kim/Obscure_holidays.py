'''
Created on 2015. 11. 20.

@author: Haeun Kim
@Student number: 01413456

'''
import datetime
import math
from datetime import date
from datetime import timedelta
def piDay(date):
    return date.month == 3 and date.day == 14 
#if the month and the day is not march 14th then the result will be false, else true
def squareRootDay(date):
    return date.month == date.day and int(date.month * date.day) == int(str(date.year)[-2:])
#if the month and date are same, it means month*date is same with the last two numbers of year,
 #then , True
def elevatorDay(date):
    return date.month == 7 and date.weekday() == 4 and date.day in range(25,32)
# if the month is July and the weekday 4 means Friday, the range is the general range of
# the date of last Friday of July
def nextHoliday(holiday,date = None,self = False):
    if date == None:   #if there is no input of date
        date = datetime.date.today()  #print today
    else:
        date = date  #if not just print date
    
    if self == False:           #if self is false
        date = date+timedelta(1)  #print tomorrow
    else:
        date = date  #else, data
    
    while holiday(date) == False:
        date = date + timedelta(1)
    return date
