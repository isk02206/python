'''
Created on 2016. 11. 18.

@author: jeongkihong
@student_number: 01514158
'''
def pangram(sentence):
    '''
    >>> pangram('The quick brown fox jumps over the lazy dog.')
    True
    >>> pangram('The quick brown fox jumped over the lazy dog.')
    False
    '''
    # alphabet letters 
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    sentence = sentence.lower()
    
    # checking weather the sentence has all letters of alphabet
    for char in alphabet:
        if char not in sentence:
            return False
        
    return True
                    
                    
def window(sentence):
    '''
    >>> window('The quick brown fox jumps over the lazy dog.')
    'quick brown fox jumps over the lazy dog'
    >>> window('The quick brown fox jumped over the lazy dog.')
    >>> window("I sang, and thought I sang very well; but he just looked up into my face with a very quizzical expression, and said, 'How long have you been singing, Mademoiselle?' ")
    'g very well; but he just looked up into my face with a very quizzical ex'
    >>> window("'We are all from Xanth,' Cube said quickly. 'Just visiting Phaze. We just want to find the dragon.'")
    "from Xanth,' Cube said quickly. 'Just visiting Phaze. W"
    >>> window("Further, fractal geometries are replicated on a human level in the production of certain 'types' of subjectivity: for example, aging kid quiz show whiz Donnie Smith (William H. Macy) and up and coming kid quiz show whiz Stanley Spector (Jeremy Blackman) are connected (or, perhaps, being cloned) in ways they couldn�셳 possibly imagine.")
    'bjectivity: for example, aging kid quiz show'
    '''
    # empty list for result
    result = []
    
    # checks weather the given sentence has probability of pangram
    if pangram(sentence) == False:
        return None
    
    # for given sentence, shortest length of pangram is 26 as length of alphabets is 26
    # slices given sentence to find pangram
    else:
        for i in range(len(sentence)-26):
            for j in range(i+26, len(sentence)):
                if pangram(sentence[i:j+1]) == True:
                    result.append(sentence[i:j+1])
                    
                else:
                    continue
    
    # sort result in length by ascending order and choose minimum             
    return sorted(result, key=len)[0]
    
    
if __name__ == "__main__" :
    import doctest
    doctest.testmod()