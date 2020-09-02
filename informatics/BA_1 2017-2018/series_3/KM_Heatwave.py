x = input()  # temperature

z = input()

a = 0 # count
b = 0 # count30
c = 0

while x != 'stop':

    z = float(z)

    if z < 25:
        a = 0
        b = 0

    if 25 <= z < 30:
        a += 1
        if a >= 5 and b >= 3:
            c = 1
            break
    if z >= 30:
        a = 1
        b = 1
        if a >= 5 and b >= 3:
            c = 1
            break

if b == 0:
    print('no heat wave')
if b == 1:
    print('heat wave')