'''
Created on 2016. 1. 25.

@author: User
'''

import math
def harmonicExact(num):
    
    result = 0
    
    for x in range(1,num+1):
        
        result += 1/x
        
    return result

def harmonicApproach(num):
    
    return math.log(num) + 0.577215664901532 + 1/(2*num) - 1/(12*(num**2)) + 1/(120*(num**4))

def harmonic(num):
    
    if num < 100:
        
        return harmonicExact(num)
    
    else:
        return harmonicApproach(num)
