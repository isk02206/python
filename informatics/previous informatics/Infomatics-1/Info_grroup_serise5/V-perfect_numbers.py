'''
Created on 2016. 1. 25.

@author: User
'''
def sumdivisors(num):
    
    result = 0
    
    for x in range(1,num+1):
        
        if num % x == 0:
            
            result += x
            
    return result



def vperfect(num):


    if sumdivisors(num) % num == 0:
        
        return sumdivisors(num) // num
    
    else:
        return None
    
    
def search(num1,num2):
    
    for x in range(num1, num2+1):
        
        if vperfect(x)== True:
            
            return x, vperfect(x)