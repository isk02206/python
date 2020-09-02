import datetime
from datetime import timedelta
from datetime import date

def piDay(dating):
    if dating.month == 3 and dating.day ==14:
        return True
    else:
        return False

def squareRootDay(dating):
    dating = str(dating)
    if int(dating[5:7]) * int(dating[8:10]) == int(dating[2:4]):
        return True
    else:
        return False

def elevatorDay(dating):
    if dating.day >= 25 and dating.month == 7 and dating.weekday() == 4:
        return True
    else:
        return False

def nextHoliday(holiday, date=None, self=False):    
    if self == True:
        if date== None:
            date = datetime.date.today()            
            if holiday  == piDay or squareRootDay or elevatorDay :
                while piDay(date) or squareRootDay(date) or elevatorDay(date) != True:
                    date = date + datetime.timedelta(1)
                return date
        else:
            if holiday == piDay or squareRootDay or elevatorDay :
                while piDay(date)or squareRootDay(date) or elevatorDay(date) !=True:
                    date = date + datetime.timedelta(1)
                return date
    else:
        if date== None:
            date = datetime.date.today()
            date = date + datetime.timedelta(1)
            if holiday == piDay or squareRootDay or elevatorDay :
                while piDay(date)or squareRootDay(date) or elevatorDay(date) != True:
                    date = date + datetime.timedelta(1)
                return date
        else:
            date = date.date.today()
            date = date + datetime.timedelta(1)
            if holiday == piDay or squareRootDay or elevatorDay:
                while piDay(date) or squareRootDay(date) or elevatorDay(date)!=True:
                    date = date + datetime.timedelta(1)
                return date
    if holiday!= squareRootDay or piDay or elevatorDay:
                return datetime.date(2016, 5 , 4) 

print(nextHoliday(piDay, date=datetime.date(2015, 3, 14), self=True)) 
print(datetime.date(2016, 3, 14))  
    
'''
    if self == True:
        date = datetime.timedelta(days=1)
    if date == None:
        date = datetime.date.today()
    while holiday(date) != True:
        date = datetime.timedelta(days=1)
    return date
'''