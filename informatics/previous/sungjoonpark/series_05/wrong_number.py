def position(n):
    '''
    >>> position(8)
    (2, 1)
    >>> position(0)
    (3, 1)
    '''
    if n == 1:
        return (0, 0)
    if n == 2:
        return (0, 1)
    if n == 3:
        return (0, 2)
    if n == 4:
        return (1, 0)
    if n == 5:
        return (1, 1)
    if n == 6:
        return (1, 2)
    if n == 7:
        return (2, 0)
    if n == 8:
        return (2, 1)
    if n == 9:
        return (2, 2)
    if n == 0:
        return (3, 1)

def movement(n, m):
    '''
    >>> movement(8, 8)
    0
    >>> movement(8, 9)
    1
    >>> movement(8, 1)
    3
    >>> movement(8, 3)
    3
    '''
    nx = position(n)[0]
    ny = position(n)[1]
    mx = position(m)[0]
    my = position(m)[1]
    move = abs(nx-mx)+abs(ny-my)
    
    return move

def fingermovement(number):
    '''
    >>> fingermovement('888-888-8888')
    0
    >>> fingermovement('053/67.83.47')
    16
    '''
    validno = []
    for t in range(len(number)):
        x = number[t]
        if  48 <= ord(x) <= 57:
            validno.append(x)
    count = 0
    for i in range(len(validno)-1):
        n = validno[i]
        a = int(n)
        m = validno[i+1]
        b = int(m)
        moving = movement(a, b)
        count += moving
    return count

if __name__ == '__main__':
    import doctest
    doctest.testmod()
