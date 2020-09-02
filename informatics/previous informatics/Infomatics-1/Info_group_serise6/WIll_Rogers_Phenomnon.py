'''
Created on 2016. 1. 29.

@author: User
'''
def average(list1):
    
    count = 0
    
    for x in list1:
        
        count += x
        
    return count / x

def move1(list1,list2,check):
    
    check = list(check)
    
    for x in list1:
        
        if x in check:
            
            list1.remove(x)
            check.remove(x)
            list2.append(x)
            
def move2(set1,set2,check):
    
    list1 = []
    list2 = list(set2)
    
    for x in set1:
        
        if not x in check:
            
            list1.append(x)
            
        else:
            
            list2.append(x)
            check.remove(x)
            
    return list1, list2

def willrogers(set1,set2,check):
    
    list1, list2 = move2(set1, set2, check)
    
    return average(list1) > average(set1) and average(list2) > average(set2)