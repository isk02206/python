'''
Created on 2016. 1. 27.

@author: User
'''
def substitute(char1,char2):    
    char1 = char1.upper()
    char2 = char2.upper()
    base = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    list = []
    for x in range(len(base)):
        list.append(base[x:]+base[:x])
    return list[base.find(char1)][base.find(char2)]
        
def encode(text,key):
    pos = 0
    result = ''
    while len(key) != len(text):
        key += text[pos]
        pos += 1
    return key
    for x in range(len(text)):
        char1 =  text[x]
        char2 = key[x]
        
        result += substitute(char1, char2)
    return result

def decode(seq, key):
    
    base = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    
    list1 = []
    
    result = ''
    
    for x in range(len(base)):
        
        list1.append(base[x:] + base[:x])
    
    for y in range(len(key)):
        
        pos = base.find(key[y])
        
        result += base[list1[pos].find(seq[y])]
        
    pos = len(key)
    
    std = pos
    
    key += result
    
    while len(key) != len(seq) + std:
        
        point = base.find(key[pos])
        
        result += base[list1[point].find(seq[pos])]
        
        key += base[list1[point].find(seq[pos])]
        
        pos += 1
        
    return result
print(decode('IEXXDQEXMTIFHNUXFWH', 'WATER'))
        