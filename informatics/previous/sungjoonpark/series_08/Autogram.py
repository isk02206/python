def letterFrequencies(sentence):
    '''
    >>> frequentie = letterFrequencies("fifteen e's, seven f's, four g's, six h's, eight i's, four n's, five o's, six r's, eighteen s's, eight t's, four u's, three v's, two w's, three x's")
    >>> frequentie['e']
    15
    >>> frequentie['f']
    7
    >>> frequentie['g']
    4
    
    >>> frequentie = letterFrequencies("sixteen e's, five f's, three g's, six h's, nine i's, five n's, four o's, six r's, eighteen s's, eight t's, three u's, three v's, two w's, four x's")
    >>> frequentie['e']
    16
    >>> frequentie['f']
    5
    >>> frequentie['g']
    3
    '''
    sentence = sentence.lower()
    frequentie = {}
    for alph in sentence:
        if alph.isalpha():
            if alph in frequentie:
                frequentie[alph] += 1
            else:
                frequentie[alph] = 1
    return frequentie

def letterPositions(sentence):
    '''
    >>> positions = letterPositions("fifteen e's, seven f's, four g's, six h's, eight i's, four n's, five o's, six r's, eighteen s's, eight t's, four u's, three v's, two w's, three x's")
    >>> positions['e']
    {97, 67, 4, 5, 8, 43, 141, 14, 142, 16, 83, 88, 89, 121, 122}
    >>> positions['f']
    {0, 64, 2, 108, 19, 54, 24}
    >>> positions['g']
    {99, 29, 45, 85}
    
    >>> positions = letterPositions("sixteen e's, five f's, three g's, six h's, nine i's, five n's, four o's, six r's, eighteen s's, eight t's, three u's, three v's, two w's, four x's")
    >>> positions['e']
    {96, 4, 5, 8, 46, 110, 16, 111, 82, 87, 56, 88, 26, 27, 121, 122}
    >>> positions['f']
    {18, 138, 13, 53, 63}
    >>> positions['g']
    {98, 84, 29}
    '''
    
    
    positions = {}
    sentence = sentence.lower()
    for alpha in range(len(sentence)):
        if sentence[alpha].isalpha() and sentence[alpha] not in positions:
            positions[sentence[alpha]] = set()
        if sentence[alpha].isalpha():
            positions[sentence[alpha]].add(alpha)
            
    return positions
        
if __name__ == '__main__':
    import doctest
    doctest.testmod()
'''
def letterFrequencies(sentence):
    
    sentence = sentence.lower()
    
    dict1 = {}
    
    for i in range(len(sentence)):
        if sentence[i].isalpha():
            dict1[sentence[i]] = sentence.count(sentence[i])
            
    return dict1
    
    #string.index()
'''