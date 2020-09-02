'''
Created on 2015. 12. 3.

@author: User
'''
5 series 05
5.1 ISBN
def isISBN(code):
"""
Checks whether or not the given ISBN-10 code is valid.
>>> isISBN(¡¯9971502100¡¯)
True
>>> isISBN(¡¯9971502108¡¯)
False
"""
# check whether the given code is a string
if not isinstance(code, str):
return False
# check whether the given code contains 10 characters
if len(code) != 10:
return False
# check whether first nine characters of the given code are digits
if not code[:9].isdigit():
return False
# check the check digit
return checkdigit(code) == code[-1]
def checkdigit(code):
"""
>>> checkdigit(¡¯997150210¡¯)
¡¯0¡¯
>>> checkdigit(¡¯938389293¡¯)
¡¯5¡¯
"""
# compute the check digit
check = sum((i + 1) * int(code[i]) for i in range(9)) % 11
# convert the check digit into string representation
return ¡¯X¡¯ if check == 10 else str(check)
if __name__ == ¡¯__main__¡¯:
import doctest
doctest.testmod()

