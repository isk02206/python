x1 = float(input())
y1 = float(input())
r1 = float(input())
x2 = float(input())
y2 = float(input())
r2 = float(input())

import math
d = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
#print(d , r1 - r2, r1 + r2, abs(r1 - r2))

if d == 0:
    print('concentric')
elif '{0:.6f}'.format(float(d)) == '{0:.6f}'.format(float(abs(r1 - r2))):
    print('touching inside')
elif '{0:.6f}'.format(float((d))) == '{0:.6f}'.format(float(r1 + r2)):
    print('touching outside')
elif d < abs(r1 - r2):
    print('enclosing')
elif abs(r1 - r2) < d < r1 + r2:
    print('intersecting')
elif d > r1 + r2:
    print('separate')
