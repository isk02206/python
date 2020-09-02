'''
Created on 2016. 1. 3.

@author: User
'''
import math
g=int(input())
m=int(input())
s=int(input())
de=g+(m*(1/60))+(s*(1/3600))
r=(math.pi/180)*de
print(r)