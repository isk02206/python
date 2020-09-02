lohh = int(input())
lohm = int(input())
afhh = int(input())
afhm = int(input())
lfhh = int(input())
lfhm = int(input())
rohh = int(input())
rohm = int(input())

lohh1 = lohh * 60 + lohm
afhh1 = afhh * 60 + afhm
lfhh1 = lfhh * 60 + lfhm
rohh1 = rohh * 60 + rohm

a = (rohh1 - lohh1) % (60 * 24)
b = (lfhh1 - afhh1) % (60 * 24)

c = (a - b) / 2
#print(c + lfhh1)
d = (c + lfhh1) % (60 * 24)

#print(d)

print(int(d // 60))
print(int(d % 60))
