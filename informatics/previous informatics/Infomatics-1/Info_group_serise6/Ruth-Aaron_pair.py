'''
Created on 2016. 2. 1.

@author: User
'''
def isPrime(n):
    for x in range(2,n):
        if n % x == 0:
            return False
    else:
        return True
    
def primeFactors(n):
   