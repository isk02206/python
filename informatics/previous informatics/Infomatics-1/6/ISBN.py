'''
Created on 2015. 12. 3.

@author: User
'''
6.1 ISBN
def isISBN(code):
"""
Checks whether or not the given ISBN-10 code is valid.
>>> isISBN(¡¯9-9715-0210-0¡¯)
True
>>> isISBN(¡¯997-150-210-0¡¯)
False
>>> isISBN(¡¯9-9715-0210-8¡¯)
False
"""
19
# check if the given code is a string
if not isinstance(code, str):
return False
# checks whether the dashes are at the right location and whether each group
# has the right number of digits
groups = code.split(¡¯-¡¯)
if tuple(len(e) for e in groups) != (1, 4, 4, 1):
return False
# remove dashes from the given code
code = ¡¯¡¯.join(groups)
# check whether or all characters (except the final one) are digits
if not code[:-1].isdigit():
return False
# chech the check digit of the given code
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