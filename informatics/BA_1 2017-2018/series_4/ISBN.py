x = input()

while x != 'stop':
    checkdigit = 0
    for i in range(9):
        ISBN = (i + 1) * int(x[i])
        checkdigit += ISBN
        if i == 8:
            func = checkdigit % 11
            if func == 10:
                func = 'X'
                if x[-1] == str(func):
                    print('OK')
                if x[-1] != str(func):
                    print('WRONG')
            else:
                if x[-1] == str(func):
                    print('OK')
                if x[-1] != str(func):
                    print('WRONG')
    x = input()