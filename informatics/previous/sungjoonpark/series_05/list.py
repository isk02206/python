def palindromic(n):
    '''
    >>> palindromic(6)
    True
    >>> palindromic(1234)
    False
    >>> palindromic(98786)
    False
    >>> palindromic(3160613)
    True
    '''
    a = str(n)
    if a == a[::-1]:
        return True
    if 0 <= n < 10:
        return True
    else:
        return False
    

def palindromicmultiples(n,c):
    '''
    >>> palindromicmultiples(3, 1)
    3
    >>> palindromicmultiples(25, 3)
    2
    >>> palindromicmultiples(12, 4)
    7
    >>> palindromicmultiples(30, 3)
    0
    >>> palindromicmultiples(81, 6)
    0
    '''
    
    if 1 <= n <1000 and 1<=c<=6:
        count = 0
        x = n
        a = 1
        while 1 <= x*a <1000000:
            if (palindromic(x*a) == True) and len(str(x*a)) == c:
                count = count + 1
                a = a + 1
                continue
            else:
                a = a + 1
                continue
            
        return count
        


if __name__ == '__main__':
    import doctest
    doctest.testmod()