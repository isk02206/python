x = float(input())
y = float(input())
import math
r = (x ** 2 + y ** 2) ** (0.5)
theta = math.atan2(y, x) #art tangent(x/y) = math.atan2(y, x)
#print(theta)
b = ((math.pi / 2) + (math.pi / 20) - theta) % (2 * math.pi)
#print(b)
si = (b / (math.pi / 10))
#print(si)
s = si + 1
#print(s)

if r < (12.7 / 2):
    print(50)
elif (12.7 / 2) < r < (31.8/2):
    print(25)
elif (31.8 / 2) < r < ((214.0 / 2) - ((31.8 / 2) - (12.7 / 2))):
    print(int(s))
elif ((214.0 / 2) - ((31.8 / 2) - (12.7 / 2))) < r < (214.0 / 2):
    print(int(s) * 3)
elif (214.0 / 2) < r < ((340.0 / 2) - ((31.8 / 2) - (12.7 / 2))):
    print(int(s))
elif ((340.0 / 2) - ((31.8 / 2) - (12.7 / 2))) < r < (340.0 / 2):
    print(int(s) * 2)
else:
    print(0)