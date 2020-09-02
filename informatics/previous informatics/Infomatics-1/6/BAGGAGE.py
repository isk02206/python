'''
Created on 2015. 12. 3.

@author: User
'''

6.5 Baggage carousel
def carousel(positions, suitcases):
"""
>>> carousel(8, ¡¯ABCDE¡¯)
[¡¯E¡¯, ¡¯A¡¯, None, ¡¯D¡¯, ¡¯B¡¯, None, None, ¡¯C¡¯]
>>> carousel(5, ¡¯ABCDE¡¯)
[¡¯E¡¯, ¡¯C¡¯, ¡¯B¡¯, ¡¯D¡¯, ¡¯A¡¯]
>>> carousel(5, ¡¯ABCDEFGH¡¯)
Traceback (most recent call last):
AssertionError: invalid arguments
>>> carousel(5, ¡¯ABA¡¯)
Traceback (most recent call last):
AssertionError: invalid arguments
"""
assert len(suitcases) <= positions, ¡¯invalid arguments¡¯
assert len(suitcases) == len(set(suitcases)), ¡¯invalid arguments¡¯
# create an empty carousel
carousel = [None] * positions
# initialize starting position (actually it doesn¡¯t really matter where
# placement of suitcases starts, since we will adjust the reference position
# at the end of this function)
position = -1
# place each suitcase on the carousel
for suitcase in suitcases:
# find the third empty space on the carousel
for _ in range(3):
# find the next empty space on the carousel
position = (position + 1) % positions
while carousel[position] is not None:
position = (position + 1) % positions
# place next suitcase on the third empty space on the carousel
carousel[position] = suitcase
# make sure the last suitcase placed on the carousel is at the first
# position of the list representing the carousel
carousel = carousel[position:] + carousel[:position]
return carousel
def rotated(carousel1, carousel2):
23
"""
>>> rotated([¡¯E¡¯, ¡¯A¡¯, None, ¡¯D¡¯, ¡¯B¡¯, None, None, ¡¯C¡¯], [¡¯B¡¯, None, None, ¡¯C¡¯, ¡¯E¡¯, ¡¯A¡¯,
None, ¡¯D¡¯])
True
>>> rotated([¡¯E¡¯, ¡¯A¡¯, None, ¡¯D¡¯, ¡¯B¡¯, None, None, ¡¯C¡¯], [¡¯B¡¯, None, None, ¡¯A¡¯, ¡¯E¡¯, ¡¯C¡¯,
None, ¡¯D¡¯])
False
>>> rotated([¡¯E¡¯, ¡¯A¡¯, None, ¡¯D¡¯, ¡¯B¡¯, None, None, ¡¯C¡¯], [¡¯C¡¯, ¡¯E¡¯, ¡¯A¡¯, None, ¡¯D¡¯, ¡¯B¡¯])
False
"""
# check whether carousels have equal length
if len(carousel1) != len(carousel2):
return False
# check whether carousels contain the same suitcases
suitcases1 = {suitcase for suitcase in carousel1 if suitcase is not None}
suitcases2 = {suitcase for suitcase in carousel2 if suitcase is not None}
if suitcases1 != suitcases2:
return False
# if there are suitcases on the carousels, check whether they are positioned
# in the same order
if suitcases1:
# select a random suitcase as a reference point
suitcase = list(suitcases1).pop()
# determine position of the suitcase on both carousels
start1 = carousel1.index(suitcase)
start2 = carousel2.index(suitcase)
# check whether the order of the suitcases on both carousels is the same
# if corresponding positions relative against the position of the chosen
# suitcase are compared
for position in range(len(carousel1)):
if (
carousel1[(start1 + position) % len(carousel1)] !=
carousel2[(start2 + position) % len(carousel2)]
):
return False
# all conditions for equivalence have been met
return True
if __name__ == ¡¯__main__¡¯:
import doctest
doctest.testmod()
