'''
Created on 2015. 12. 3.

@author: User
'''
import random
def fill(marbles):
# generate a list having the given number of marbles, where each element
# represent a marble that is randomly given either a black or white color
    return [random.choice((¡¯black¡¯, ¡¯white¡¯)) for _ in range(marbles)]
def pick(urn):
# check whether there are at least two marbles in the urn
    assert len(urn) > 1, ¡¯the urn contains less than two marbles¡¯
# randomly pick the position of the first marble
    marble1 = random.randint(0, len(urn) - 1)
# randomly pick the position of the second marble, but make sure this
# position is different from the position of the first marble
    marble2 = random.randint(0, len(urn) - 1)
    while marble1 == marble2:
        marble2 = random.randint(0, len(urn) - 1)
# return the position in the urn of the first and the second marble picked
    return marble1, marble2
def remove(marble1, marble2, urn):
# check whether the two given positions point to different positions within
# the list representing the given urn
    assert (
        0 <= marble1 < len(urn) and
        0 <= marble2 < len(urn) and
        marble1 != marble2
    ), ¡¯invalid arguments¡¯
# remove the first marble at the given position and determine its color
    color1 = urn.pop(marble1)
# remove the second marble at the given position and determine its color
    if marble1 < marble2:
# if the first marble has been removed at a position before the position
# of the second marble, the second marble has now shifted one position
# to the head of the list
        color2 = urn.pop(marble2 - 1)
    else:

color2 = urn.pop(marble2)
    if color1 == color2:
# if both marbles are black or both marbles are white, put a black
# marble into the urn
    urn.append(¡¯black¡¯)
    else:
# if both marbles have a different color, put a white marble in the urn
urn.append(¡¯white¡¯)
def last(urn):
"""
>>> urn = fill(10)
>>> urn
[¡¯white¡¯, ¡¯white¡¯, ¡¯black¡¯, ¡¯black¡¯, ¡¯black¡¯, ¡¯white¡¯, ¡¯white¡¯, ¡¯white¡¯, ¡¯white¡¯, ¡¯black¡¯]
>>> marble1, marble2 = pick(urn)
>>> marble1, marble2
(1, 9)
>>> remove(marble1, marble2, urn)
>>> urn
[¡¯white¡¯, ¡¯black¡¯, ¡¯black¡¯, ¡¯black¡¯, ¡¯white¡¯, ¡¯white¡¯, ¡¯white¡¯, ¡¯white¡¯, ¡¯white¡¯]
>>> last(urn)
¡¯black¡¯
"""
# create a new list containing the elements of the given sequence, so that
# we can remove elements with changing the original sequence
    urn = list(urn)
# repeat the procedure to remove marbles from the urn, until a single marble
# remains
    while len(urn) > 1:
        marble1, marble2 = pick(urn)
        remove(marble1, marble2, urn)
# return the color of the last remaining marble
    return urn[0]
# there exists an alternative solution that only requires a single line and
# does not require to call the previous functions
#
# return ¡¯white¡¯ if urn.count(¡¯white¡¯ % 2) else ¡¯black¡¯
#
# to understand this solution, you need to make the following observation:
# the number of white marbles in the urn remains unchanged in the first two
# cases, and it drops by two in the third; that means its parity never
# changes; if the initial number of white marbles is odd, it must remain odd
# throughout, and the last ball can¡¯t avoid being white; by the same
# principle, if the urn originally contains an even number of white balls,
# the last ball will be black
if __name__ == ¡¯__main__¡¯:
import doctest
doctest.testmod()