
x = input()

while x != 'stop':
    checkdigit = int(x)
    for i in range(2,10):
        checkdigit+=i*int(input())
        checkdigit %= 11
    if checkdigit == int(input()):
        print('OK')
    else:
        print('WRONG')
    x = input()
