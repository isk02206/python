x1 = input()
while x1 != 'stop':
    x10 = (int(x1[0]) + int(x1[1]) * 2 + int(x1[2]) * 3 + int(x1[3]) * 4 + int(x1[4]) * 5 + int(x1[5]) * 6 + int(x1[6]) * 7 + int(x1[7]) * 8 + int(x1[8]) * 9) % 11

    if x10 == 10:
        x10 = str('X')
    if x10 != 10:
        x10 != str('X')
    if x1[9] == str(x10):
        print('OK')
    else:
        print('WRONG')
    x1 = input()