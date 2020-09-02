n = int(input())
rx = int(input())
ry = int(input())
rz = int(input())
gx = int(input())
gy = int(input())
gz = int(input())

x = abs((rx - gx)/(n-1))
y = abs((ry - gy)/(n-1))
z = abs((rz - gz)/(n-1))

for i in range(n):
    if rx > gx:
        a = rx - x*i
    elif rx == gx:
        a = rx
    elif rx < gx:
        a = rx + x*i
        
    if ry > gy:
        b = ry - y*i
    elif ry == gy:
        b = ry
    elif ry < gy:
        b = ry + y*i
    
    if rz > gz:
        c = rz - z*i
    elif rz == gz:
        c= rz
    elif rz < gz:
        c = rz + z*i
    
    s = round(a)
    j = round(b)
    p = round(c)
    
    print('rgb('+format(s) +',',format(j)+ ',' ,format(p)+ ')')