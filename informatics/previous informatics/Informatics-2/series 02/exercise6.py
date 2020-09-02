x=float(input())
y=float(input())
import math
from math import atan2
r=(x**2+y**2)**(1/2)
t= math.atan2(y, x)
b= ((math.pi/2)+(math.pi/20)-t)%(2*math.pi)
si=(b/(math.pi/10))
s=si+1

if r<(12.7/2):
    print(50)
elif (12.7/2)<r<(31.8/2):
    print(25)
elif 31.8/2<r<(214.0/2-(31.8/2-12.7/2)):
    print(int(s))
elif (214.0/2-(31.8/2-12.7/2))<r<214.0/2:
    print(int(s)*3)
elif 214.0/2<r<(340.0/2-(31.8/2-12.7/2)):
    print(int(s))
elif (340.0/2-(31.8/2-12.7/2))<r<340.0/2:
    print(int(s)*2)
else:
    print(0)