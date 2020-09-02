def lettervalue(alphabet):
    '''
    >>> lettervalue('A')
    1
    >>> lettervalue('j')
    10
    >>> lettervalue('!')
    0
    '''
    alphabet = alphabet.lower()
    if 97 <= ord(alphabet)<= 122:
        number = ord(alphabet) - 96
        return number
    else:
        return 0

def wordvalue(word):
    '''
    >>> wordvalue('arm')
    32
    >>> wordvalue('BEND')
    25
    >>> wordvalue('elbow')
    57
    '''
    sum = 0
    for i in word:
        sum += lettervalue(i)
    return sum

def wordsum(word1, word2, word3):
    '''
    >>> wordsum('arm', 'BEND', 'elbow')
    True
    >>> wordsum('KING', 'chair', 'THRONE')
    True
    >>> wordsum('Monty', 'Python', 'SHRUBBERY')
    False
    '''
    sumword1 = wordvalue(word1)
    sumword2 = wordvalue(word2)
    sumword3 = wordvalue(word3)
    if sumword1 + sumword2 == sumword3:
        return True
    else:
        return False
