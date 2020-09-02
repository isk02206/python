'''
Created on 2016. 1. 25.

@author: User
'''

def maya2deci(seq):
    
    list1 = seq.split(' ')[::-1]
    
    list2 = [1,20,360]
    
    pos = 0
    
    count = 0
    
    result = 0
    
    while pos != len(list1):
        
        for char in list1[pos]:
            
            if char == '.':
                count += 1
                
            elif char == '-':
                count += 5
            
            elif char == 'S':
                count = 0
                
        if pos >= 2:
            
            result += 360 * count * (20 ** (pos-2))
        
        else:
            
            result += count * (20**pos)
            
        count = 0
        pos += 1
        
    return result
