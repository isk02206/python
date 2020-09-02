'''
Name: Sung Joon Park
ID: 01514170
'''
def merge(chutes, ladders):
    '''
    >>> chutes = {98: 78, 95: 75, 93: 73, 87: 24, 64: 60, 62: 19, 56: 53, 49: 11, 47: 26, 16: 6}
    >>> ladders = {1: 38, 4: 14, 9: 31, 21: 42, 28: 84, 36: 44, 51: 67, 71: 91, 80: 100}
    >>> merge(chutes, ladders)
    {64: -4, 1: 37, 4: 10, 71: 20, 9: 22, 16: -10, 21: 21, 87: -63, 28: 56, 93: -20, 95: -20, 80: 20, 98: -20, 36: 8, 47: -21, 49: -38, 51: 16, 56: -3, 62: -43}
    >>> chutes
    {98: 78, 95: 75, 93: 73, 87: 24, 64: 60, 62: 19, 56: 53, 49: 11, 47: 26, 16: 6}
    >>> ladders
    {1: 38, 4: 14, 9: 31, 21: 42, 28: 84, 36: 44, 51: 67, 71: 91, 80: 100}
    >>> merge({23: 32}, {44: 44})
    Traceback (most recent call last):
    AssertionError: invalid configuration
    '''
    merges = {}
    for i in chutes:
        if int(chutes[i]) >= int(i):
            raise AssertionError('invalid configuration')
        else:
            merges[i] = int(chutes[i])-int(i)
    for j in ladders:
        if int(ladders[j]) <= int(j):
            raise AssertionError('invalid configuration')
        if j in merges:
            raise AssertionError('invalid configuration')
        else:
            merges[j] = int(ladders[j]) - int(j)
    return merges
def spaces(rolls, chutes, ladders):
    '''
    >>> chutes = {98: 78, 95: 75, 93: 73, 87: 24, 64: 60, 62: 19, 56: 53, 49: 11, 47: 26, 16: 6}
    >>> ladders = {1: 38, 4: 14, 9: 31, 21: 42, 28: 84, 36: 44, 51: 67, 71: 91, 80: 100}
    >>> spaces([1, 4, 5], chutes, ladders)
    [38, 42, 26]
    >>> spaces([2, 4, 1, 4, 5, 5, 4, 2], chutes, ladders)
    [2, 6, 7, 11, 6, 11, 15, 17]
    >>> spaces([5] * 16, chutes, ladders)
    [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 100]
    >>> spaces([6] * 14, chutes, ladders)
    [6, 12, 18, 24, 30, 44, 50, 53, 59, 65, 91, 97, 97, 97]
    >>> spaces([4, 2, 5, 6], {23: 32}, {44: 44})
    Traceback (most recent call last):
    AssertionError: invalid configuration
    '''
    merges = merge(chutes, ladders)
    moves = []
    position = 0
    for i in rolls:
        position += i
        if position not in merges:
            if position <= 100:
                moves.append(position)
            if position > 100:
                position -= i
                moves.append(position)
        if position in merges:
            position += merges[position]
            moves.append(position)
    return moves