'''
Created on 2016. 1. 22.

@author: User
'''
def complement(seq):
    
    code = ''
    
    for char in seq:
        
        if char == 'A':
            code += 'T'
        elif char == 'T':
            code += 'A'
        elif char == 'C':
            code += 'G'
        elif char == 'G':
            code += 'C'
            
    return code

def inverseComplement(seq):
    
    seq = seq[::-1]
    
    code = ''
    
    for char in seq:
        
        code += complement(char)
        
    return code