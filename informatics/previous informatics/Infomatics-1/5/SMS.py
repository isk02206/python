'''
Created on 2015. 12. 3.

@author: User
'''
5.5 SMS language
def removeDuplicates(word):
"""
>>> removeDuplicates(¡¯bookkeeper¡¯)
¡¯bokeper¡¯
>>> removeDuplicates(¡¯Aardvark¡¯)
¡¯Ardvark¡¯
>>> removeDuplicates(¡¯eELGRASS¡¯)
¡¯eLGRAS¡¯
"""
result = ¡¯¡¯
for letter in word:
# remark: we make use of slicing to extract the last letter of the
# result, because slicing does not generate an error in case
# the result is still the empty string; using plain indexing
# given an index out of bound error
if letter.upper() != result[-1:].upper():
result += letter
return result
def removeVowels(word):
"""
>>> removeVowels(¡¯bookkeeper¡¯)
¡¯bkkpr¡¯
>>> removeVowels(¡¯Aardvark¡¯)
¡¯Ardvrk¡¯
>>> removeVowels(¡¯eELGRASS¡¯)
¡¯eLGRSS¡¯
"""
return word[:1] + ¡¯¡¯.join(
letter for letter in word[1:]
if letter.lower() not in ¡¯aeiou¡¯
)
def txtWord(word):
"""
>>> txtWord(¡¯Some¡¯)
¡¯Sm¡¯
>>> txtWord(¡¯people¡¯)
¡¯ppl¡¯
>>> txtWord(¡¯compress¡¯)
¡¯cmprs¡¯
>>> txtWord(¡¯text¡¯)
¡¯txt¡¯
>>> txtWord(¡¯messages¡¯)
¡¯msgs¡¯
"""
return removeVowels(removeDuplicates(word))
def txtSentence(sentence):
"""
>>> txtSentence(¡¯And now for something completely different!¡¯)
¡¯And nw fr smthng cmpltly dfrnt!¡¯
17
>>> txtSentence(¡¯Some people compress text messages by replacing doubled letters with
single letters and by retaining only those vowels that begin a word.¡¯)
¡¯Sm ppl cmprs txt msgs by rplcng dbld ltrs wth sngl ltrs and by rtnng only ths vwls tht
bgn a wrd.¡¯
"""
result, word = ¡¯¡¯, ¡¯¡¯
for character in sentence:
if character.isalpha():
word += character
else:
if word:
result += txtWord(word)
result += character
word = ¡¯¡¯
if word:
result += txtWord(word)
return result
if __name__ == ¡¯__main__¡¯:
import doctest
doctest.testmod()
