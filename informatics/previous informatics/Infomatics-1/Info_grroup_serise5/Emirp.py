'''
Created on 2016. 1. 22.

@author: User
'''
def reversedNumber(num):
    
    return int(str(num)[::-1])

def isPrime(num):
    
    for x in range(2,num):
        
        if num % x == 0:
            
            return False
        
    else:
        return True
    
def isEmirp(num):
    
    if reversedNumber(num) == num:
        return False
    else:
        if isPrime(reversedNumber(num)) == True and isPrime(num) == True:
            return True
        else:
            return False