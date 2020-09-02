'''
Created on 2015. 12. 3.

@author: User
'''
10.4 Cowsay
class Cowsay:
"""
>>> quote = Cowsay([’Moo may represent an idea,’, ’but only the cow knows.’])
>>> quote
+----------------------------+
| Moo may represent an idea, |
| but only the cow knows. |
+----------------------------+
>>> print(quote)
+----------------------------+
| Moo may represent an idea, |
| but only the cow knows. |
+----------------------------+
\\ ˆ__ˆ
\\ (oo)\\_______
(__)\\ )\\/\\
||----w |
|| ||
>>> quote.setEyes(33)
Traceback (most recent call last):
AssertionError: invalid eyes
>>> quote.setEyes(’***’)
Traceback (most recent call last):
AssertionError: invalid eyes
>>> quote.setEyes(’ˆˆ’)
>>> print(quote)
+----------------------------+
| Moo may represent an idea, |
| but only the cow knows. |
+----------------------------+
\\ ˆ__ˆ
\\ (ˆˆ)\\_______
(__)\\ )\\/\\
55
||----w |
|| ||
>>> quote.setImage(’tux.cow’)
>>> print(quote)
+----------------------------+
| Moo may represent an idea, |
| but only the cow knows. |
+----------------------------+
\\
\\
.--.
|ˆ_ˆ |
|:_/ |
// \\ \\
(| | )
/’\\_ _/‘\\
\___)=(___/
"""
def __init__(self, message):
# set default value for eyes
self.setEyes(’oo’)
# set default value for image
self.setImage(’cow.cow’)
# set given message
self.lines = message
def __repr__(self):
# determine width of longest line in given message
width = max(len(line) for line in self.lines)
# formatting of top and bottom border
border = ’+’ + ’-’ * (width + 2) + ’+’
# add top border to output
lines = [border]
# add centered lines of message to output
for line in self.lines:
lines.append(’| {} |’.format(line.center(width)))
# add bottom border to output
lines.append(border)
# compose output as a series of lines
return ’\n’.join(lines)
def setImage(self, bestandsnaam):
# set new image
self.image = open(bestandsnaam, ’r’).read().rstrip(’\n’)
def setEyes(self, eyes):
# check whether given eyes is a 2-character string
assert isinstance(eyes, str) and len(eyes) == 2, ’invalid eyes’
# set new pair of eyes
self.eyes = eyes
def __str__(self):
# compose output of repr with the image of object that is given the eyes
# of the object
return (
56
’{!r}\n’.format(self) +
self.image.format(self.eyes[0], self.eyes[1])
)
if __name__ == ’__main__’:
import doctest
doctest.testmod()
