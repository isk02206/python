'''
Created on 2016. 1. 27.

@author: User
'''

def recombination(word1, word2, word3):
    '''
    >>> recombination('burgul', 'aeneas', 'bengal')
    'aureus'
    >>> recombination('oleins', 'arcade', 'oreads')
    'alcine'
    >>> recombination('alevin', 'elodea', 'alodia')
    'eleven'
    >>> recombination('nitrogen', 'fluorine', 'tin')
    Traceback (most recent call last):
    AssertionError: words must have equal length
    >>> recombination('nitrogen', 'fluorine', 'aluminium')
    Traceback (most recent call last):
    AssertionError: words must have equal length

    >>> recombination('nitrogen', 'fluorine', 'ringtone')
    Traceback (most recent call last):
    AssertionError: invalid recombination

    '''
    result = ''
    
    assert len(word1) == len(word2) and len(word1) == len(word3), 'words must have equal length'
    
    for pos in range(len(word3)):
        
        if word3[pos] != word1[pos] and word3[pos] != word2[pos]:
            
            raise AssertionError('invalid recombination')
        
            break
        
        else:
            if word3[pos] == word1[pos]:
            
                result += word2[pos]
            
            elif word3[pos] == word2[pos]:
            
                result += word1[pos]
                
    return result

def chimeras(word1, word2, sec):
    '''
    >>> chimeras('burgul', 'aeneas', '2-3;5')
    ('bengal', 'aureus')
    >>> chimeras('oleins', 'arcade', '2;4-5')
    ('oreads', 'alcine')
    >>> chimeras('alevin', 'elodea', '2-4;6')
    ('alodia', 'eleven')

    >>> chimeras('nitrogen', 'aluminium', '3-7')
    Traceback (most recent call last):
    AssertionError: words must have equal length
'''
    assert len(word1) == len(word2), 'words must have equal length'
       
    #list1 = sorted(sec.split(';')) #알파벳이나 숫자들을 큰순서대로 
    list1 = sec.split(';')
    new1 = ''
    new2 = ''
    
    pos = 0
    
    for x in list1:
        
        if not '-' in x:
            
            part = int(x) -1
            
            while pos != part:
                
                new1 += word1[pos]
                
                new2 += word2[pos]
                
                pos += 1
            
            else:
                new1 += word2[pos]
                
                new2 += word1[pos]
                
                pos += 1
        else:
            
            part = x.split('-')
            
            start = int(part[0]) - 1
            
            end = int(part[1]) - 1
            
            while pos != start:
                
                new1 += word1[pos]
                
                new2 += word2[pos]
            
                pos += 1
            
            new1 += word2[start:end+1] 
            
            new2 += word1[start:end+1]
            
            pos += len(word2[start:end+1])
    
    
    while pos < len(word1):
        
        new1 += word1[pos]
        
        new2 += word2[pos]
        
        pos += 1
        
    return new1, new2


if __name__ == '__main__':
    import doctest
    doctest.testmod()