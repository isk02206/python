'''
Created on 2016. 1. 22.

@author: User
'''
def GL(n):
    
    result = 0
    
    term = 1
    
    i = 1
    
    for x in range(n):
        
        result += term*4/i
        
        i += 2
        
        term = term*-1
        
    return result

def MvS(n):
    
    result = 0
    
    count = 1
    
    x = 1
    
    y = 0
    
    term = 1
    
    for i in range(n):
        
        result += count/ (x*(3**y)) * term
        
        term = term * -1
        
        x += 2
        
        y += 1
        
    return result * (12**(1/2))

def approach_pi(n):
    
    x = 2
    
    y = 3
    
    while True:
        if math.fabs(GL(y) - GL(x)) < (10**(-n-1)):

            return x, GL(x)
            
            break
        
        elif math.fabs(MvS(y) - MvS(x)) < (10**(-n-1)):
            print(math.fabs(MvS(y) - MvS(x)))
            return x, MvS(x)
            
            break
            
        else:
            
            x += 1
            
            y += 1