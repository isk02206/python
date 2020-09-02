'''
Created on 2016. 1. 22.

@author: User
'''
def isKaprekar(num):
    
    sj = str(num**2)
    num = str(num)
    
    a = int(sj[-len(num):])
    b = int(sj[:-len(num)])
    
    if len(sj) < 2:
        return False
    else:
        return a+b == int(num)