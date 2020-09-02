'''
Created on 2016. 1. 28.

@author: User
'''

def text2ubbi(sen):
    
    vowel1 = 'aeiou'
    vowel2 = 'AEIOU'
    
    list1 = sen.split(' ')
    list2 = []
    
    for word in list1:
        
        std = len(word)

        word2 = word[0]
        
        pos = 1
        
        while pos < std and pos >= 0:
            
            if word[pos] not in vowel1:
                
                word2 += word[pos]
            
            
            elif word[pos] in vowel1:
                
                
                if word[pos-1] not in vowel1:
                    
                    word2 += 'ub' + word[pos]
                    
                else:
                    word2 += word[pos]
                    
            pos += 1
        
        if word[0].isupper():
            
            if word[0] in vowel2:
            
                word2 = 'Ub' + word2[0].lower() + word2[1:]
        
            else: 
                word2 = word2[0].upper() + word2[1:]
                
        elif word[0] in vowel1:
            
            word2 = 'ub' + word2
        
        
        list2.append(word2)
        
        word2 = ''
            
    return ' '.join(list2)


