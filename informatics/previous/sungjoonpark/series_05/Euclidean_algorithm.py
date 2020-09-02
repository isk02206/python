def gcd(a,b):
    """
    Computes the greatest common divisor of the two
    integers a and b.
    
    >>> gcd(252, 105)
    21
    >>> gcd(48, 18)
    6
    """
    if a < b:
        a,b = b,a
    while b!= 0:
        a,b = b,a % b
    return a
    

def lcm(a,b):
    """
    Computes the least common multiple of the two
    integers a and b.

    >>> lcm(252, 105)
    1260
    >>> lcm(48, 18)
    144
    """
    x = (a*b)/ gcd(a,b)
    return int(x)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
