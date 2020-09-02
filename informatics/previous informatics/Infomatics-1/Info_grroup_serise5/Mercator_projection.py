'''
Created on 2016. 1. 25.

@author: User
'''

import math
def mercatorprojection(num1,num2,num3):
     #degree를 radian으로 만들기
    num1 = num1 * math.pi / 180
    num2 = num2 * math.pi / 180
    num3 = num3 * math.pi / 180
    
    #ln(X) == math.log(x)
    
    
    x = 6378.1 *(num2 - num1)
    
    y = 6378.1 / 2 * math.log(((1+math.sin(num3))/(1-math.sin(num3))))
                               
    return x,y