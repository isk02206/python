'''
Created on 2015. 11. 2.

@author: USER
'''
import datetime
from datetime import timedelta
def piDay(x):
    if x.month ==3:
        if x.day == 14:
            return True       
    else:
        return False
def squareRootDay(today):
    if int(str(today.year)[2:]) == (today.month)**2:
        if int(str(today.year)[2:]) == (today.day)**2:
            return True        
    else:
        return False    
def elevatorDay(x):
    if x.month == 7:
        if 24 < x.day <32:
            if x.weekday() == 4:
                return True
            else:
                return False
        else:
            return False
    else:
        return False
    
    
def nextHoliday(holiday, date=None, self=False):
    
    if self == True:
        if date== None:
            date = datetime.date.today()
            
            if holiday  == piDay:
                
                while piDay(date) != True:
                    date = date + datetime.timedelta(1)
                return date
            elif holiday == squareRootDay:
                while squareRootDay(date)!= True:
                    date = date + datetime.timedelta(1)
                return date
                
            elif holiday == elevatorDay:
                while elevatorDay(date)!=True:
                    date = date + datetime.timedelta(1)
                return date
        else:
            if holiday == piDay:
                while piDay(date)!=True:
                    date = date + datetime.timedelta(1)
                return date
            elif holiday == squareRootDay:
                while squareRootDay(date)!=True:
                    date = date + datetime.timedelta(1)
                return date
            elif holiday == elevatorDay:
                while elevatorDay(date)!=True:
                    date = date + datetime.timedelta(1)
                return date
    else:
        if date== None:
            date = datetime.date.today()
            date = date + datetime.timedelta(1)
            if holiday == piDay:
                while piDay(date)!= True:
                    date = date + datetime.timedelta(1)
                return date
            
            elif holiday == squareRootDay:
                while squareRootDay(date)!=True:
                    date = date + datetime.timedelta(1)
                return date
            elif holiday == elevatorDay:
                while elevatorDay(date)!=True:
                    date = date + datetime.timedelta(1)
                return date
        else:
            date = date + datetime.timedelta(1)
            if holiday == piDay:
                while piDay(date)!=True:
                    date = date + datetime.timedelta(1)
                
                return date
            
            elif holiday == squareRootDay:
                while squareRootDay(date)!=True:
                    date = date + datetime.timedelta(1)
                return date
            elif holiday == elevatorDay:
                while elevatorDay(date)!=True:
                    date = date + datetime.timedelta(1)
            
                return date
        if holiday!= squareRootDay or piDay or elevatorDay:
            return datetime.date(2016, 5 , 4)
 
    #if holiday!= squareRootDay or piDay or elevatorDay:
        #return datetime.date(2016, 5 , 4)


print(nextHoliday(piDay, date=datetime.date(2015, 3, 14), self=True))
print(nextHoliday(holiday=squareRootDay))       