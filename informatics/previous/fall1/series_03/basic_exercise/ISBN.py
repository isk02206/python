x = input()

while x != 'stop':
    value = int(x)
    for i in range(2, 10):
        value += i*int(input())
    value %= 11
    
    if value == int(input()):
        print()
        print('OK')
    else:
        print('WRONG')
    x = input()