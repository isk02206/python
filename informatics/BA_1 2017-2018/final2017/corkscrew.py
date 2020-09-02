'''
Name: Sung Joon Park
ID: 01514170
'''
def rotateLeft(natural_number):
    '''
    >>> rotateLeft(717948)
    179487
    >>> rotateLeft(142857)
    428571
    >>> rotateLeft(105263157894736842)
    52631578947368421
    '''
    natural_number = str(natural_number) #converting the number into string form
    rotate_number = natural_number[0] #slicing the first number
    new_number = natural_number[1:] + rotate_number #chaanging the number form to a number without the first number
    # slicing the first number and adding the sliced number on the back of the original number without the first number
    return int(new_number)

def rotateRight(natural_number):
    '''
    >>> rotateRight(179487)
    717948
    >>> rotateRight(428571)
    142857
    >>> rotateRight(52631578947368421)
    15263157894736842
    '''
    natural_number = str(natural_number)
    rotate_number = natural_number[-1] #slicing the last number
    new_number = rotate_number + natural_number[:-1] #chaanging the number form to a number without the last number
    # slicing the last number and adding the sliced number on the front of the original number without the last number
    return int(new_number)

def parasitic(natural_number):
    '''
    >>> parasitic(179487)
    4
    >>> parasitic(142857)
    5
    >>> parasitic(105263157894736842)
    2
    >>> parasitic(1234)
    0
    '''
    result = rotateRight(natural_number) // natural_number #divided result with no floats
    compare_result = rotateRight(natural_number) / natural_number # divided result with floats
    if result == compare_result:
        #searching if the result is perfectly divided
        return result
    else:
        #if the result is not the same it means that the number is not parasitic and must return 0
        return 0

def corkscrew(a, b):
    '''
    >>> corkscrew(4, 7)
    179487
    >>> corkscrew(5, 7)
    142857
    >>> corkscrew(2, 2)
    105263157894736842
    '''
    b1 = b
    c = a * b1
    while rotateLeft(a*b1) != b1:
        c = a * b1
        if len(str(c)) == len(str(b1)):
            b1 = int(str(c)+str(b))
        if len(str(c)) > len(str(b1)):
            length_c = len(str(c))-1
            new_c = str(c)[-length_c:]
            b1 = int(new_c+str(b))
    return b1
