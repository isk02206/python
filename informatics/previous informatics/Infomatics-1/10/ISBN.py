'''
Created on 2015. 12. 3.

@author: User
'''
10.1 ISBN
class ISBN13:
"""
>>> code = ISBN13(9780136110675)
>>> print(code)
978-0-13611067-5
>>> code
ISBN13(9780136110675, 1)
>>> code.isValid()
True
>>> code.asISBN10()
¡¯0-13611067-3¡¯
"""
def __init__(self, code, length=1):
# check validity of arguments
assert isinstance(code, int), ¡¯ISBN-13 codes must only contain digits.¡¯
assert len(str(code)) == 13, ¡¯ISBN13-codes must contain 13 digits.¡¯
assert 1 <= length <= 5, ¡¯The specification of the country group of an ISBN-13 code
must have 1 to 5 digits.¡¯
self.code = code
self.length = length
def __str__(self):
code = str(self.code)
return ¡¯{}-{}-{}-{}¡¯.format(
code[:3],
code[3:3 + self.length],
code[3 + self.length:-1],
code[-1]
)
def __repr__(self):
return ¡¯ISBN13({}, {})¡¯.format(self.code, self.length)
def isValid(self):
def checkdigit(code):
51
# compute ISBN-13 check digit
check = sum((3 if i % 2 else 1) * int(code[i]) for i in range(12))
# convert the check digit into string representation
return str((10 - check) % 10)
# convert ISBN13 code to string
code = str(self.code)
# check validity of check digit
return code[12] == checkdigit(code)
def asISBN10(self):
def checkdigit(code):
# compute ISBN-10 check digit
check = sum((i + 1) * int(code[i]) for i in range(9)) % 11
# convert the check digit into string representation
return ¡¯X¡¯ if check == 10 else str(check)
if not self.isValid() or str(self.code)[:3] == ¡¯979¡¯:
return None
else:
code = str(self.code)[3:-1]
check = checkdigit(code)
return ¡¯{}-{}-{}¡¯.format(
code[:self.length],
code[self.length:],
checkdigit
)
if __name__ == ¡¯__main__¡¯:
import doctest
doctest.testmod()
