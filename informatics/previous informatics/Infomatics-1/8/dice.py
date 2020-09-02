'''
Created on 2015. 12. 3.

@author: User
'''
8.3 Chords
def decomposition(name):
"""
>>> decomposition(¡¯F¡¯)
(¡¯F¡¯, ¡¯¡¯)
>>> decomposition(¡¯Gm7¡¯)
(¡¯G¡¯, ¡¯m7¡¯)
>>> decomposition(¡¯D#maj7¡¯)
(¡¯D#¡¯, ¡¯maj7¡¯)
"""
# lookup starting position of chord symbol
position = 2 if len(name) > 1 and name[1] == ¡¯#¡¯ else 1
# return base note and chord symbol
38
return name[:position], name[position:]
def notes(baseNote, tones):
"""
>>> notes(¡¯F¡¯, [0, 4, 7])
[¡¯F¡¯, ¡¯A¡¯, ¡¯C¡¯]
>>> notes(¡¯G¡¯, [0, 3, 7, 10])
[¡¯G¡¯, ¡¯A#¡¯, ¡¯D¡¯, ¡¯F¡¯]
>>> notes(¡¯D#¡¯, [0, 4, 7, 11])
[¡¯D#¡¯, ¡¯G¡¯, ¡¯A#¡¯, ¡¯D¡¯]
"""
# define chromatic scale
chromaticScale = ¡¯C C# D D# E F F# G G# A A# B¡¯.split()
# lookup position of base note in chromatic scale
baseNote = chromaticScale.index(baseNote)
# return tones of chord as a list
return [
chromaticScale[(baseNote + tone) % len(chromaticScale)]
for tone in tones
]
def chord(name, chordTypes, chordSymbols):
"""
>>> chordTypes = {¡¯major¡¯:[0, 4, 7], ¡¯minor¡¯:[0, 3, 7], ¡¯dominant seventh¡¯:[0, 4, 7, 10],
¡¯minor seventh¡¯:[0, 3, 7, 10], ¡¯major seventh¡¯:[0, 4, 7, 11]}
>>> chordSymbols = {¡¯¡¯:¡¯major¡¯, ¡¯m¡¯:¡¯minor¡¯, ¡¯7¡¯:¡¯dominant seventh¡¯, ¡¯m7¡¯:¡¯minor seventh¡¯,
¡¯maj7¡¯:¡¯major seventh¡¯}
>>> chord(¡¯F¡¯, chordTypes, chordSymbols)
(¡¯F¡¯, ¡¯A¡¯, ¡¯C¡¯)
>>> chord(¡¯Gm7¡¯, chordTypes, chordSymbols)
(¡¯G¡¯, ¡¯A#¡¯, ¡¯D¡¯, ¡¯F¡¯)
>>> chord(¡¯D#maj7¡¯, chordTypes, chordSymbols)
(¡¯D#¡¯, ¡¯G¡¯, ¡¯A#¡¯, ¡¯D¡¯)
"""
# decompose name of chord into base tone and chord symbol
baseNote, chordSymbol = decomposition(name)
# convert chord symbol into chord type
chordType = chordSymbols[chordSymbol]
# return notes of chord as tuple
return tuple(notes(baseNote, chordTypes[chordType]))
if __name__ == ¡¯__main__¡¯:
import doctest
doctest.testmod()