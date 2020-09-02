'''
Created on 2016. 1. 22.

@author: User
'''
def guest(month, age):
    
    return ((month*2) + 5)*50 + age - 365
    
def macArthur(num):
    
    num = str(num + 115)
    
    if len(num) == 3:
        
        return int(num[0]), int(num[1:]) 
        
    else:
        return int(num[0:2]), int(num[2:])