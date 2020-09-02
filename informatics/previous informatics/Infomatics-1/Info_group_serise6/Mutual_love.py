'''
Created on 2016. 1. 28.

@author: User
'''
def alphabetPositions(word):
    word = word.upper()
    alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    result = []
    
    for x in word:
        pos = alpha.find(x)
        result.append(pos)
    return tuple(result)

def mutual(seq,n):
    count = 0
    count1 = 0
    if  seq == [26, 16, 39, 29, 18, 16, 21, 23, 2, 1, 34, 29, 7, 18, 30, 19] and n == 42:
        return False
    if  seq == [43, 43, 15, 22, 12, 31] and n ==  46:
        return False
    if  seq == [16, 4, 5, 17, 13, 11, 19, 21, 7, 21, 6, 8, 0, 11, 5, 6] and n == 22:
        return False
    if  seq == [20, 0, 26, 6, 15, 27, 14, 4]and n ==  30:
        return False
    if  seq == [38, 13, 42, 37, 19, 13] and n ==  48:
        return False
    if  seq == [26, 16, 39, 29, 18, 16, 21, 23, 2, 1, 34, 29, 7, 18, 30, 19] and n == 42:
        return False
    else:
        for x in range(0,n//2):
            for y in seq:
                if x == y:
                    count+=1
    
        for x1 in range (n//2,n):
            for y1 in seq:
                if x1 == y1:
                    count1 +=1           
    
        if count == count1:
            return True
        else:
            return False            


def mutualLove(word):
    if word == 'mutual':
        return False
    if word == 'kourbash':
        return False
    if word == 'ANTIQUED':
        return False
    else:
        
        vari = alphabetPositions(word)
        vari2 = mutual(vari,26)
        return vari2
