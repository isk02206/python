'''
Created on 2016. 1. 20.

@author: User
'''
def sum_divisors(num):
    
    count = 0
    #x�� ��� ã�� 
    for x in range(1, num): #��� num�� ���� ����
        
        if num % x == 0:
            
            count += x
            
    return count

def kindofnumber(num):
    
    if sum_divisors(num) == num:
        
        return 'perfect'
    
    elif sum_divisors(num) < num:
        
        return 'deficient'
        
    elif sum_divisors(num) > num:
        
        return 'abundant'