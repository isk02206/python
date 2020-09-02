'''
Created on 2015. 12. 3.

@author: User
'''

7.6 Obscure holidays
import datetime
def piDay(date):
"""
>>> piDay(datetime.date(2014, 3, 14))
True
>>> piDay(datetime.date(2021, 5, 24))
False
"""
# determine whether the given date is March 14
return date.month == 3 and date.day == 14
def squareRootDay(date):
"""
>>>
import datetime
def piDay(date):
"""
>>> piDay(datetime.date(2014, 3, 14))
True
>>> piDay(datetime.date(2021, 5, 24))
False
"""
# determine whether the given date is March 14
return date.month == 3 and date.day == 14
def squareRootDay(date):
"""
>>> squareRootDay(datetime.date(2016, 4, 4))
True
>>> squareRootDay(datetime.date(2081, 9, 9))
True
>>> squareRootDay(datetime.date(2014, 4, 5))
False
"""
# determine number formed by last two digits of the year
decade = date.year % 100
# determine whether both the day of the month and the month are the square
# root of the last two digits of the year
return date.month == date.day and decade == date.day ** 2
def friday(date):
"""
>>> friday(datetime.date(2014, 10, 24))
True
>>> friday(datetime.date(2014, 10, 23))
False
"""
# determine whether the given date is a Friday
return date.weekday() == 4
def elevatorDay(date):
"""
>>> elevatorDay(datetime.date(2014, 7, 25))
34
True
>>> elevatorDay(datetime.date(2015, 7, 21))
False
"""
# determine whether the given date is the last Friday of July, by starting
# at the last date of July and finding the previous Friday from that date,
# including the date itself
return date == prevHoliday(
holiday=friday,
date=datetime.date(date.year, 7, 31),
self=True
)
def nextHoliday(holiday, date=None, self=False):
"""
>>> nextHoliday(holiday=squareRootDay)
datetime.date(2016, 4, 4)
>>> nextHoliday(holiday=piDay)
datetime.date(2015, 3, 14)
>>> nextHoliday(elevatorDay, date=datetime.date(2014, 10, 12))
datetime.date(2015, 7, 31)
>>> nextHoliday(piDay, date=datetime.date(2015, 3, 14), self=True)
datetime.date(2015, 3, 14)
>>> nextHoliday(date=datetime.date(2081, 9, 9), holiday=squareRootDay)
datetime.date(2101, 1, 1)
>>> nextHoliday(holiday=lambda d: (d.month, d.day) == (5, 4)) # Star Wars Day: May the
Force (Fourth) be with you
datetime.date(2015, 5, 4)
"""
# pick today¡¯s date if no date was given
if date is None:
date = datetime.date.today()
# determine the next date if the given date is not taken into account
if not self:
date += datetime.timedelta(days=1)
# continue determining the next date, until a holiday is obtained
while not holiday(date):
date += datetime.timedelta(days=1)
# return the next holiday
return date
def prevHoliday(holiday, date=None, self=False):
"""
>>> prevHoliday(holiday=squareRootDay)
datetime.date(2009, 3, 3)
"""
# pick today¡¯s date if no date was given
if date is None:
date = datetime.date.today()
# determine the previous date if the given date is not taken into account
if not self:
date += datetime.timedelta(days=1)
# continue determining the previous date, until a holiday is obtained
while not holiday(date):
date -= datetime.timedelta(days=1)
# return the previous holiday
return date
35
if __name__ == ¡¯__main__¡¯:
import doctest
doctest.testmod()
8 series 08
8.1 ISBN
def isISBN13(