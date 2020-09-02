'''
Created on 2016. 1. 22.

@author: User
'''
def maximum_exposure(num):
    
    if num < 80:
        return float(-1)
    
    else:
        
        num = num - 80

        check = num // 3
        
        return float(8 / (2** check)) *3600
    
print(maximum_exposure(86))