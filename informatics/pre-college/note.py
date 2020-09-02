n = int(input())
s = 0
i = 0
h = 0
for i in range(i, int(n/2)):
    p = float(input())
    if p > h:
        h = p
    i += 1
    s += 1
c = False
for j in range(int(n / 2) + 1, n + 1):
    p = float(input())
    if p > h and c == False:
        h = p
        c = True
        s += 1
if c == False:
    h = p
    s += 1
r = round(float(h), 4)
print(r)

