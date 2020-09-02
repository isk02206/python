'''
n = int(input())

from math import e
import math

frog = []
first = []
for x in range(math.ceil(n / e)):
    x = input()
    first.append(x)

for i in range((math.ceil(n/e)) , n):
    i = input()
    frog.append(i)
    if i > max(first):
        print(i)
        break
if max(frog) < max(first):
    print(frog[-1])
'''
n = int(input())

from math import e

frog = []
for y in range(n):
    y = input()
    frog.append(y)
    for i in range((math.ceil(n/e)) , n):
        if i > max(first):
        print(i)
        break
if max(frog) < max(first):
    print(frog[-1])