
h1 = int(input())
m1 = int(input())
h2 = int(input())
m2 = int(input())

x = abs(h1-h2)
if x < 12:
    h = x
else : 
    h = (24-x)

y = abs(m1-m2)
if y < 30:
    m = y
else:
    m = (60-y)
    
print(h+m)