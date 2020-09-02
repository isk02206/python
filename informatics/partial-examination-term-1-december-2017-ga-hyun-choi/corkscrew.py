def rotateLeft(number):
    '''
    return natural number after left rotation
    :param number:
    :return:
    >>> rotateLeft(717948)
    179487
    >>> rotateLeft(142857)
    428571
    >>> rotateLeft(105263157894736842)
    52631578947368421
    '''
    str_number = str(number)  # string fixes the digits
    rotated = str_number[0]  # character that rotates
    str_number = int(str_number[1:])  # atomatically drop leading zeros
    output = str(str_number)+rotated  # rotated number comes after all others
    return int(output)


def rotateRight(number):
    '''
    return natural number after fight rotation
    :param number:
    :return:
    >>> rotateRight(179487)
    717948
    >>> rotateRight(52631578947368421)
    15263157894736842
    '''
    str_number = str(number)  # string fixes the digits
    lotated = str_number[-1]  # character that rotates
    output = lotated + str_number[:-1]  # rotated number comes before all others
    return int(output)


def parasitic(number):
    '''
    indicate n if the number is n-parasitic, return 0 if it is not.
    :param number:
    :return:
    >>> parasitic(179487)
    4
    >>> parasitic(142857)
    5
    >>> parasitic(105263157894736842)
    2
    >>> parasitic(1234)
    0
    '''
    k = int(str(number)[-1])  # the last digit of the number
    n = 0  # the default value
    for test_n in range(1, k+1):  # n is always smaller or equal to k
        if test_n*number == rotateRight(number):  # definition of parasitic number
            n = test_n  # found the right n
            break
    return n


def corkscrew(n, k):
    '''
    return n-parasitic number that ends with digit k by corkscrew method
    :param n:
    :param k:
    :return:
    >>> corkscrew(4, 7)
    179487
    >>> corkscrew(5, 7)
    142857
    >>> corkscrew(2, 2)
    105263157894736842
    '''
    ans = n*k
    count = 0
    while True:
        count += 1
        rotated = str(ans)[-count:]  # the last two digits of the product
        k_number = int(rotated + str(k))  # k is added to the rightmost side
        ans = n*k_number  # product
        if rotateRight(k_number) == ans:
            break
    return k_number



if __name__ == "__main__":
    import doctest
    doctest.testmod()
