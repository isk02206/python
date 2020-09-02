mt = int(input())
lt = int(input())
ht = int(input())
a = str(input())
b = str(input())

if mt < lt:
    print('too', a)
elif lt <= mt <= ht:
    print('just right')
else:
    print('too', b)
