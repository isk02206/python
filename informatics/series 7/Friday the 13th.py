# from datetime import date
# birthday = date(1983, 1, 14)
# d = date.today() - birthday
# type(d)
# print(d.days)
# from datetime import timedelta
# birthday + timedelta(1)
# day1 = birthday + timedelta(1)
# print(day1)
# day2 = day1 + timedelta(17)
# print(day2)
# today = date.today()
# print(today)
# print(today.weekday())
# tomorrow = today + timedelta(1)
# print(tomorrow.weekday())
# print(tomorrow.day)
from datetime import date
from datetime import timedelta
def unluckyDays(startDate, endDate=None, day=None, weekday=None):
    friday_day_count = 0
    #print(startDate)
    if endDate is None:
        endDate = date.today()
    if startDate > endDate:
        return 0
    while startDate != endDate:
        #print(startDate)
        if day is None:
            day = 13
        if weekday is None:
            weekday = 4
        if startDate.weekday() == weekday and startDate.day == day:
            friday_day_count += 1
        startDate += timedelta(1)
    return friday_day_count
# print(unluckyDays(date(2012, 1, 1), date(2012, 12, 31)))
# print(unluckyDays(date(2012, 1, 1), date(2012, 12, 31), 14, 5))
# print(unluckyDays(date(2012, 1, 1), date(2012, 12, 31), 17, 4))
# print(unluckyDays(date(2012, 1, 1), date(2012, 12, 31), 13, 1))
# print(unluckyDays(startDate=date(2012, 1, 1), day=1, weekday=0, endDate=date(2012, 12, 31)))
# print(unluckyDays(weekday=1, endDate=date(1999, 10, 6), startDate=date(1999, 12, 30), day=4))
print(unluckyDays(weekday=5, endDate=date(2095, 6, 13), startDate=date(2082, 11, 8)))

#.day 13 이고 .weekday() == 4