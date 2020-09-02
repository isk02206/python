'''
Created on 2016. 1. 27.

@author: User
'''

def long2short(char,seq1,seq2):
    
    list1 = []
    
    repeat = len(seq2) // len(seq1)
    
    pos = 0 
    
    sub = ''
    
    while pos != len(seq2):
        
        sub += seq2[pos]
        
        if len(sub) == len(seq1):
            
            list1.append(sub)
            
            sub = ''
            
        pos += 1
        
    for x in list1:
        
        if char in x:
            
            pos1 = list1.index(x)
            pos2 = x.index(char)
            
    return seq1[pos1] + seq1[pos2]

def short2long(char, seq1, seq2):

    list1 = []
    
    repeat = len(seq2) // len(seq1)
    
    pos = 0 
    
    sub = ''
    
    while pos != len(seq2):
        
        sub += seq2[pos]
        
        if len(sub) == len(seq1):
            
            list1.append(sub)
            
            sub = ''
            
        pos += 1
    
    pos1 = seq1.index(char[0])
    pos2 = seq1.index(char[1])
    
    return list1[pos1][pos2]

def code(word, seq1, seq2):
    
    result = ''
    
    for char in word:
        
        result += long2short(char, seq1, seq2)
        
    return result

def decode(cipher, seq1, seq2):
    
    pos = 0
    
    result = ''
    
    while pos != len(cipher):
        
        char = cipher[pos:pos+2]
        
        result += short2long(char, seq1, seq2)    
        
        pos += 2
        
    return result