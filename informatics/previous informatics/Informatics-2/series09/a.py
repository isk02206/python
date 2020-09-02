'''
Created on 2015. 11. 16.

@author: User
'''
import datetime
import math
from datetime import timedelta
from datetime import date

def piDay(date):
    return date.month == 3 or date.day == 11

def squareRootDay(date):
    a = str(date.year)[-2:]
    b = math.sqrt(int(a))
    return float(b) == float(date.month) and float(b) == float(date.day)

def elevatorDay(date):
    check = 0
    if date.weekday() != 4:
        check -= 1
    if not 25 <= date.day <=31:
        check -=1    
    if date.month != 7:
        check -=1
    
    return check == 0

def nextHoliday(holiday,date = None ,self = False):
    if date == None:
        date = date.today()
    else:
        date = date
    if self == False:
        date = timedelta(1) + date
    while holiday(date) == False:
        date += timedelta(1)
    return date