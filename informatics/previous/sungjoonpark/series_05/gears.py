def gcd(a,b):
    """
    Computes the greatest common divisor of the two integers a and b.

    >>> gcd(15, 24)
    3
    >>> gcd(252, 105)
    21
    """
    if a < b:
        a,b = b,a
    while b!= 0:
        a,b = b,a % b
    return a
    

def lcm(a,b):
    """
    Computes the least common multiple of the two integers a and b.

    >>> lcm(15, 24)
    120
    >>> lcm(252, 105)
    1260
    """
    x = (a*b)/ gcd(a,b)
    return int(x)

def rotations(a,b):
    """
    Computes the smallest number of rotations of a gear having a teeth that 
    puts gears with a and b teeth back into their initial position.

    >>> rotations(15, 24)
    8
    >>> rotations(252, 105)
    5
    """
    y = lcm(a,b) / a
    return int(y)
    

if __name__ == '__main__':
    import doctest
    doctest.testmod()
