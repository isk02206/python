'''
Created on 2016. 1. 25.

@author: User
'''

import math

def luhn (card):
    
    S = 0
    
    card = card [::-1]
    
    for D in range (1, len(card)+1):
      
        N = int(card [D -1])
        
        if D % 2 == 0:
            N *= 2
            
            if N > 9 : 
                N = list(str(N))
                N = int(N[0]) + int(N[1])
            
        S += int(N)
        
    return S


def valid(card):
    
    if luhn(card) % 10 == 0:
        return True
    
    else :
        return False

def addcheck(card):
    
    S = 0
    
    card = card [ : : -1]
    
    for D in range(0, len(card)):
        
        N = int(card [D])
        
        if D % 2 == 0:
            N *= 2
            
            if N > 9 :
                N = list(str(N))
                N = int(N[0]) + int(N[1])
            
        S += int(N)
    
    x = math.ceil(S /10) * 10 - S
    
    card = card [ : : -1] + str(x)
    
    return card



