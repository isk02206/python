'''
Created on 2015. 11. 16.

@author: User
'''
def isISBN10(code):
"""
Checks whether or not the given ISBN-10 code is valid.
>>> isISBN10(¡¯9971502100¡¯)
 True 
>>> isISBN10(¡¯9971502108¡¯) 
 False 
"""
def checkdigit(code):
# compute the check digit
    check = sum((i + 1) * int(code[i]) 
    for i in range(9)) % 11
# convert the check digit into string representation 
        return ¡¯X¡¯ if check == 10 
        else str(check)
# check whether the given code is a string 
        if not isinstance(code, str): 
            return False
# check whether the given code contains 10 characters 
        if len(code) != 10:
            return False
# check whether first nine characters of the given code are digits
        if not code[:9].isdigit(): 
            return False
# check the check digit return checkdigit(code) == code[-1]
def isISBN13(code):
""" Checks whether or not the given ISBN-13 code is valid.
>>> isISBN13(¡¯9789743159664¡¯) True >>> isISBN13(¡¯9787954527409¡¯) False >>> isISBN13(¡¯8799743159665¡¯) False """
def checkdigit(code):
# compute the check digit 
    check = sum((3 if i % 2 else 1) * int(code[i]) for i in range(12))
# convert the check digit into a single digit     
    return str((10 - check) % 10)
# check whether the given code is a string 
if not isinstance(code, str): 
    return False
# check whether the given code contains 10 characters 
if len(code) != 13: 
    return False
# check whether first nine characters of the given code are digits 
if not code[:12].isdigit(): 
    return False
# check the check digit 
return checkdigit(code) == code[-1]

def isISBN(code, isbn13=True):
""" 
>>> isISBN(¡¯9789027439642¡¯, False) 
False 
>>> isISBN(¡¯9789027439642¡¯, True) 
True 
>>> isISBN(¡¯9789027439642¡¯) 
True 
>>> isISBN(¡¯080442957X¡¯) 
False 
>>> isISBN(¡¯080442957X¡¯, False) 
True 
"""
return isISBN13(code) if isbn13 else isISBN10(code)
def areISBN(codes, isbn13=None):
""" 
>>> areISBN(
...     [
...         ¡¯0012345678¡¯, ¡¯0012345679¡¯, ¡¯9971502100¡¯, ¡¯080442957X¡¯,
...         5, True, ¡¯The Practice of Computing Using Python¡¯, 
...         ¡¯9789027439642¡¯, ¡¯5486948320146¡¯ 
...     ]
... ) 
[False, True, True, True, False, False, False, True, False]
>>> areISBN( 
...     [ 
...         ¡¯0012345678¡¯, ¡¯0012345679¡¯, ¡¯9971502100¡¯, ¡¯080442957X¡¯, 
...         5, True, ¡¯The Practice of Computing Using Python¡¯, 
...         ¡¯9789027439642¡¯, ¡¯5486948320146¡¯ 
...     ], 
...     True 
...     ) 
 [False, False, False, False, False, False, False, True, False]
>>> areISBN( 
...     [ 
...         ¡¯0012345678¡¯, ¡¯0012345679¡¯, ¡¯9971502100¡¯, ¡¯080442957X¡¯, 
...         5, True, ¡¯The Practice of Computing Using Python¡¯, 
...         ¡¯9789027439642¡¯, ¡¯5486948320146¡¯ 
...     ], 
...     False 
... ) 
[False, True, True, True, False, False, False, False, False]
 """
# initialize list of evaluations 
evaluations = []
# construct list of evaluations 
for code in codes: 
    if isinstance(code, str): 
        if isbn13 is None: 
            if len(code) == 13: 
                evaluations.append(isISBN(code, True)) 
            else: evaluations.append(isISBN(code, False)) 
        else: evaluations.append(isISBN(code, isbn13)) 
    else: evaluations.append(False)
# return list of results 
    return evaluations

if __name__ == ¡¯__main__¡¯: 
    import doctest 
    doctest.testmod()
