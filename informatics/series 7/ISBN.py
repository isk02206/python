def testISBN10(code):
    """
    >>> ISBN10(’080442957X’)
    True
    """
    if len(code) != 10:
        return False
    if not code[:-1].isdigit():
        return False
    if not code[-1].isdigit() and code[-1] != 'X':
        return False
    checkdigit = 0
    for i in range(9):
        checkdigit += int(code[i]) * (i+1)
        checkdigit %= 11
    if checkdigit == 10:
        if code[-1] != 'X':
            return False
    elif str(checkdigit) != code[-1]:
        return False
    return True
def testISBN13(code):
    """
    >>> testISBN13(’9789027439642’)
    True
    """
    if isinstance(code, int):
        return  False
    if len(code) != 13:
        return False
    if not code.isdigit():
        return False
    checkdigit = 0
    for i in range(12):
        if i % 2:
            checkdigit += 3 * int(code[i])
        else:
            checkdigit += int(code[i])
    checkdigit %= 10
    checkdigit = (10 - checkdigit) % 10
    if checkdigit != int(code[-1]):
        return False
    return True
def isISBN(code, new=True):
    """
    >>> testISBN(’9789027439642’, False)
    False
    >>> testISBN(’9789027439642’, True)
    True
    >>> testISBN(’9789027439642’)
    True
    >>> testISBN(’080442957X’)
    False
    >>> testISBN(’080442957X’, False)
    True
    """
    if new:
        return testISBN13(code)

    return testISBN10(code)
def areISBN(codes, new=None):
    """
    >>> isbnList([’0012345678’, ’0012345679’, ’9971502100’, ’080442957X’, 5, True, ’The
    Practice of Computing Using Python’, ’9789027439642’, ’5486948320146’])
    [False, True, True, True, False, False, False, True, False]
    >>> isbnList([’0012345678’, ’0012345679’, ’9971502100’, ’080442957X’, 5, True, ’The
    Practice of Computing Using Python’, ’9789027439642’, ’5486948320146’], True)
    [False, False, False, False, False, False, False, True, False]
    >>> isbnList([’0012345678’, ’0012345679’, ’9971502100’, ’080442957X’, 5, True, ’The
    Practice of Computing Using Python’, ’9789027439642’, ’5486948320146’], False)
    [False, True, True, True, False, False, False, False, False]
    """
    result = []
    for code in codes:
        if isinstance(code, str):
            if new is None:
                if len(code) == 13:
                    result.append(isISBN(code, True))
                else:
                    result.append(isISBN(code, False))
            else:
                result.append(isISBN(code, new))
        else:
            result.append(False)
    return result

if __name__ == '__main__':
    import doctest
    doctest.testmod()