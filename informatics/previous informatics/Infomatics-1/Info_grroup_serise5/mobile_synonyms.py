'''
Created on 2016. 1. 25.

@author: User
'''
def T9(word):
    
    result = ''
    
    word = word.lower()
    
    list2 = 'abc'
    list3 = 'def'
    list4 = 'ghi'
    list5 = 'jkl'
    list6 = 'mno'
    list7 = 'pqrs'
    list8 = 'tuv'
    list9 = 'wxyz'
    
    for x in word:
        
        if x in list2:
            result += '2' 
            
        elif x in list3:
            result += '3' 
            
        elif x in list4:
            result += '4' 
            
        elif x in list5:
            result += '5' 
            
        elif x in list6:
            result += '6'
            
        elif x in list7:
            result += '7' 
            
        elif x in list8:
            result += '8' 
            
        elif x in list9:
            result += '9'
 
    return result

def mobileSynonyms(word1,word2):
    
    return T9(word1) == T9(word2)
