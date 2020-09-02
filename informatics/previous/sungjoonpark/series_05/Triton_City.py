def factorial(n):
    """
    Computes the factorial of n.
    
    >>> factorial(10)
    3628800
    >>> factorial(32)
    263130836933693530167218012160000000
    """
    num =1
    while n>1:
        num = num*n
        n = n-1
    return num

def binomialCoefficient(n,k):
    """
    Computes the bionomial coefficient index by n and k.
    
    >>> binomialCoefficient(7, 3)
    35
    >>> binomialCoefficient(12, 4)
    495
    """
    if 0 <= k <= n:
        bc = factorial(n) / (factorial(k)*factorial(n-k))
        return int(bc)
    if k < 0 or k > n:
        return 0

def triangularNumber(n):
    """
    Computes the n-th triangular number.
    
    >>> triangularNumber(10)
    55
    >>> triangularNumber(32)
    528
    """
    tn = (n*(n+1))/2
    return int(tn)

def tetrahedralNumber(n):
    """
    Computes the n-th tetrahedral number.
    
    >>> tetrahedralNumber(10)
    220
    >>> tetrahedralNumber(32)
    5984
    """
    tk = (n*(n+1)*(n+2))/6
    return int(tk)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    