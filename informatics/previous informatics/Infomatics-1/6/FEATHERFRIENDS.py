'''
Created on 2015. 12. 3.

@author: User
'''
6.6 Feathered friends
def coord2label(row, col):
"""
>>> coord2label(0, 0)
¡¯A1¡¯
>>> coord2label(1, 5)
¡¯B6¡¯
>>> coord2label(7, 4)
¡¯H5¡¯
"""
# convert row index to corresponding letter and add one to column index
return chr(ord(¡¯A¡¯) + row) + str(col + 1)
def label2coord(label):
24
"""
>>> label2coord(¡¯A1¡¯)
(0, 0)
>>> label2coord(¡¯B6¡¯)
(1, 5)
>>> label2coord(¡¯H5¡¯)
(7, 4)
"""
# determine position of first digit in the label
pos = 0
while not label[pos].isdigit():
pos += 1
# convert letter of row index to corresponding position in the alphabet
row = ord(label[:pos]) - ord(¡¯A¡¯)
# subtract one from column index
col = int(label[pos:]) - 1
# return tuple containing row and column index
return row, col
def columns(rows, environment):
# check whether length of environment is divisible by the given number of
# rows; if this is not the case, an AssertionError is raised
assert not(len(environment) % rows), ¡¯ongeldige argumenten¡¯
# return number of columns
return len(environment) // rows
def observation(rows, environment, label):
"""
>>> observation(2, ¡¯abaabcabaabc¡¯, ¡¯A1¡¯)
¡¯a¡¯
>>> observation(2, ¡¯abaabcabaabc¡¯, ¡¯B6¡¯)
¡¯c¡¯
>>> observation(2, ¡¯abaabcabaabc¡¯, ¡¯H5¡¯)
Traceback (most recent call last):
AssertionError: ongeldige argumenten
"""
# determine number of columns
cols = columns(rows, environment)
# check whether given cell exists in grid
row, col = label2coord(label)
assert 0 <= row < rows, ¡¯ongeldige argumenten¡¯
assert 0 <= col < cols, ¡¯ongeldige argumenten¡¯
# return letter at given position
return environment[row * cols + col]
def endpoint(rows, environment, startpoint, route):
"""
>>> endpoint(2, ¡¯abaabcabaabc¡¯, ¡¯A5¡¯, ¡¯bLaLa¡¯)
¡¯A3¡¯
>>> endpoint(2, ¡¯abcdeecdea¡¯, ¡¯B4¡¯, ¡¯eLdLcUb¡¯)
¡¯A2¡¯
>>> endpoint(2, ¡¯abcdeecdea¡¯, ¡¯A3¡¯, ¡¯cRdUcLbLaDa¡¯)
"""
# check whether route has an odd number of characters
assert len(route) % 2, ¡¯ongeldige argumenten¡¯
25
# determine row and column index of starting point in grid
row, col = label2coord(startpoint)
# determine number of columns
cols = columns(rows, environment)
# define possible movements
directions = {¡¯L¡¯:(0, -1), ¡¯R¡¯:(0, 1), ¡¯U¡¯:(-1, 0), ¡¯D¡¯:(1, 0)}
# traverse route to see whether it can be followed completely from the
# given starting point
for index, letter in enumerate(route):
if index % 2:
# move in the direction indicated by the letter, if this would not
# lead to a position outside the map
dr, dk = directions[letter]
if 0 <= row + dr < rows and 0 <= col + dk < cols:
row, col = row + dr, col + dk
else:
# check whether observation at current position corresponds to the
# observation indicated by the letter
if observation(rows, environment, coord2label(row, col)) != letter:
return None
# route could be followed completely -> return end point
return coord2label(row, col)
def beehives(rows, environment, route):
"""
>>> beehives(2, ¡¯abaabcabaabc¡¯, ¡¯bLaLa¡¯)
[¡¯A1¡¯, ¡¯A3¡¯, ¡¯B1¡¯, ¡¯B3¡¯]
>>> beehives(2, ¡¯abcdeecdea¡¯, ¡¯eLdLcUb¡¯)
[¡¯A2¡¯]
>>> beehives(2, ¡¯abcdeecdea¡¯, ¡¯cRdUcLbLaDa¡¯)
[]
"""
# check whether route has an odd number of characters
assert len(route) % 2, ¡¯ongeldige argumenten¡¯
# determine number of columns
cols = columns(rows, environment)
# traverse all cells as candidate starting positions; check whether route
# can be completely followed for each individual starting position; add
# end point of route to the set of end points if this were the case
positions = set()
for row in range(rows):
for col in range(cols):
label = endpoint(rows, environment, coord2label(row, col), route)
if label is not None:
positions.add(label)
# return sorted list of positions
return sorted(positions)
if __name__ == ¡¯__main__¡¯:
import doctest
doctest.testmod()