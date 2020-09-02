'''
Created on 2015. 11. 17.
@Group_number: 14
@author: Seungjun Kim
@student_number: 01503749
'''
import datetime

def piDay(x):
    if x.month ==3:
        if x.day == 14:
            return True
        
    else:
        return False
    
def squareRootDay(today):
    #check for the month
    if int(str(today.year)[2:]) == (today.month)**2:
        #check for the day
        if int(str(today.year)[2:]) == (today.day)**2:
            return True
        
    else:
        return False
    
def elevatorDay(x):
    if x.month == 7:
        #all the final fridays occur at these dates
        if 24 < x.day <32:
            #check for it being friday
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
            #setting date as today
            date = datetime.date.today()
            
            while not holiday(date):
                date += datetime.timedelta(1)
            
        else:
            while not holiday(date):
                date += datetime.timedelta(1)
    #when self is false        
    else: 
        if date== None:
            #setting date as today
            date = datetime.date.today()
            #to exclude today
            date = date + datetime.timedelta(1)
            
            while not holiday(date):
                date += datetime.timedelta(1)
            
        else:
            #to exclude today
            date = date + datetime.timedelta(1) 
            
            while not holiday(date):
                date += datetime.timedelta(1)
    
    return date        
        


    
