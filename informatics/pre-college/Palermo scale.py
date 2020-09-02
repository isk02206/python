import math
t = int(input())
p = float(input())
e = float(input())
b = 0.03 * (e ** -0.8)
print(math.log( p / (b * t) , 10))
