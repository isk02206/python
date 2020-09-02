'''
Created on 2015. 12. 3.

@author: User
'''
def lettervalue(values):
"""
>>> penstrokes = [3, 3, 1, 2, 4, 3, 2, 3, 1, 2, 3, 2, 4, 3, 1, 2, 2, 3, 1, 2, 1, 2, 4, 2,
3, 3]
>>> value = lettervalue(penstrokes)
>>> value[¡¯L¡¯]
2
>>> value[¡¯U¡¯]
1
>>> value[¡¯C¡¯]
1
>>> value[¡¯K¡¯]
3
"""
# check whether the list has 26 elements
assert len(values) == 26, ¡¯lijst moet 26 getallen bevatten¡¯
# convert list into dictionary that maps each letter in the alphabet to its
# corresponding value in the list
return {
chr(index + ord(¡¯A¡¯)): value
for index, value in enumerate(values)
}
def wordvalue(word, values):
37
"""
>>> penstrokes = [3, 3, 1, 2, 4, 3, 2, 3, 1, 2, 3, 2, 4, 3, 1, 2, 2, 3, 1, 2, 1, 2, 4, 2,
3, 3]
>>> wordvalue(¡¯LUCK¡¯, penstrokes)
7
>>> wordvalue(¡¯blackjack¡¯, penstrokes)
21
>>> wordvalue(¡¯FREEZING POINT¡¯, penstrokes)
32
>>> wordvalue(¡¯Hours in a Day¡¯, penstrokes)
24
>>> wordvalue(¡¯Twenty-nine¡¯, penstrokes)
29
>>> braille = (1, 2, 2, 3, 2, 3, 4, 3, 2, 3, 2, 3, 3, 4, 3, 4, 5, 4, 3, 4, 3, 4, 4, 4, 5,
4)
>>> wordvalue(¡¯TEN¡¯, braille)
10
>>> wordvalue(¡¯ten + ten¡¯, braille)
20
>>> morse = [2, 4, 4, 3, 1, 4, 3, 4, 2, 4, 3, 4, 2, 2, 3, 4, 4, 3, 3, 1, 3, 4, 3, 4, 4, 4]
>>> wordvalue(¡¯fifteen¡¯, morse)
15
>>> wordvalue(¡¯Se7en¡¯, morse)
7
>>> scrabble = (1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8,
4, 10)
>>> wordvalue(¡¯TWELVE¡¯, scrabble)
12
>>> wordvalue(¡¯Life, Universe and Everything¡¯, scrabble)
42
"""
# convert given list into a dictionary
value = lettervalue(values)
# compute sum of values of all letters in the given word
return sum(
value[letter]
for letter in word.upper()
if letter.isalpha()
)
if __name__ == ¡¯__main__¡¯:
import doctest
doctest.testmod()
