a = input()
while a != 'stop':
    b = (int(a[0]) + int(a[1])*2 + int(a[2])*3 + int(a[3])*4 + int(a[4])*5 + int(a[5])*6 + int(a[6])*7 + int(a[7])*8 + int(a[8])*9) % 11

    if b==10:
        b = str('X')
    if b!=10:
        b!=str('X')
    if a[9] == str(b):
        print('OK')
    else:
        print('WRONG')
    a = input()
9971502100
9971502108
stop