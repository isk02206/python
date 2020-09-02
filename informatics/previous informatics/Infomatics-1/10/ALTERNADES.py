'''
Created on 2015. 12. 3.

@author: User
'''
10.3 Alternades
class Alternade:
"""
>>> word1 = Alternade(¡¯SHOE¡¯)
>>> word1.words
[¡¯SHOE¡¯]
>>> word1
Alternade(¡¯SHOE¡¯)
>>> print(word1)
SHOE
>>> words = [¡¯COLD¡¯]
>>> word2 = Alternade(words)
>>> word2.words
[¡¯COLD¡¯]
>>> id(words) != id(word2.words)
True
>>> word2
Alternade(¡¯COLD¡¯)
>>> word3 = word1 + word2
>>> isinstance(word3, Alternade)
True
>>> word3.words
[¡¯SHOE¡¯, ¡¯COLD¡¯]
>>> word3
Alternade([¡¯SHOE¡¯, ¡¯COLD¡¯])
>>> print(word3)
SCHOOLED
>>> word1
Alternade(¡¯SHOE¡¯)
>>> word2
Alternade(¡¯COLD¡¯)
>>> word4 = Alternade(¡¯DEMO¡¯) + Alternade(¡¯RABAT¡¯)
>>> word4
Alternade([¡¯DEMO¡¯, ¡¯RABAT¡¯])
>>> print(word4)
DREAMBOAT
>>> word5 = Alternade(¡¯SIR¡¯) + Alternade(¡¯ILL¡¯) + Alternade(¡¯MAY¡¯)
>>> word5.words
[¡¯SIR¡¯, ¡¯ILL¡¯, ¡¯MAY¡¯]
>>> word5
Alternade([¡¯SIR¡¯, ¡¯ILL¡¯, ¡¯MAY¡¯])
>>> print(word5)
SIMILARLY
"""
def __init__(self, words):
# assign a copy of the given list of words or a new list cohtaining the
# given word to the property words of the newly created object
54
self.words = list(words) if isinstance(words, list) else [words]
def __repr__(self):
# format Python expression that creates a new object of the class
# Alternade having the same status as the current object
return ¡¯{}({!r})¡¯.format(
self.__class__.__name__,
self.words[0] if len(self.words) == 1 else self.words
)
def __str__(self):
# interleave letters of the list of words
from itertools import zip_longest
return ¡¯¡¯.join(
¡¯¡¯.join(letters)
for letters in zip_longest(*self.words, fillvalue=¡¯¡¯)
)
def __add__(self, other):
# create new object of the class Alternade having a word list that
# results from concatenating the word lists of the two operandi of the
# addition
return Alternade(self.words + other.words)
if __name__ == ¡¯__main__¡¯:
import doctest
doctest.testmod()
