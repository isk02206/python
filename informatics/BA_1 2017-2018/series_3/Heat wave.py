a = input()

temp = []

while a != 'stop':
    temp.append(a)
    a = input()

count = 0
count30 = 0
b = 0

for i in temp:
    c = float(i)
    if 25 <= c < 30:
        count += 1
        if count >= 5 and count30 >= 3:
            b = 1
            break
    if 25 > c:
        count = 0
        count30 = 0
    if 30 <= c:
        count30 += 1
        count += 1
        if count >= 5 and count30 >= 3:
            b = 1
            break

if b == 1:
    print('heat wave')
if b == 0:
    print('no heat wave')