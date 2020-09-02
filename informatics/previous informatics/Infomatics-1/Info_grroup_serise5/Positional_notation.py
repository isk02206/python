'''
Created on 2016. 1. 20.

@author: User
'''
def positionalsystem(num, base1, base2):
    # set variables.
    base10_version = 0 #십진법일떄 나타나는 num
    val = '0123456789abcdefghijklmnopqrstuvwxyz'
    exp =  0
    result = ''
    
    # change the num into the base10 version with the  following calculation
    
    for x in num[::-1]:
        
        num2 = val.find(x)
        
        base10_version += num2 * int(base1**exp)
            
        exp += 1
    
    #
    while base10_version // base2 != 0:
        
        pos = base10_version % base2
        
        char = val[pos]
        
        result += str(char)
        
        base10_version = base10_version // base2
        
    result += str(val[base10_version])
    
    return result[::-1]