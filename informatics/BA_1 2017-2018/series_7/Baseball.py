def hit(x, occupied = None):
    '''
    >>> hit(2)
    (0, [2])
    >>> hit(0, [1, 3])
    (0, [1, 3])
    >>> hit(1, (1, 3))
    (1, [1, 2])
    >>> hit(2, occupied=[1, 3])
    (1, [2, 3])
    >>> hit(3, occupied=(1, 3))
    (2, [3])
    >>> hit(4, occupied=[1, 3])
    (3, [])
    '''
    score = 0
    result = []
    if occupied is None:
        if 0 < x < 4:
            result.append(x)
        if x == 4:
            score += 1
        return score,result
    else:
        run = []
        if 0 < x < 4:
            result.append(x)
        if x == 4:
            score += 1
        for i in occupied:
            i = int(i)
            i += x
            run.append(i)
        for j in run:
            j = int(j)
            if j >= 4:
                score += 1
            else:
                result.append(j)
        return score,result

def inning(hits):
    '''
    >>> inning([0, 1, 2, 3, 4])
    (4, [])
    >>> inning((4, 3, 2, 1, 0))
    (2, [1, 3])
    >>> inning([1, 1, 2, 1, 0, 0, 1, 3, 0])
    (5, [3])
    '''
    score = 0
    occupied = []
    for i in hits:
        i = int(i)
        a = hit(i,occupied)[0]
        occupied = hit(i,occupied)[1]
        score += a
    return score,occupied




