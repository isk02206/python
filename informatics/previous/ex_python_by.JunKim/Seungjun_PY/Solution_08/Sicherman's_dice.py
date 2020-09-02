'''
Created on 2015. 12. 2.

@author: USER
'''
def combinations(dice1, dice2):
    """
    >>> dice6_1 = {1, 2, 3, 4, 5, 6}
    >>> dice6_2 = [1, 2, 2, 3, 3, 4]
    >>> dice6_3 = (1, 3, 4, 5, 6, 8)
    >>> throw = combinations(dice6_1, dice6_1)
    >>> throw[8]
    [(2, 6), (3, 5), (4, 4), (5, 3), (6, 2)]
    >>> throw = combinations(dice6_2, dice6_3)
    >>> throw[8]
    39
    [(2, 6), (2, 6), (3, 5), (3, 5), (4, 4)]
    """
    # generate all possible outcomes of throwing the two given dice, and map the
    # sum of the dice to the list of outcomes that generate that sum
    freq = dict()
    for eyes1 in dice1:
        for eyes2 in dice2:
            if eyes1 + eyes2 not in freq:
                freq[eyes1 + eyes2] = [(eyes1, eyes2)]
            else:
                freq[eyes1 + eyes2].append((eyes1, eyes2))
    # sort the list of throws that result in the same sum
    for total in freq:
        freq[total].sort()
    # return the generated dictionary
    return freq
def distribution(dice1, dice2):
    """
    >>> dice6_1 = {1, 2, 3, 4, 5, 6}
    >>> dice6_2 = [1, 2, 2, 3, 3, 4]
    >>> dice6_3 = (1, 3, 4, 5, 6, 8)
    >>> distribution(dice6_1, dice6_1)
    {2: 1, 3: 2, 4: 3, 5: 4, 6: 5, 7: 6, 8: 5, 9: 4, 10: 3, 11: 2, 12: 1}
    >>> distribution(dice6_2, dice6_3)
    {2: 1, 3: 2, 4: 3, 5: 4, 6: 5, 7: 6, 8: 5, 9: 4, 10: 3, 11: 2, 12: 1}
    """
    # generate all possible outcomes of throwing the two given dice, and map the
    # sum of the dice to the total number of outcomes that generate that sum
    freq = dict()
    for eyes1 in dice1:
        for eyes2 in dice2:
            freq[eyes1 + eyes2] = freq.get(eyes1 + eyes2, 0) + 1
    # return the generated dictionary
    return freq
def equalDistribution(pair1, pair2):
    """
    >>> dice6_1 = {1, 2, 3, 4, 5, 6}
    >>> dice6_2 = [1, 2, 2, 3, 3, 4]
    >>> dice6_3 = (1, 3, 4, 5, 6, 8)
    >>> equalDistribution([dice6_1, dice6_1], (dice6_2, dice6_3))
    True
    >>> dice8_1 = {1, 2, 3, 4, 5, 6, 7, 8}
    >>> dice8_2 = (1, 3, 5, 5, 7, 7, 9, 11)
    >>> dice8_3 = (1, 2, 2, 3, 3, 4, 4, 5)
    >>> dice8_4 = (1, 2, 5, 5, 6, 6, 9, 10)
    >>> dice8_5 = (1, 2, 3, 3, 4, 4, 5, 6)
    >>> equalDistribution((dice8_1, dice8_1), (dice8_2, dice8_3))
    True
    >>> equalDistribution((dice8_1, dice8_1), (dice8_3, dice8_4))
    False
    >>> equalDistribution((dice8_1, dice8_1), (dice8_4, dice8_5))
    True
    """
    # check if the probability distribution of both pairs of dice is the same
    return distribution(*pair1) == distribution(*pair2)
    
if __name__ == '__main__':
    import doctest
    doctest.testmod()
