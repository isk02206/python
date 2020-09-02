n=int(input())
e=int(input())
w=int(input())
l=input()
 
p=0
 
for i in range(1,n):
    if i % w!=0:
        p += e*(i)
        print("table #"+str(i)+': \u20ac'+str(p))
    else:
        p += e*(i)
        p *= 2
        print("table #"+str(i)+' (x2): \u20ac'+str(p))
if l=="stopped":
    if n % w != 0:
        p+=e*(n)
        print("table #"+str(n)+': \u20ac'+str(p))
    else:
        p += e*(n)
        p*=2
        print("table #"+str(n)+' (x2): \u20ac'+str(p))
else:
    p /= 2
    print("table #"+str(n)+': \u20ac'+str(int(p)))
