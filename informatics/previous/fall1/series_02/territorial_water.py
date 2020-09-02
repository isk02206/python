
from math import sqrt

x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
x3 = float(input())
y3 = float(input())

u = ((x3-x1)*(x2-x1)+(y3-y1)*(y2-y1))/((x2-x1)**2+(y2-y1)**2)
xn = x1+u*(x2-x1)
yn = y1+u*(y2-y1)

xn1 = str(xn)
yn1 = str(yn)

d = sqrt((xn-x3)**2+(yn-y3)**2)

print("nadir: ("+xn1+",",yn1+")")
print("distance:",d,"nautical miles")
if 0<=d<12:
    print("zone: territorial waters")
elif d<24:
    print("zone: contiguous zone")
elif d<200:
    print("zone: exclusive economic zone")
else:
    print("zone: international waters")