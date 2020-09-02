x = input()

while x != 'stop':
    n = int(x)
    for i in range(1,9):
        n += (i+1)* int(input())
        if i == 8:
            checkdigit = n % 11
            if checkdigit == 10:
                checkdigit = 0
    if checkdigit == int(input()):
        print('OK')
    else:
        print('WRONG')
    x = input()

