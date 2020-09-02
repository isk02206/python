'''
Created on 2015. 12. 3.

@author: User
'''

5.2 Solresol
12
def isSolresol(word):
"""
Returns a Boolean value that indicates whether or not the given word meets
the grammar rules of Solresol.
>>> isSolresol(¡¯doresol¡¯)
True
>>> isSolresol(¡¯doreso¡¯)
False
>>> isSolresol(¡¯salami¡¯)
False
"""
index = 0 # position in word
syllables = 0 # number of syllables
# traverse and analyse syllables
while index < len(word):
# check whether the number of syllables is not too large
if syllables == 5:
return False
# check whether syllable represents music note and jump forward to the
# next syllably in the word
if word[index:index + 2] in {¡¯do¡¯, ¡¯re¡¯, ¡¯mi¡¯, ¡¯fa¡¯, ¡¯la¡¯, ¡¯si¡¯}:
index += 2
elif word[index:index + 3] == ¡¯sol¡¯:
index += 3
else:
# syllable does not represent a music note
return False
# increment the number of syllables
syllables += 1
# word meets all grammar rules of Solresol
return True
def shorthand(word):
"""
Returns the shorthand of the given Solresol word.
>>> shorthand(¡¯fala¡¯)
¡¯fl¡¯
>>> shorthand(¡¯doremi¡¯)
¡¯drm¡¯
>>> shorthand(¡¯doresol¡¯)
¡¯drso¡¯
"""
# initialize position in word and shorthand
index, shorthand = 0, ¡¯¡¯
# traverse and abbreviate syllables
while index < len(word):
if word[index:].startswith(¡¯so¡¯):
shorthand += ¡¯so¡¯
index += 3
else:
shorthand += word[index]
index += 2
# return abbreviated word
return shorthand
def opposite(word):
13
"""
Returns the opposite of the given Solresol word.
>>> opposite(¡¯fala¡¯)
¡¯lafa¡¯
>>> opposite(¡¯doremi¡¯)
¡¯miredo¡¯
>>> opposite(¡¯doresol¡¯)
¡¯solredo¡¯
"""
# initialize position in word and opposite word
index, opposite = 0, ¡¯¡¯
# traverse syllables and prepend to opposite word
while index < len(word):
if word[index:].startswith(¡¯sol¡¯):
opposite = ¡¯sol¡¯ + opposite
index += 3
else:
opposite = word[index:index + 2] + opposite
index += 2
# return opposite word
return opposite
if __name__ == ¡¯__main__¡¯:
import doctest
doctest.testmod()
