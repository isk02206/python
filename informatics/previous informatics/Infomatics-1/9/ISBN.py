'''
Created on 2015. 12. 3.

@author: User
'''
def isISBN13(code):
"""
Checks whether or not the given ISBN-13 code is valid.
>>> isISBN13(¡¯9789743159664¡¯)
True
>>> isISBN13(¡¯9787954527409¡¯)
False
>>> isISBN13(¡¯8799743159665¡¯)
False
"""
def checkdigit(code):
"""
Helper function to compute the ISBN-13 check digit
"""
# compute the check digit
check = sum((2 * (i % 2) + 1) * int(code[i]) for i in range(12))
# convert the check digit into a single digit
return str((10 - check) % 10)
# check whether the given code is a string
if not isinstance(code, str):
return False
# check whether the given code contains 10 characters
if len(code) != 13:
return False
# check prefix of the given code
if code[:3] not in {¡¯978¡¯, ¡¯979¡¯}:
return False
# check whether first nine characters of the given code are digits
if not code[:12].isdigit():
return False
# check the check digit
return checkdigit(code) == code[-1]
def remove_tags(s):
"""
Removes all XML tags from the given string and then removes leading and
trailing whitespace.
>>> remove_tags(¡¯ <Title> The Practice of Computing using <b>Python</b> </Title> ¡¯)
¡¯The Practice of Computing using Python¡¯
"""
# removes all XML tags from the given string
s = s.strip()
while s.find(¡¯<¡¯) >= 0:
start = s.find(¡¯<¡¯)
43
stop = s.find(¡¯>¡¯)
if stop == -1:
stop = len(s)
s = s[:start] + s[stop+1:]
# removes leading and trailing whitespace and returns the modified string
return s.strip()
def displayBookInfo(code):
"""
>>> displayBookInfo(¡¯9780136110675¡¯)
Title: The Practice of Computing using Python
Authors: William F Punch, Richard Enbody
Publisher: Addison Wesley
>>> displayBookInfo(¡¯9780136110678¡¯)
Wrong ISBN-13 code
"""
# check validity of ISBN-13 code
if not isISBN13(code):
print(¡¯Wrong ISBN-13 code¡¯)
return
# open web page with URL of ISBNdb.com that provides information about a
# given ISBN-13 code
import urllib.request
url = ¡¯http://isbndb.com/api/books.xml¡¯
parameters = ¡¯?access_key=ZFD8L2Z5&index1=isbn&value1=¡¯ + code.strip()
info = urllib.request.urlopen(url + parameters)
# extract and output selected book information from XML
for line in info:
line = line.decode(¡¯utf-8¡¯)
if line.startswith(¡¯<Title>¡¯):
print(¡¯Title: {}¡¯.format(remove_tags(line)))
elif line.startswith(¡¯<AuthorsText>¡¯):
print(¡¯Authors: {}¡¯.format(remove_tags(line).rstrip(¡¯, ¡¯)))
elif line.startswith(¡¯<PublisherText ¡¯):
print(¡¯Publisher: {}¡¯.format(remove_tags(line).rstrip(¡¯, ¡¯)))
# close web page
info.close()
if __name__ == ¡¯__main__¡¯:
import doctest
doctest.testmod()
