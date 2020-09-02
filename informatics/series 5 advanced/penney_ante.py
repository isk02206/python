'''
Created on 2018. 10. 07
@Subject : penney_ante
@Author : Son Jee Hun
@Student Number : 01406444
'''
def winner(player_1, player_2, sequence):
    '''
    >>> winner('HHH', 'THH', 'HTHTHHHHTHHHTTTTHTHH')
    2
    >>> winner('THT', 'TTH', 'HTHTHHHHTHHHTTTTHTHH')
    1
    >>> winner('THH', 'HHT', 'HHHHHHHHHHHHHHHHHHHH')
    0
    >>> winner('THH', 'THH', 'HHHHHHHHHHHHHHHHHHHH')
    Traceback (most recent call last):
    AssertionError: sequences cannot be equal
    >>> winner('THHT', 'THH', 'HHHHHHHHHHHHHHHHHHHH')
    Traceback (most recent call last):
    AssertionError: sequences must have equal length
    '''
    test_sequence = ''
    for i in sequence:
        test_sequence += i
        # if each player pick card appear, appear card have player win
        if test_sequence[-len(player_1)::] == player_1:
            type = 1
            break
        elif test_sequence[-len(player_2)::] == player_2:
            type = 2
            break
        else:
            type = 0

    assert player_1 != player_2, 'sequences cannot be equal'
    assert len(player_1) == len(player_2), 'sequences must have equal length'

    return type

def bitsequence(seq_1, seq_2):
    '''
    >>> bitsequence('HHH', 'THH')
    '000'
    >>> bitsequence('THT', 'TTH')
    '001'
    >>> bitsequence('THH', 'HHT')
    '011'
    '''
    result = ''
    # length different
    if len(seq_1) < len(seq_2):
        for index in range(0, len(seq_1)):
            if seq_1[index:] == seq_2[0:len(seq_1) - index]:
                result += '1'
            else:
                result += '0'

    if len(seq_1) >= len(seq_2):
        #because seq_1 and seq_2 not same
        result += '0' * (len(seq_1) - len(seq_2))
        for index in range(0, len(seq_2)):
            if seq_1[(len(seq_1)-len(seq_2)) + index:] == seq_2[0:len(seq_2) - index]:
                result += '1'
            else:
                result += '0'

    return result

def odds(seq_1, seq_2):
    '''
    >>> odds('HHH', 'THH')
    (1, 7)
    >>> odds('THT', 'TTH')
    (1, 2)
    >>> odds('THH', 'HHT')
    (3, 1)
    '''
    from fractions import gcd
    # binary number change decimal number. int function has seceond optional parameter
    aa = int(bitsequence(seq_1, seq_1).replace("'", ''), 2)
    ab = int(bitsequence(seq_1, seq_2).replace("'", ''), 2)
    bb = int(bitsequence(seq_2, seq_2).replace("'", ''), 2)
    ba = int(bitsequence(seq_2, seq_1).replace("'", ''), 2)
    Ka = bb - ba
    Kb = aa - ab
    #find greatest common divisor
    greatest_common_divisor = gcd(Ka, Kb)
    Ka //= greatest_common_divisor
    Kb //= greatest_common_divisor

    return (Ka, Kb)

def probabilities(seq_1, seq_2):
    '''
    >>> probabilities('HHH', 'THH')
    (0.125, 0.875)
    >>> probabilities('THT', 'TTH')
    (0.3333333333333333, 0.6666666666666666)
    >>> probabilities('THH', 'HHT')
    (0.75, 0.25)
    '''
    # make list odds function
    list_odds = list(odds(seq_1, seq_2))
    Ka = list_odds[0]
    Kb = list_odds[1]
    Pa = int(Ka) / (int(Ka) + int(Kb))
    Pb = int(Kb) / (int(Ka) + int(Kb))

    return (Pa, Pb)


if __name__ == '__main__':
    import doctest
    doctest.testmod()