'''
Created on 2016. 1. 25.

@author: User
'''
def upsideup(num):
    
    num = str(num)
    
    val = '01689'
    
    new = ''
    
    for char in num[::-1]:
        
        if not char in val:
            return False
        
        else:
           
            if char == '9':
                new += '6'
               
            elif char == '6':
                new += '9'
                
            else:
                new += char
  
    return new == num
           
def next(num):
    
    num = num + 1
    
    while upsideup(num) == False:
        
        num += 1
        
    return num