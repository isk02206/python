'''
Created on 2018. 10. 07
@Subject : corkscrew
@Author : Son Jee Hun
@Student Number : 01406444
'''

def rotateLeft(nature_number):
    '''
    >>> rotateLeft(717948)
    179487
    >>> rotateLeft(142857)
    428571
    >>> rotateLeft(105263157894736842)
    52631578947368421
    '''
    list_nature_number = list(str(nature_number)) # nature_number make list
    list_nature_number = list_nature_number[1:] + list(list_nature_number[0])
    # first number remove after removed first number add last number
    if list_nature_number[0] == '0': # if first number is 0, remove 0
        list_nature_number = list_nature_number[1:]
    return int(''.join(list_nature_number)) # list convert integer

def rotateRight(nature_number):
    '''
    >>> rotateRight(179487)
    717948
    >>> rotateRight(428571)
    142857
    >>> rotateRight(52631578947368421)
    15263157894736842
    '''
    list_nature_number = list(str(nature_number)) #nature_number make list
    list_nature_number = list(list_nature_number[-1]) + list_nature_number[:-1]
    #Last nature_number remove and removed nature_number add first place
    return int(''.join(list_nature_number)) # list convert integer

def parasitic(nature_number):
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
    parasitic_number = 0
    while parasitic_number < 10:
        if int(parasitic_number) * int(nature_number) == int(rotateRight(nature_number)):
            return parasitic_number
        parasitic_number += 1
    return 0

def corkscrew(multiflying_number, append_number):
    '''
    >>> corkscrew(4, 7)
    179487
    >>> corkscrew(5, 7)
    142857
    >>> corkscrew(2, 2)
    105263157894736842
    '''
    result = multiflying_number * append_number
    count = 1
    while result != rotateRight(append_number):
        # change type number because change the position
        append_number = str(result)[len(str(result)) - count:] + str(append_number)[-1]
        # first number 0 remove 0
        if append_number[0] == '0':
            append_number = append_number[1:]
        #change result value
        result = multiflying_number * int(append_number)
        count += 1
    return int(append_number)

if __name__ == '__main__':
    import doctest
    doctest.testmod()