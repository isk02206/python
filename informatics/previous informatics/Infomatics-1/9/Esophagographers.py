'''
Created on 2015. 12. 3.

@author: User
'''
def occurrences(word):
"""
>>> occurrences(¡¯CHACHACHA¡¯)
{¡¯a¡¯: 3, ¡¯h¡¯: 3, ¡¯c¡¯: 3}
>>> occurrences(¡¯Esophagographers¡¯)
{¡¯a¡¯: 2, ¡¯e¡¯: 2, ¡¯g¡¯: 2, ¡¯h¡¯: 2, ¡¯o¡¯: 2, ¡¯p¡¯: 2, ¡¯s¡¯: 2, ¡¯r¡¯: 2}
>>> occurrences(¡¯happenchance¡¯)
{¡¯a¡¯: 2, ¡¯c¡¯: 2, ¡¯e¡¯: 2, ¡¯h¡¯: 2, ¡¯n¡¯: 2, ¡¯p¡¯: 2}
"""
# create a dictionary that maps each letter in the given word onto the
# number of occurrences of that letter in the word
freq = {}
for character in word.lower():
if character.isalpha():
freq[character] = freq.get(character, 0) + 1
44
# return the dictionary of occurrences
return freq
def isRepetitionWord(word, minimal_repetition=1):
"""
>>> isRepetitionWord(¡¯CHACHACHA¡¯)
True
>>> isRepetitionWord(¡¯Esophagographers¡¯)
True
>>> isRepetitionWord(¡¯happenchance¡¯, minimal_repetition=3)
False
"""
# determine the set of the number of occurrences of all letters in the word
repetitions = set(occurrences(word).values())
# determine whether all letters have the same occurrence and whether these
# occurrences are greater then or equal to the given minimal number of
# occurrences
return (
len(repetitions) == 1 and
repetitions.pop() >= minimal_repetition
)
def repetitionWords(filename, minimal_repetition=1, minimal_length=1):
"""
>>> repetitionWords(¡¯words.txt¡¯, minimal_repetition=2, minimal_length=10)
{¡¯horseshoer¡¯, ¡¯intestines¡¯}
"""
# open the given file
fl = open(filename, ¡¯r¡¯)
# traverse all words in the given file and add the repetition words that are
# long enough to a file (set comprehension)
return {
line.strip() # remove newlines
for line in fl # traverse all lines
if (
len(line.strip()) >= minimal_length and
isRepetitionWord(line, minimal_repetition)
)
}
if __name__ == ¡¯__main__¡¯:
    import doctest
doctest.testmod()