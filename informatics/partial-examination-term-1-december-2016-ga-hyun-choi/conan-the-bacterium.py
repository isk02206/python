a = int(input())
b = int(input())
n = int(input())
t = int(input())
i = 0
z = 1
while i < n:
    z = a*z+b
    i += 1
print('experiment #1:', z, 'cells after', n, 'seconds')
j = 0
while t < z:
    t = a*t+b
    j += 1

print('experiment #2:', t, 'cells after', j, 'seconds')