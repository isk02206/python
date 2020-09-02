'''
Created on 2016. 2. 5.

@author: User
'''
def nPrime(n = None):
    '''
    >>> nPrime()
    [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    >>> nPrime(5)
    [2, 3, 5, 7, 11]
    >>> nPrime(8)
    [2, 3, 5, 7, 11, 13, 17, 19]
    '''
    # 'n = none' means the value of n is 10.
    if n == None:
        n = 10
    #set variables
    result = []
    # prime number starts from 2
    number = 2
    #
    while len(result) != n:
        if number <= 3:
            
            result.append(number)
        
        else:
            for x in range(2,number):
                
                if number % x == 0:
                
                    break
                
            else:
                result.append(number)
                    
        number += 1
        
    return result

def anagramHash(sentence, list1):
    '''
    >>> anagramHash('Leonardo Da Vinci', nPrime(26))
    4153036139030192260
    >>> anagramHash('Leonardo Da Vinci', range(1, 27))
    4073908608000
    >>> anagramHash('Leonardo Da Vinci', nPrime(52)[-26:])
    280080025163413341541861091223919
    >>> anagramHash('O Draconian Devil', nPrime(26))
    4153036139030192260


    '''
    count = 1
    
    sentence = sentence.lower()
    
    for char in sentence:
        
        if char.isalpha():
            
            pos = ord(char) - 97
            
            count = count * list1[pos]
            
    return count

def areAnagrams(word1, word2, list1 = nPrime(26)):
    '''
    >>> areAnagrams('Leonardo Da Vinci', 'O Draconian Devil')
    True
    >>> areAnagrams('The Mona Lisa', 'Oh Lame Saint')
    True
    >>> areAnagrams('The Mona Lisa', 'Oh Lame Saint', range(1, 27))
    True
    >>> areAnagrams('The Mona Lisa', 'Oh Lame Saint', nPrime(52)[-26:])
    True
    '''
    return anagramHash(word1, list1) == anagramHash(word2, list1)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
