def isISBN(x):
    ISBN = []
    while x != 'stop':
        if (1 <= x <=9 and x == 0) or (1 <= x <=9 and x == 0 and x == 'X'):
            a = list(x)
            for i in range(0,10):
                b = ISBN.append(a[i])
                c = int(b[i])
                c+=c*(1+i)
                c%= 11
                if c == 'X':
                    'X' == 0
                    if c == 'X':
                        return True
                    else:
                        return False
                elif c == ISBN[-1]:
                        return True
                else:
                    return False
        else:
            return False
'''
value = '9971502100'
result = isISBN(value)
print(result)
'''