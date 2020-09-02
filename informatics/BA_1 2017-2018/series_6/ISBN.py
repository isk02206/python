def isISBN10(code):
    if len(code) != 10:
        return False
    if not code[:-1].isdigit():
        return False
    if not code[:-1].isdigit() and code[-1] != 'X':
        return False
    # together = 0
    # for i,number in enumerate(code[:-1]):
    #    together += (i+1)*int(number)
    # together %= 11
    together = sum([(i + 1) * int(number) for i, number in enumerate(code[:-1])]) % 11

    if together == 10:
        return code[-1] == 'X'
    else:
        return code[-1] == str(together)


def isISBN13(code):
    if not isinstance(code, str):
        return False
    if len(code) != 13:
        return False
    if not code.isdigit():
        return False
    # together = 0
    # for i in range(12):
    #    if i %2:
    #        together += 3*int(code[i])
    #    else:
    #        together += int(code[i])
    # together %= 10
    together = sum([factor * int(number) for factor, number in zip(6 * [1, 3], code[:-1])]) % 10
    together = (10 - together) % 10
    return together == int(code[-1])


def isISBN(code, isbn13=True):
    if not isinstance(code, str):
        return False
    if isbn13 is None:
        isbn13 = (len(code) == 13)
    if isbn13:
        return isISBN13(code)
    else:
        return isISBN10(code)


def areISBN(are, isbn13=None):
    if not isinstance(are, list):
        return []
    else:
        return [isISBN(item, isbn13) for item in are]


if __name__ == '__main__':
    import doctest
    doctest.testmod()