'''
Created on 2018. 11. 09
@Subject : chutes_and_ladders
@Author : Son Jee Hun
@Student Number : 01406444
'''
def merge(chutes, ladders):
    '''
    >>> chutes = {98: 78, 95: 75, 93: 73, 87: 24, 64: 60, 62: 19, 56: 53, 49: 11, 47: 26, 16: 6}
    >>> ladders = {1: 38, 4: 14, 9: 31, 21: 42, 28: 84, 36: 44, 51: 67, 71: 91, 80: 100}
    >>> merge(chutes, ladders)
    {64: -4, 1: 37, 4: 10, 71: 20, 9: 22, 16: -10, 21: 21, 87: -63, 28: 56, 93: -20, 95: -20, 80: 20, 98: -20, 36: 8, 47: -21, 49: -38, 51: 16, 56: -3, 62: -43}
    >>> merge({23: 32}, {44: 44})
    Traceback (most recent call last):
    AssertionError: invalid configuration
    '''
    new = {}
    for chute in chutes:
        assert chute >= chutes[chute], 'invalid configuration'
        chutes_value = chutes[chute] - chute # make chute value
        new.update({chute:chutes_value}) # new dictionary add chute key and value
    for ladder in ladders:
        assert ladder not in new.keys(), 'invalid configuration'
        assert ladder <= ladders[ladder], 'invalid configuration'
        ladders_value = ladders[ladder] - ladder # make ladder value
        new.update({ladder:ladders_value}) # new dictionary add ladder key and value

    return new

def spaces(moving_space, chutes, ladders):
    '''
    >>> chutes = {98: 78, 95: 75, 93: 73, 87: 24, 64: 60, 62: 19, 56: 53, 49: 11, 47: 26, 16: 6}
    >>> ladders = {1: 38, 4: 14, 9: 31, 21: 42, 28: 84, 36: 44, 51: 67, 71: 91, 80: 100}
    >>> spaces([1, 4, 5], chutes, ladders)
    [38, 42, 26]
    >>> spaces([2, 4, 1, 4, 5, 5, 4, 2], chutes, ladders)
    [2, 6, 7, 11, 6, 11, 15, 17]
    >>> spaces([5] * 16, chutes, ladders)
    [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 100]
    >>> spaces([6] * 14, chutes, ladders)
    [6, 12, 18, 24, 30, 44, 50, 53, 59, 65, 91, 97, 97, 97]
    >>> spaces([4, 2, 5, 6], {23: 32}, {44: 44})
    Traceback (most recent call last):
    AssertionError: invalid configuration
    '''
    rule = merge(chutes, ladders) # use merge function
    result = []
    count = 0
    for i in moving_space:
        if result == []: # if length of result list is 0
            count += i # moving player
            if rule.get(count) is None:
                result.append(count) # not ladder or chute, moving only spacing
                count = result[-1]
            else:# if ladder or chute, moving laddervalue or chutevalue add spacing
                result.append(count + rule.get(count))
                count = result[-1]
        else:
            count += i
            if count > 100 or count < 0:
                count = result[-1] # if count > 100, count < 0 count are result final value

            elif count <= 100 or count > 0:
                count = result[-1] + i # if count < 100, count > 0 are result value final value add moving space

            if rule.get(count) is None:
                result.append(count) # if not ladder or chute, moving only spacing
                count = result[-1]
            else:
                result.append(count + rule.get(count))# if ladder or chute, moving laddervalue or chutevalue and spacing
                count = rule.get(count) + count # reset moving count

    return result

if __name__ == '__main__':
    import doctest
    doctest.testmod()