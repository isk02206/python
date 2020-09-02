x1 = input()
while x1 != 'stop':
    # read the next digits and compute check digit
    checkdigit = int(x1)
    for i in range(2, 10): # i = [2,3,4,5,6,7,8,9,10]
        checkdigit += i * int(input())
    checkdigit %= 11
    # test check digit
    if checkdigit == int(input()):
        print('OK')
    else:
        print('WRONG')

    x1 = input()
