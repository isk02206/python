sta = str(input())
p = int(input())
s = int(input())

slogan = []
pos = p
poslist = []
for i in range(len(sta)):
    x = pos + s * (i)
    poslist.append(x)
y = 1
a = abs(int(poslist[-1]))
b = abs(int(poslist[0]))

while (a+b) > len(sta)*y:
    statement = sta * y
    y += 1
statement = sta*y + sta
for j in poslist:
    j = int(j)
    sword = statement[j]
    slogan.append(sword)
slogan = "".join(slogan)

print(slogan)
