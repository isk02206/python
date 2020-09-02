'''
Created on 2015. 12. 2.

@author: USER
'''
def decomposition(name):
    """
    >>> decomposition(�섺��)
    (�섺��, �쇺��)
    >>> decomposition(�섻m7��)
    (�섻��, �셫7��)
    >>> decomposition(�섵#maj7��)
    (�섵#��, �셫aj7��)
    """
    # lookup starting position of chord symbol
    position = 2 if len(name) > 1 and name[1] == '#' else 1
    # return base note and chord symbol
    return name[:position], name[position:]
    
def notes(baseNote, tones):
    """
    >>> notes(�섺��, [0, 4, 7])
    [�섺��, �섲��, �섴��]
    >>> notes(�섻��, [0, 3, 7, 10])
    [�섻��, �섲#��, �섵��, �섺��]
    >>> notes(�섵#��, [0, 4, 7, 11])
    [�섵#��, �섻��, �섲#��, �섵��]
    """
    # define chromatic scale
    chromaticScale = 'C C# D D# E F F# G G# A A# B'.split()
    # lookup position of base note in chromatic scale
    baseNote = chromaticScale.index(baseNote)
    # return tones of chord as a list
    return [
        chromaticScale[(baseNote + tone) % len(chromaticScale)]
        for tone in tones
    ]

def chord(name, chordTypes, chordSymbols):
    """
    >>> chordTypes = {�셫ajor��:[0, 4, 7], �셫inor��:[0, 3, 7], �셝ominant seventh��:[0, 4, 7, 10],
    �셫inor seventh��:[0, 3, 7, 10], �셫ajor seventh��:[0, 4, 7, 11]}
    >>> chordSymbols = {�쇺��:�셫ajor��, �셫��:�셫inor��, ��7��:�셝ominant seventh��, �셫7��:�셫inor seventh��,
    �셫aj7��:�셫ajor seventh��}
    >>> chord(�섺��, chordTypes, chordSymbols)
    (�섺��, �섲��, �섴��)
    >>> chord(�섻m7��, chordTypes, chordSymbols)
    (�섻��, �섲#��, �섵��, �섺��)
    >>> chord(�섵#maj7��, chordTypes, chordSymbols)
    (�섵#��, �섻��, �섲#��, �섵��)
    """
    # decompose name of chord into base tone and chord symbol
    baseNote, chordSymbol = decomposition(name)
    # convert chord symbol into chord type
    chordType = chordSymbols[chordSymbol]
    # return notes of chord as tuple
    return tuple(notes(baseNote, chordTypes[chordType]))