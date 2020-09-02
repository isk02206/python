'''
Created on 2018. 1. 4.

@author: TaeWoo
'''

from math import pi, sqrt

r = float(input())      # distance between a satellite and the center of the Earth
v = float(input())      # velocity

u = 398600.4418*(10**9) # constant
a = ((u*r)/(2*u-r*v**2))

period = 2*pi*sqrt(a**3/u)

if period < 86400:
    day = 0

else:
    day = int(period // 86400)

if period < 3600:
    hour = 0
    
else:
    hour = int(period % 86400 / 3600)
    
minutes = int(period % 86400 % 3600 / 60)

print('major axis: {} meters'.format(a))
print('period: {} seconds'.format(period))
print('period: {} days, {} hours and {} minutes'.format(day, hour, minutes))
