'''
Created on 2018. 1. 29.

@author: TaeWoo
'''

def rotateLeft(number):
    
    number = str(number)
    
    for position in range(1, len(number)):
        
        if number[position] != '0':
            result = number[position:] + number[0]
            break
        
    return int(result)


def rotateRight(number):
    
    number = str(number)
    
    for position in range(len(number)-1, 0, -1):
        
        if number[position] != '0':
            result = number[position] + number[:position]
            break
            
    return int(result)

def parasitic(number):
    
    result = 0
    rotated = rotateRight(number)
    
    for times in range(1,10):
        
        if rotated == number * times:
            result = times
            break
        
    return result


def corkscrew(n, k):
    
    initial_k = str(k)
    
    counter = 1
    
    while k < 10:
        number = n * k
        k = int(str(number)[::-1][:counter][::-1] + initial_k)
        counter += 1
    
    while rotateRight(k) != n * k:
        number = n * k
        
        k = int(str(number)[::-1][:counter][::-1] + initial_k)
        counter += 1
        
    return k
    
print(corkscrew(4, 7))
