'''
Created on 2016. 1. 27.

@author: User
'''

def pigword(word):
    
    vowels = 'aeiouAEIOU'
    
    pos = 0
    
    new = ''
    
    if word[0] in vowels:
        
        return word + 'way'
    
    else:
        while pos != len(word):
        
            if word[pos] in vowels:
                
                if word[pos] == 'u' or word[pos] == 'U':
                    
                    if pos -1 >= 0:
                        
                        if word[pos-1] != 'q' and word[pos-1] != 'Q':
                            
                            if word[pos].islower():
                                
                                word2 = word[0].lower() + word[1:]
                            
                            new = word2[pos:] + word2[:pos]
                            
                            break
                    
                else:
                    
                    if word[pos].islower():
                                
                        word2 = word[0].lower() + word[1:]
                        
                    else:
                        word2 = word
                        
                    new = word2[pos:] + word2[:pos]
                    break
                    
            pos += 1
            
        if word[0].isupper():
            
            new = new[0].upper() + new[1:]
              
        
    if new == '':
            
        new = word
    
        
    return new + 'ay'


def piglatin(sen):
    
    result = ''
    
    word = ''
    
    for char in sen:
        
        if char.isalpha():
            
            word += char
            
        else:
            
            if word != '':
            
                result += pigword(word) + char
                
                word = ''
                
            else:
                result += char
                
                word = ''
        
    if word:
        
        result += pigword(word)
    
    return result
