def isVowel(alphabet):
    '''
    >>> isVowel('a')
    True
    >>> isVowel('c')
    False
    >>> isVowel('E')
    True
    '''
    vowel = ['a', 'e', 'i', 'o', 'u','A','E','I','O','U']
    for i in vowel:
        if alphabet == i:
            return True
    else:
        return False

def encode(statement):
    '''
    >>> encode('Fabiano')
    'Fabababianabo'
    >>> encode('CIA-agent')
    'CAbiA-abagabent'
    '''
    encoded = ''
    pos = -1
    for i in statement:
        if i.isupper() == True and isVowel(i) == True:
            encoded += 'Ab'
            encoded += i.lower()
        if i.islower() == True and isVowel(i) == True:
            encoded += 'ab'
            encoded += i
        if isVowel(i) == False:
            encoded += i

    for j in range(len(statement)):
        x = statement[j]
        if isVowel(x) == True:
            a =
            while



    return encoded
