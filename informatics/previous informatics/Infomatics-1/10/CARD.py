'''
Created on 2015. 12. 3.

@author: User
'''
10.5 Card dressage
class CardDressage:
"""
>>> game = CardDressage(5, 3)
>>> print(game)
###
###
###
###
###
>>> game.turnCard(1)
>>> game
--#
-##
###
###
###
>>> game.won()
False
>>> game.turnCard(3)
>>> game
-#-
-#-
###
###
###
>>> game.won()
False
>>> game.turnCard(16)
Traceback (most recent call last):
AssertionError: invalid card number
>>> game.turnCard(0)
Traceback (most recent call last):
AssertionError: invalid card number
>>> game.turnCards([5, 7, 9, 14])
>>> game
---
---
---
---
---
>>> game.won()
True
>>> game = CardDressage(5)
>>> game.turnCards([18, 13, 9, 11, 21, 24, 12, 7, 17, 5, 4, 6, 19, 23, 10])
>>> game
-----
-----
-----
-----
-----
>>> game.won()
True
>>> game = CardDressage(3, 6)
>>> game.turnCards((1, 5, 9, 8, 6, 10))
57
>>> game
-#-###
##-##-
#---##
>>> game.won()
False
"""
def __init__(self, rows, cols=None):
# equal number of rows and columns if only the number of rows is passed
if cols is None:
cols = rows
# assign number of rows and columns as object attributes
self.rows = rows
self.cols = cols
# initialize cards arranged in a grid; on each position a Boolean value
# True indicates that the card is face down and the Boolean value False
# indicates that the card is face up
self.cards = [[True for _ in range(cols)] for _ in range(rows)]
def __str__(self):
# convert each row of cards to a single string, and then concatenate
# these strins into the lines of a multiline string
return ¡¯\n¡¯.join(
¡¯¡¯.join(¡¯#¡¯ if card else ¡¯-¡¯ for card in row)
for row in self.cards
)
def __repr__(self):
# both string representation methods should return the same value
return str(self)
def turnCard(self, card):
# helper function that converts the given index of a card to its row and
# column index in the grid of cards
def pos2rowcol(pos, cols):
# determine row and column index
row = (pos - 1) // cols
col = (pos - 1) % cols
# return row and column index
return row, col
assert 1 <= card <= self.rows * self.cols, ¡¯invalid card number¡¯
# determine row and column index of card
row, col = pos2rowcol(card, self.cols)
# turn card and all its neighbours
for dr, dc in ((0, 0), (1, 0), (-1, 0), (0, 1), (0, -1)):
if 0 <= row + dr < self.rows and 0 <= col + dc < self.cols:
self.cards[row + dr][col + dc] = not self.cards[row + dr][col + dc]
def turnCards(self, cards):
# turn series of cards in the given order
for card in cards:
self.turnCard(card)
def won(self):
return all(all(not card for card in row) for row in self.cards)
58
if __name__ == ¡¯__main__¡¯:
import doctest
doctest.testmod()
