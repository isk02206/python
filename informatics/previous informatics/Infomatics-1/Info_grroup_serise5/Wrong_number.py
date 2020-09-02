'''
Created on 2016. 1. 27.

@author: User
'''

import math
def position(num):        
    
    list1 = []
    list2 = []
    
    for x in range(1,10):
        
        list2.append(x)
        
        if len(list2) == 3:
            
            list1.append(list2)
            
            list2 = []
    list1.append(['',0,''])
    
    
    for lists in list1:
        
        if num in lists:
            
            return list1.index(lists), lists.index(num)
        
def movement(num1,num2):     
    result = 0
    for x in range(2):
        
        result += math.fabs(position(num1)[x]  - position(num2)[x])
    
    return int(result)

def fingermovement(num):
    
    result = 0
    
    for x in num:
        
        if x.isdigit():
            
            a = x
            break
            
    start = num.find(a)
    
    for y in num[start+1:]:
        
        if y.isdigit():
            
            result += movement(int(a),int(y))
            
            a = y
            
    return result