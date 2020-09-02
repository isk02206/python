def next(list):
    '''
    >>> next([32, 9, 14, 3])
    (23, 5, 11, 29)
    >>> next((1, 2, 1, 2, 1, 0))
    (1, 1, 1, 1, 1, 1)
    >>> next((1, 2, 1, 2, 1, 1))
    (1, 1, 1, 1, 0, 0)
    '''
    nextList = []
    for i in range(len(list)):
        if i == len(list) - 1:
            pat = abs(int(list[i])-int(list[0]))
            nextList.append(pat)
        else:
            pat = abs(int(list[i]) - int(list[i + 1]))
            nextList.append(pat)
    return tuple(nextList)

def ducci(list):
    '''
    >>> ducci([32, 9, 14, 3])
    ((32, 9, 14, 3), (23, 5, 11, 29), (18, 6, 18, 6), (12, 12, 12, 12), (0, 0, 0, 0))
    >>> ducci((1, 2, 1, 2, 1, 0))
    ((1, 2, 1, 2, 1, 0), (1, 1, 1, 1, 1, 1), (0, 0, 0, 0, 0, 0))
    >>> ducci((1, 2, 1, 2, 1, 1))
    ((1, 2, 1, 2, 1, 1), (1, 1, 1, 1, 0, 0), (0, 0, 0, 1, 0, 1), (0, 0, 1, 1, 1, 1), (0, 1, 0, 0, 0, 1), (1, 1, 0, 0, 1, 1), (0, 1, 0, 1, 0, 0), (1, 1, 1, 1, 0, 0))
    '''
    result = [tuple(list)]
    pos = 0
    a = next(list)
    while tuple(list) != a:
        pos += 1
        a = next(result[pos-1])
        if a in result:
            result.append(a)
            return tuple(result)
        result.append(a)
        sum = 0
        for i in a:
            i = int(i)
            sum += i
        if sum == 0:
            return tuple(result)
    return tuple(result)

def period(list):
    '''
    >>> period([32, 9, 14, 3])
    0
    >>> period((1, 2, 1, 2, 1, 0))
    0
    >>> period((1, 2, 1, 2, 1, 1))
    6
    '''
    a = ducci(list)
    sum = 0
    for i in a[-1]:
        i = int(i)
        sum += i
    if sum == 0:
        return 0
    else:
        pos = -1
        same = a[-1]
        for j in a:
            pos += 1
            if j == same:
                break
        new = a[pos:]
        per = len(new)-1
        return per




