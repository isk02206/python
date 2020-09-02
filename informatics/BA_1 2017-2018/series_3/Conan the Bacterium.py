a = int(input())
b = int(input())
n = int(input())
t = int(input())

z1 = 1
for i in range(n):
    z1 = (z1*a + b)

z2 = t
count = 0
while z2 < z1:
    z2 = z2*a + b
    count+=1

print('experiment #1:',z1,'cells after',n,'seconds')
print('experiment #2:',z2,'cells after',count,'seconds')




