def merge(chutes,ladders):
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
    merge = {}
    for i in chutes:
        if chutes[i] != i:
            chutesValue = int(chutes[i]) - int(i)
            merge[i] = chutesValue

    for j in ladders:
        if ladders[j] != j:
            ladderValue = int(ladders[j]) - int(j)
            merge[j] = ladderValue
    return merge

def spaces(sequence, chutes, ladders):
    '''
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
    mergeDict =  merge(chutes,ladders)
    count = 0
    move = 0
    moveList = []
    while move < 100:
        for i in sequence:
            move += int(i)
            count += 1
            for j in mergeDict:
                if move == int(j):
                    move += merge[j]
                    moveList.append(move)
                else:
                    moveList.append(move)
    else:
        moveList.append(sequence[count-1:])
    return moveList