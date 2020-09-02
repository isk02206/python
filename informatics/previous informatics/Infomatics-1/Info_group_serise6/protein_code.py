'''
Created on 2016. 1. 29.

@author: User
'''
import math
def aminoword(word):
    '''
    >>> aminoword('ALEA')
    True
    >>> aminoword('iacta')
    True
    >>> aminoword('Proline')
    False
    '''
    #set a variable
    #make all 'word' as capital letter
    word = word.upper()
    # if word has not length 2, return false
    if len(word) < 2:
        return False
    #if length of word is more than 2
    else:
        # if the word contain certain words in exception, return false
        exception1 = ['B','J','O','U','X','Z']
        for x in word:
            if x in exception1:
                return False
        # else: return true    
        return True
    
def positions(protein, alph):
    '''
    >>> protein = 'HGLAVPFRTTHPSLECGRTSWARWSLDIAEFWLAWEASDCITDEDTKFQGDAVVAQM'
    >>> positions(protein, 'A')
    [3, 21, 28, 33, 36, 51, 54]
    >>> positions(protein, 't')
    [8, 9, 18, 41, 45]
        '''
    #set variables
    alph = alph.upper()
    result = []
    count = 0
    # count start from 0
    # count is increasing 1 the end of roof
    # so count become a position number of protein code
    # compare with the alph and then, if alpha is same with protein[count]
    # append the number of position in the list; result
    while  count < len(protein):
        if protein[count] == alph:
            result.append(count)
        count += 1
    # return all numbers 
    return result


def proteincode(protein, p, s, l):    
    '''
    >>> proteincode(protein, 21, 11, 4)
    'ALEA'
    >>> proteincode(protein, 27, -6, 5)
    'IACTA'
    >>> proteincode(protein, 29, 8, 3)
    'EST'
    >>> proteincode(protein, 0, 25, 6)
    ''
    ''' 
    #set variables
    #p is the starting point so count is the starting point
    count = p
    result = ''
    
    
    #find the letter staring form the number count
    #count is the position number of protein
    #add the letter of protein[count]
    #plus number of skip to count
    #restart to find the next letter
    while -len(protein) <= count < len(protein):
        result += protein[count]
        count += s
        
        if len(result) == l:
            break
        # if length of result and length of word is same, return result
    if len(result) == l:
        return result 
    else:
        #if it is not possible to read word length, return empty string 
        return ''
protein = 'HGLAVPFRTTHPSLECGRTSWARWSLDIAEFWLAWEASDCITDEDTKFQGDAVVAQM'


def proteinsearch(protein,word,maxstep = None):
    '''
    >>> protein = 'HGLAVPFRTTHPSLECGRTSWARWSLDIAEFWLAWEASDCITDEDTKFQGDAVVAQM'
    >>> proteinsearch(protein, 'ALEA')
    [(21, 4), (21, 11), (36, -11)]
    >>> proteinsearch(protein, 'iacta')
    [(27, -6), (27, 6)]
    >>> proteinsearch(protein, 'EST')
    [(29, -10), (29, 8)]
    >>> proteinsearch(protein, 'EST', maxstep=8)
    [(29, 8)]
    >>> proteinsearch(protein, 'Proline')
    Traceback (most recent call last):
    AssertionError: invalid amino word
    Traceback (most recent call last):
    AssertionError: invalid amino word
        '''
    # checking word by the function 'aminoword()'
    # if the result is false, then assertionerror 
    if aminoword(word) == False:
        raise AssertionError( 'invalid amino word')
    # if the result is true
    else:
        #set variables
        result = []
        first = word[0]
        second = word[1]
        word = word.upper()
        #using the function positions to find position number of certain letter
        list1 = positions(protein, first)
        list2 = positions(protein, second)
        #list1 은 a를 뭉쳐놓은것들
        for x in list1:
            for y in list2:      
                s = int(math.fabs(y - x))
               #if there is given maxstep
                if maxstep:
                    if s <= maxstep:
                        if proteincode(protein, x, s, len(word)) == word:
                            result.append((x,s))
                    
                        if proteincode(protein, x, -s, len(word)) == word:
                            result.append((x,-s))
                        
                #if there is no maxstep 
                else:
                    if proteincode(protein, x, s, len(word)) == word:
                        result.append((x,s))
                    
                    if proteincode(protein, x, -s, len(word)) == word:
                        result.append((x,-s))
                        
            
        
        # remove the 겹치는 것들
        result = set(result)
        return sorted(list(result))




if __name__ == '__main__':
    import doctest
    doctest.testmod()