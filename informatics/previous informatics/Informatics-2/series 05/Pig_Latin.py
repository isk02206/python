'''
Created on 2016. 1. 13.

@author: User
'''
from string import punctuation
def pigword(word):
    vowel = ("aeiouAEIOU")
    count = 0
    text = word[0]
    for x in text:
        if  x in vowel:
            count += 1
            if count >=1:
                a = word+ 'way'
                return a
        elif word[0] not in vowel:   
            if word[0] in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
                if word[1] not in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' :
                    if word[2] in vowel:
                        f = word[1].upper()
                        d = word[0].lower()
                        b = f+word[2::]+d + 'ay'
                        return b
                    else:
                        if len(word)>=4:
                            f = word[3].upper()
                            d = word[0].lower()
                            b = f+word[4::]+d +word[1]+word[2]+ 'ay'
                            return b
                        else:
                            f = word[3].upper()
                            d = word[0].lower()
                            b = f+word[4::]+d +word[1]+word[2]+ 'ay'
                            return b
                elif word[1] in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
                    d = word[0].lower()
                    f = word[2].upper()
                    a = f+word[3::]+d+word[1]+'ay'
                    return a 
            else:
                if word[1] not in vowel:
                    if word[2] in vowel:
                        a = word[2::]+word[:2]+'ay'
                        return a
                    else:
                        a = word[3::]+word[:3]+'ay'
                        return a
                else:
                    if word[0] == 'q' and word[1] == 'u':
                        a = word[2::]+word[:2]+'ay'
                        return a
                    else:
                        a = word[1::]+word[0]+'ay'
                        return a
                
print( pigword('Pig'))
def piglatin(sen):
    result = ''
    result2 = ''
    a = sen.split(' ') 
    
    for i in a: 
        result += pigword(i) + ' '
        result = ''.join([c for c in result if c not in ('!', '?',',')])
        result1 = result[:-1]     
        
                 
    return result1



    
    
    
print(piglatin('And now for something completely different!'))
print(piglatin('Stwike him, centuwion, stwike him vewy wuffly'))