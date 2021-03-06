'''
Created on 2015. 12. 3.

@author: User
'''
def isISBN13(code):
"""
Checks whether or not the given ISBN-13 code is valid.
>>> isISBN13(��9789743159664��)
True
>>> isISBN13(��9787954527409��)
False
>>> isISBN13(��8799743159665��)
False
"""
def checkdigit(code):
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
if code[:3] not in {��978��, ��979��}:
return False
# check whether first nine characters of the given code are digits
if not code[:12].isdigit():
return False
# check the check digit
return checkdigit(code) == code[-1]
def overview(codes):
"""
>>> codes = [
... ��9789743159664��, ��9785301556616��, ��9797668174969��, ��9781787559554��,
... ��9780817481461��, ��9785130738708��, ��9798810365062��, ��9795345206033��,
... ��9792361848797��, ��9785197570819��, ��9786922535370��, ��9791978044523��,
... ��9796357284378��, ��9792982208529��, ��9793509549576��, ��9787954527409��,
... ��9797566046955��, ��9785239955499��, ��9787769276051��, ��9789910855708��,
... ��9783807934891��, ��9788337967876��, ��9786509441823��, ��9795400240705��,
... ��9787509152157��, ��9791478081103��, ��9780488170969��, ��9795755809220��,
... ��9793546666847��, ��9792322242176��, ��9782582638543��, ��9795919445653��,
... ��9796783939729��, ��9782384928398��, ��9787590220100��, ��9797422143460��,
... ��9798853923096��, ��9784177414990��, ��9799562126426��, ��9794732912038��,
... ��9787184435972��, ��9794455619207��, ��9794270312172��, ��9783811648340��,
... ��9799376073039��, ��9798552650309��, ��9798485624965��, ��9780734764010��,
... ��9783635963865��, ��9783246924279��, ��9797449285853��, ��9781631746260��,
36
... ��9791853742292��, ��9781796458336��, ��9791260591924��, ��9789367398012��
... ]
>>> overview(codes)
English speaking countries: 8
French speaking countries: 4
German speaking countries: 6
Japan: 3
Russian speaking countries: 7
China: 8
Other countries: 11
Errors: 9
"""
# construct histogram of registration groups
groups = {}
for i in range(11):
groups[i] = 0
for code in codes:
if not isISBN13(code):
groups[10] += 1
else:
groups[int(code[3])] += 1
# display overview
print(��English speaking countries: {}��.format(groups[0] + groups[1]))
print(��French speaking countries: {}��.format(groups[2]))
print(��German speaking countries: {}��.format(groups[3]))
print(��Japan: {}��.format(groups[4]))
print(��Russian speaking countries: {}��.format(groups[5]))
print(��China: {}��.format(groups[7]))
print(��Other countries: {}��.format(groups[6] + groups[8] + groups[9]))
print(��Errors: {}��.format(groups[10]))
if __name__ == ��__main__��:
import doctest
doctest.testmod()
8.2 Self-fulfillers
def lettervalue(