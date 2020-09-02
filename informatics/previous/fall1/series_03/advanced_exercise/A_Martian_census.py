from math import sqrt
m = int(input())
n = int(input())
lists = []  #definition lists is empty yet

for i in range (m, n+1):
    x = round(sqrt(i))   #derive a square root of value x between m and n
    for y in range (2, x):  #a prime number can be divided by 1 and oneself
        if x % y == 0:  #x has to be divided by both 1 and oneself, not another number
            break
        elif y == x-1: #if it is oneself, put on the list because prime number can be divided by oneself
            lists.append(x)
print("There are",min(lists),"Martians having",min(lists),"fingers each.")