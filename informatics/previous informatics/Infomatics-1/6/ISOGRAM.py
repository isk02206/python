'''
Created on 2015. 12. 3.

@author: User
'''
6.2 Isograms
def occurrences(word):
"""
>>> occurrences(¡¯ambidextrously¡¯)
[1, 1, 0, 1, 1, 0, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 0]
>>> occurrences(¡¯DOCTORWHO¡¯)
[0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 3, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0]
>>> occurrences(¡¯uncopyrightable¡¯)
[1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 0, 0, 0, 1, 0]
"""
# determine a list containing the number of occurrence in the given word of
# each letter in the alphabet
freq = [0] * 26
for letter in word.lower():
freq[ord(letter) - ord(¡¯a¡¯)] += 1
# return the list of occurrences
return freq
def isogram(word):
"""
>>> isogram(¡¯ambidextrously¡¯)
True
>>> isogram(¡¯DOCTORWHO¡¯)
20
False
>>> isogram(¡¯uncopyrightable¡¯)
True
"""
# check whether there are no repeated letters in the given word
return max(occurrences(word)) < 2
def anagram(word1, word2):
"""
>>> anagram(¡¯DOCTORWHO¡¯, ¡¯Torchwood¡¯)
True
>>> anagram(¡¯isogram¡¯, ¡¯anagram¡¯)
False
>>> anagram(¡¯Aristotelian¡¯, ¡¯retaliations¡¯)
True
"""
# anagrams: words having the same letter frequencies
return occurrences(word1) == occurrences(word2)
if __name__ == ¡¯__main__¡¯:
import doctest
doctest.testmod()
6.3 N50
def median(collection):
"""
returns the median of a given collection of numbers
>>> median((2, 2, 2, 3, 3, 4, 8, 8))
3.0
"""
collection = sorted(collection)
if len(collection) % 2:
return float(collection[len(collection) // 2])
else:
middle = len(collection) // 2
return (collection[middle - 1] + collection[middle]) / 2
def extend(collection):
"""
returns the extended list in wich each value n from the given collection
is added n times
>>> contigs = (2, 2, 2, 3, 3, 4, 8, 8)
>>> extend(contigs)
[2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8,
8, 8]
"""
extended = []
for number in collection:
extended += [number] * number
return extended
def N50(collection):
"""
computes the N50 statistic as the median of the extended list
21
>>> contigs = (2, 2, 2, 3, 3, 4, 8, 8)
>>> N50_median(contigs)
6.0
"""
return median(extend(collection))
if __name__ == ¡¯__main__¡¯:
import doctest
doctest.testmod()
