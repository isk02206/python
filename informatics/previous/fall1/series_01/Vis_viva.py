r = float(input())
v = float(input())
μ = 398600.4418*(10**9)

from math import pi
from math import sqrt

a = μ*r/(2*μ - r*v**2)
period = 2*pi*sqrt(a**3/μ)

d = period//(24*60*60)
h = (period-(24*60*60)*d)//3600
m = (period-3600*(h+24*d))//60


print("major axis:", a, "meters")
print("period:", period, "seconds" )
print("period:",int(d),"days,",int(h),"hours and",int(m),"minutes")