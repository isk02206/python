def increasing(pn):
    '''
    >>> increasing([2, 3, 5, 7, 11, 13])
    True
    >>> increasing((0, 0, 1, 2, 2, 3, 3, 4, 4, 4, 4, 5, 5, 6))
    True
    >>> increasing([5, 3, 2, 7, 8, 1, 9])
    False
    '''
    for i in range(len(pn)-1):
        a = pn[i]
        b = pn[i+1]
        if a > b:
            return False
        if a <= b:
            continue
    return True

def frequencySequence(pn):
    '''
    >>> frequencySequence([2, 3, 5, 7, 11, 13])
    [0, 0, 1, 2, 2, 3, 3, 4, 4, 4, 4, 5, 5, 6]
    >>> frequencySequence((0, 0, 1, 2, 2, 3, 3, 4, 4, 4, 4, 5, 5, 6))
    [2, 3, 5, 7, 11, 13, 14]
    >>> frequencySequence([5, 3, 2, 7, 8, 1, 9])
    Traceback (most recent call last):
    AssertionError: given sequence is not increasing
    '''
    record = int(pn[-1])+1
    frequencyList = []
    count = 0
    if increasing(pn) == True:
        for i in range(record):
            for j in pn:
                if i == j:
                    count += 1
            else:
                frequencyList.append(count)
        return frequencyList
    else:
        raise AssertionError('given sequence is not increasing')

def lift(list):
    '''
    >>> lift([2, 3, 5, 7, 11, 13])
    [3, 5, 8, 11, 16, 19]
    >>> lift((0, 0, 1, 2, 2, 3, 3, 4, 4, 4, 4, 5, 5, 6))
    [1, 2, 4, 6, 7, 9, 10, 12, 13, 14, 15, 17, 18, 20]
    >>> lift([5, 3, 2, 7, 8, 1, 9])
    [6, 5, 5, 11, 13, 7, 16]
    '''
    liftList = []
    number = 0
    for i in list:
        i = int(i)
        number += 1
        liftList.append(i+number)
    return liftList

def complementarySequences(pn):
    '''
    >>> complementarySequences([2, 3, 5, 7, 11, 13])
    ([3, 5, 8, 11, 16, 19], [1, 2, 4, 6, 7, 9, 10, 12, 13, 14, 15, 17, 18, 20])
    >>> complementarySequences((1, 3, 3, 5, 5, 5, 7, 7, 7, 7))
    ([2, 5, 6, 9, 10, 11, 14, 15, 16, 17], [1, 3, 4, 7, 8, 12, 13, 18])
    >>> complementarySequences([5, 3, 2, 7, 8, 1, 9])
    Traceback (most recent call last):
    AssertionError: given sequence is not increasing
    '''
    increase = []
    if increasing(pn) == True:
        count = 0
        for i in pn:
            count += 1
            i = int(i)
            number = i + count
            increase.append(number)
        freq = frequencySequence(pn)
        lif = lift(freq)
        all = increase,lif
        return tuple(all)
    else:
        raise AssertionError('given sequence is not increasing')

