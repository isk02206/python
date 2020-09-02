'''
Created on 2015. 12. 3.

@author: User
'''
10.6 Reservoir
class Reservoir:
"""
>>> profile = [4, 3, 2, 2, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 2, 5, 6, 5, 2, 2, 2, 3, 3, 3,
4, 5, 3, 2, 2]
>>> reservoir = Reservoir(profile)
>>> print(reservoir)
#
### #
# ### ##
## ### ######
#### ###############
###### #################
>>> reservoir.fill()
63
>>> print(reservoir)
#
###˜˜˜˜˜˜˜#
#˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜###˜˜˜˜˜˜##
##˜˜˜˜˜˜˜˜˜˜˜˜˜˜###˜˜˜######
####˜˜˜˜˜˜˜˜˜˜˜###############
######˜˜˜˜˜˜˜#################
>>> reservoir.drain()
63
>>> print(reservoir)
#
### #
# ### ##
## ### ######
#### ###############
###### #################
>>> reservoir.fill()
63
>>> print(reservoir)
#
###˜˜˜˜˜˜˜#
#˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜###˜˜˜˜˜˜##
##˜˜˜˜˜˜˜˜˜˜˜˜˜˜###˜˜˜######
####˜˜˜˜˜˜˜˜˜˜˜###############
######˜˜˜˜˜˜˜#################
>>> reservoir.penetrate()
47
>>> print(reservoir)
#
###˜˜˜˜˜˜˜#
# ###˜˜˜˜˜˜##
## ###˜˜˜######
#### ###############
###### #################
>>> reservoir.fill()
47
>>> print(reservoir)
#
###˜˜˜˜˜˜˜#
#˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜###˜˜˜˜˜˜##
##˜˜˜˜˜˜˜˜˜˜˜˜˜˜###˜˜˜######
####˜˜˜˜˜˜˜˜˜˜˜###############
######˜˜˜˜˜˜˜#################
>>> reservoir.drain()
63
59
>>> print(reservoir)
#
### #
# ### ##
## ### ######
#### ###############
###### #################
"""
def __init__(self, profile):
# derive height and width of grid representation from given profile
self.width = len(profile)
self.height = max(profile)
# build grid representation of reservoir based on given profile
self.reservoir = [
[
’#’ if row >= self.height - profile[col] else ’ ’
for col in range(self.width)
]
for row in range(self.height)
]
def __str__(self):
# convert grid representation into string represention
return ’\n’.join(’’.join(row) for row in self.reservoir)
def fill(self):
# keep last position of leftside on all heights
amount = 0
leftside = [None] * self.height
for col in range(self.width):
for row in range(self.height):
if self.reservoir[row][col] == ’#’:
# fill water until previous leftside
if leftside[row] is not None:
for kol2 in range(leftside[row] + 1, col):
if self.reservoir[row][kol2] == ’ ’:
amount += 1
self.reservoir[row][kol2] = ’˜’
# set new leftside
leftside[row] = col
# build string representation of filled grid
return amount
def drain(self):
# remove all water from the reservoir
amount = 0
for row in range(self.height):
for col in range(self.width):
if self.reservoir[row][col] == ’˜’:
amount += 1
self.reservoir[row][col] = ’ ’
return amount
def penetrate(self):
# mark all water that touches the ground to let it penetrate
remove = {
(self.height - 1, col) for col in range(self.width)
if self.reservoir[self.height - 1][col] == ’˜’
}
60
# let marked water penetrate and mark all neighbours left, right, above
# and below to let them penetrate
amount = 0
while remove:
# select a random area that has to be removed
row, col = remove.pop()
# delete the water of that area
amount += 1
self.reservoir[row][col] = ’ ’
# mark neighbours left, right and above to be removed if they
# contain water
for dr, dk in ((-1, 0), (0, 1), (0, -1)):
if (
0 <= row + dr < self.height and
0 <= col + dk < self.width and
self.reservoir[row + dr][col + dk] == ’˜’
):
remove.add((row + dr, col + dk))
return amount
if __name__ == ’__main__’:
import doctest
doctest.testmod()