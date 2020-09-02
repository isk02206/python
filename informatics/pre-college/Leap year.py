a = int(input())

b = a % 400
c = a % 4
d = a % 100
if b == 0 or c == 0 and d != 0:
    print('leap year')
elif d == 0:
    print('not a leap year')
else:
    print('not a leap year')
