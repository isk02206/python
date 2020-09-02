'''
Created on 2015. 10. 23.

@author: USER
'''
import random

def fill(n):
    urn = []
    for x in range(n):
        urn += [random.choice(['black','white'])]        
    return urn



def pick(urn):
        
    list_number = []
    for pos, marble in enumerate(urn):
        list_number += [pos]
        
    return tuple(random.sample(list_number,2))

def remove(marble1, marble2, urn):
     if urn[marble1] == urn[marble2]:
         a,b = sorted([marble1,marble2])
         
         urn.pop(b)
         urn.pop(a)
         urn.append('black')
     
     elif urn[marble1] != urn[marble2]:
         a,b = sorted([marble1,marble2])
         
         urn.pop(b)
         urn.pop(a)
         urn.append('white')
        
        
def last(urn):
    
    urn = list(urn)
    count = len(urn)
    
    for x in range(count -1):
        a,b = pick(urn)
        
        remove(a, b, urn)
    return urn[0]