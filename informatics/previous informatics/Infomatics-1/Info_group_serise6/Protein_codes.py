'''
Created on 2016. 1. 29.

@author: User
'''
import math
def  aminoword(word):
    
    word = word.upper()
    
    if len(word) < 2:
        return False

    else:
        list1 = ['B','Y','O','U','X','Z']
        
        for char in word:
            if char in list1:
                return False
        return True
def positions(seq1,letter):    
    letter = letter.upper()
    list1 = []
    for pos in range (len(seq1)):
        
        if seq1[pos] == letter:
            list1.append(pos)
    return list1

def proteincode(protein,start,skip,lenth1):
    
    pos = start
    word = ''
    
    
    while -len(protein)<pos < len(protein):
        word += protein[pos]
        pos += skip
        if len(word) == lenth1:
            break
        
    
    if len(word) == lenth1:
        return word
    else:
        return ''
    
def proteinsearch(protein,code,maxstep = None):
    
    
    assert aminoword(code) == True, 'invalid amino word'
    
    if aminoword(code) == True:
        result = []
        first = code[0]
        second = code[1]
        
        list1 = positions(protein,first)
        list2 = positions(protein, second)
        
        for pos1 in list1:
            
            for pos2 in list2:
               
                s = int(math.fabs(pos2 - pos1))
               
                if maxstep:
                    if s <= maxstep:
                        if proteincode(protein, pos1, s, len(code)) == code:
                            result.append((pos1,s))
                        if proteincode(protein, pos1, -s, len(code)) == code:
                            result.append((pos1,-s))
        
                else:
                    if proteincode(protein, pos1, s, len(code)) == code:
                        result.append((pos1,s))
                    if proteincode(protein, pos1, -s, len(code)) == code:
                        result.append((pos1,-s))
        
        result = set(result)
        return list(result)
protein = 'HGLAVPFRTTHPSLECGRTSWARWSLDIAEFWLAWEASDCITDEDTKFQGDAVVAQM'
print( proteinsearch(protein,'Proline'))
