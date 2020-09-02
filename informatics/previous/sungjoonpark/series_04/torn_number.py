n = str(input())

for i in range(1,len(n)): 
    a = (n[0:i])
    b = (n[i:len(n)])
    if b[0] == 0:
        a = int(n[:i])
        b = int(n[i+1:])
    else:
        a = int(n[0:i])
        b = int(n[i:len(n)])
    t = (a+b)**2
    if t == int(n):
        print('torn')
        break
else:
    print('not torn')