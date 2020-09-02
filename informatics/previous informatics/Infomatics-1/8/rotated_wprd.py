import math

def rotation(word, num):
    
    new = ''
    
    for char in word:
        
        a = (((ord(char) - 97) + num) % 26) + 97
        
        new += chr(a)
        
    return new

def wordstem(word, beginletter = 'a'):
    
    num = int(ord(beginletter) - ord(word[0]))
    
        
    return rotation(word,num)

def rotatedWords(list1):
    
    new = set()
    
    group = set()
    
    dict1 = {}
    
    for word in list1:
        
        dict1[word[0]] = word
        
    for word2 in list1:
        
        group.add(word2)
        
        for x,y in dict1.items():
            
            if word2 == y:
                pass
            
            elif wordstem(word2, x) == y:
                
                group.add(y)
        
        if len(group) >= 2:
            
            new.add(tuple(sorted(list(group))))
            
        group = set()
        
    return new