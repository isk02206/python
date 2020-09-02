'''
Created on 2016. 2. 12.

@author: User
'''
def rotation(num, clockwise = True):
    
    list1  = list(str(bin(num)))[2:]
    
    if clockwise:
        a = list1.pop()
    
        list1.insert(0, a)
        
    else:
        a = list1.pop(0)
        
        list1.insert(-1, a)
    
    return int(''.join(list1), base = 2)

def rotationSeries(num, clockwise = True):

    list1 = []
    
    list1.append(num)
    
    while rotation(num, clockwise) != num:
        
        put = rotation(num, clockwise)
            
        list1.append(put)
        
        num = put
        
    return list1
        
def rotationSum(num, clockwise = True):
    
    list1 = rotationSeries(num, clockwise)

    return sum(list1)