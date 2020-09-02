'''
Created on 2015. 10. 23.

@author: USER
'''
def isISBN10(code):

    if len(code) != 10:
        return False
    
    if not code[:-1].isdigit():
        return False
    
    if not code[-1].isdigit() and code[-1] != 'X':
        return False
   
    checkdigit = 0
    for i in range(9):
        checkdigit += int(code[i]) * (i+1)
    checkdigit %= 11
   
    if checkdigit == 10:
        if code[-1] != 'X':
            return False
    elif str(checkdigit) != code[-1]:
        return False
    return True
def isISBN13(code):
 
    if len(code) != 13:
        return False
    
    if not code.isdigit():
        return False
    checkdigit = 0
    for i in range(12):
        if i % 2:
            checkdigit += 3 * int(code[i])
        else:
            checkdigit += int(code[i])
    checkdigit %= 10
    checkdigit = (10 - checkdigit) % 10
    
    
    if checkdigit != int(code[-1]):
        return False
    return True

def isISBN(code, new=True):

    if new:
        return isISBN13(code)
    else:
        return isISBN10(code)
def areISBN(codes, new=None):

    result = []
    for code in codes:
        if isinstance(code, str):
            if new is None:
                if len(code) == 13:
                    result.append(isISBN(code, True))
                else:
                    result.append(isISBN(code, False))
            else:
                result.append(isISBN(code, new))
        else:
            result.append(False)
    return result