'''
name : Sung Joon Park
student number : 01514170
'''

def merge(chutes,ladders):
    '''
    >>> chutes = {98: 78, 95: 75, 93: 73, 87: 24, 64: 60, 62: 19, 56: 53, 49: 11, 47: 26, 16: 6}
    >>> ladders = {1; 38, 4: 14, 9: 31, 21: 42, 28: 84, 36: 44, 51: 67, 71: 91, 80: 100}
    >>>merge(chutes, ladders)
    {64: -4, 1: 37, 4: 10, 71: 20, 9: 22, 16: -10, 21: 21, 87: -63, 28: 56, 93: -20, 95: -20, 80: 20, 98: -20, 36: 8, 47: -21, 49: -38, 51: 16, 56: -3, 62: -43}
    >>> chutes
    {98: 78, 95: 75, 93: 73, 87: 24, 64: 60, 62: 19, 56: 53, 49: 11, 47: 26, 16: 6}
    >>> ladders
    {1: 38, 4: 14, 9: 31, 21: 42, 28: 84, 36: 44, 51: 67, 71: 91, 80: 100}
    >>> merge({23: 32}, {44: 44})
    Traceback (most recent call last):
    AssertionError: invalid configuration
    '''
    merge = {}
    for i in chutes:
        cvalue = int(i)-int(chutes.values(i)) #new merge value for chutes' key
        merge[i] = cvalue #add merged value to dictionary
    for j in ladders:
        lvalue = j - ladders.values(j) #new merge value for ladders' key
        merge[j] = lvalue #add merged value to dictionary
    return merge
    
def spaces(rolls,chutes,ladders):
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
    rolls = [] 
    rolled = [] #changed location history
    location = 0 #changed location 
    for i in range(len(rolls)):
        if rolls[i] == merge(chutes,ladders):
            location = location + rolls[i] + merge[rolls[i]] #if location has chute or ladder the location changes.
            rolled.append(location)
        if rolls[i] != merge(chutes,ladders): #if the location doesn't have a chute or a ladder the location doesn't changes.
            if 100 - location < rolls[i]: #token's location doesn't change if the die roll is bigger then the spaces left.
                location = location
            else:
                location = rolls[i] #the token changes location with
                rolled.append(location)
        if 100-location == rolls: #if the token reaches 100 the game stops
            rolled.append(100)
            break
    return rolled

if __name__ == '__main__':
    import doctest
    doctest.testmod()