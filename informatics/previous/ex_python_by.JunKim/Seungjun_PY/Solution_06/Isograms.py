'''
Created on 2015. 12. 1.

@author: USER
'''
def occurrences(word):
    """
    >>> occurrences('ambidextrously')
    [1, 1, 0, 1, 1, 0, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 0]
    >>> occurrences('DOCTORWHO')
    [0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 3, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0]
    >>> occurrences('uncopyrightable')
    [1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 0, 0, 0, 1, 0]
    """
    # determine a list containing the number of occurrence in the given word of
    # each letter in the alphabet
    freq = [0] * 26
    for letter in word.lower():
        freq[ord(letter) - ord('a')] += 1
    # return the list of occurrences
    return freq
def isogram(word):
    """
    >>> isogram('ambidextrously')
    True
    >>> isogram('DOCTORWHO')
    20
    False
    >>> isogram('uncopyrightable')
    True
    """
    # check whether there are no repeated letters in the given word
    return max(occurrences(word)) < 2
def anagram(word1, word2):
    """
    >>> anagram('DOCTORWHO', 'Torchwood')
    True
    >>> anagram('isogram', 'anagram')
    False
    >>> anagram('Aristotelian', 'retaliations')
    True
    """
    # anagrams: words having the same letter frequencies
    return occurrences(word1) == occurrences(word2)
if __name__ == '__main__':
    import doctest
    doctest.testmod()
