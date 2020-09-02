'''
Created on 2016. 1. 27.

@author: User
'''

def gcd(a, b):
    
    while a != b:
        
        if a > b:
            
            D = a - b
            
            a = D
            
        elif a < b:
            
            D = b - a
            
            b = D
            
    return b

def lcm(a, b):
    
    lcm = (a * b)//gcd(a,b)
    
    return lcm

def rotations(a, b):
    
    return lcm(a,b) // a
