'''
Created on 2015. 12. 2.

@author: USER
'''
def lettervalue(values):
    """
    >>> penstrokes = [3, 3, 1, 2, 4, 3, 2, 3, 1, 2, 3, 2, 4, 3, 1, 2, 2, 3, 1, 2, 1, 2, 4, 2,
    3, 3]
    >>> value = lettervalue(penstrokes)
    >>> value[�셂��]
    2
    >>> value[�셐��]
    1
    >>> value[�섴��]
    1
    >>> value[�셁��]
    3
    """
    # check whether the list has 26 elements
    assert len(values) == 26, 'lijst moet 26 getallen bevatten'
    # convert list into dictionary that maps each letter in the alphabet to its
    # corresponding value in the list
    return {chr(index + ord(�섲��)): value for index, value in enumerate(values)}

def wordvalue(word, values):
    """
    >>> penstrokes = [3, 3, 1, 2, 4, 3, 2, 3, 1, 2, 3, 2, 4, 3, 1, 2, 2, 3, 1, 2, 1, 2, 4, 2,
    3, 3]
    >>> wordvalue(�셂UCK��, penstrokes)
    7
    >>> wordvalue(�셚lackjack��, penstrokes)
    21
    >>> wordvalue(�섺REEZING POINT��, penstrokes)
    32
    >>> wordvalue(�섽ours in a Day��, penstrokes)
    24
    >>> wordvalue(�셏wenty-nine��, penstrokes)
    29
    >>> braille = (1, 2, 2, 3, 2, 3, 4, 3, 2, 3, 2, 3, 3, 4, 3, 4, 5, 4, 3, 4, 3, 4, 4, 4, 5,
    4)
    >>> wordvalue(�셏EN��, braille)
    10
    >>> wordvalue(�셳en + ten��, braille)
    20
    >>> morse = [2, 4, 4, 3, 1, 4, 3, 4, 2, 4, 3, 4, 2, 2, 3, 4, 4, 3, 3, 1, 3, 4, 3, 4, 4, 4]
    >>> wordvalue(�셟ifteen��, morse)
    15
    >>> wordvalue(�셎e7en��, morse)
    7
    >>> scrabble = (1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8,
    4, 10)
    >>> wordvalue(�셏WELVE��, scrabble)
    12
    >>> wordvalue(�셂ife, Universe and Everything��, scrabble)
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