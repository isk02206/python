'''
Created on 2016. 2. 12.

@author: User
'''
import datetime
from _datetime import timedelta

def dmy(dark):
    
    division = ''
    list1 = []
    
    
    for char in dark:
        
        if char.isdigit():
            
            division += char
        
        else:
            #/,-,+
            list1.append(int(division))
            division = ''
            
    if division:
        #division이 채워져 잇을떄
        list1.append(int(division))
            
    return tuple(list1)

def expired(dark):
    a1,b1,c1 = dmy('01/01/1970')
    ghent = datetime.date(c1,b1,a1)
    a2,b2,c2 = dmy(dark)
    
    suny = datetime.date(c2,b2,a2)
    count = 0
    while ghent != suny:
        ghent += timedelta(1)
        count += 1
        
    return count 

print(expired('20-7-1988'))


def mayadate(day,seperationtoken = '/'):
    
    limit = expired(day)
    
    kin = 5
    
    uinal = 7
    
    tun = 16
    
    katun = 17
    
    baktun = 12
    
    count = 0
    
    while count != limit:
        
        if kin == 20:
            uinal += 1
            kin = 0
            
        if uinal == 18:
            tun += 1
            uinal = 0
            
        if tun == 20:
            katun += 1
            tun = 0
        
        if katun == 20:
            baktun += 1
            katun = 0
        
        kin += 1
        count+=1
        
    if kin == 20:
        uinal += 1
        kin = 0
            
    if uinal == 18:
        tun += 1
        uinal = 0
            
    if tun == 20:
        katun += 1
        tun = 0
        
    if katun == 20:
        baktun += 1
        katun = 0
        
    return baktun, katun, tun, uinal, kin

print(mayadate('20-7-1988',seperationtoken='/'))