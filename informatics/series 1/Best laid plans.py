a = int(input())
b = int(input())
c = int(input())

d = ((a - c) * (b - c)) / c

print('There are', '{0:.2f}'.format(float(d)), 'undiscovered errors.')