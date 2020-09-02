'''
b = int(input()) #total budget
p = int(input()) #cost of chocolate bar
w = int(input()) #wrapper recycled
n = int(input()) #new bar got for free

x = b // p #choco got 1st

y = (x // w)*n #choco got recycled

(x //w)

while x >= w:
    
'''
b = int(input()) #total budget
p = int(input()) #cost of chocolate bar
w = int(input()) #wrapper recycled
n = int(input()) #new bar got for free

r = 0 
initial = b //p
ini = initial
while ini>= w:
    initial += n*(ini//w)
    r = ini % w
    ini = n *(ini // w) +r
print(initial)