'''
Created on 2015. 10. 20.

@author: USER
'''


def isISBN(code):
    if len(code) != 13:
        return False
    if str(code) != code:
        return False
    for i in range(2, 9):
        if code[i].isalpha():
            return False
    x1 = code[0]
    x2 = code[1]
    x3 = code[2]
    x4 = code[3]
    x5 = code[4]
    x6 = code[5]
    x7 = code[6]
    x8 = code[7]
    x9 = code[8]
    x10 = code[9]
    x11 = code[10]
    x12 = code[11]
    x13 = code[12]

    if x13 == 'X':
        x13 = 10
    if x2 != '-':
        return False
    if x7 != '-':
        return False
    if x12 != '-':
        return False

    exam = (int(x1) + 2 * int(x3) + 3 * int(x4) + 4 * int(x5) + 5 * int(x6) + 6 * int(x8) + 7 * int(x9) + 8 * int(
        x10) + 9 * int(x11)) % 11

    if exam == int(x13) and x2 == '-' and x7 == '-' and x12 == '-':
        find = True
    elif exam != int(x13):
        find = False
    return find