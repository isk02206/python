import math

n=int(input())

e=math.ceil(n/math.e)

#print(e)

list=[]
for attempts in range(1,e+1):
    #print(attempts)
    rating1=float(input())
    list.append(rating1)
    m=max(list)
    
#print()
    
for attempts in range (e+1,n+1):
    #print(attempts)
    rating2=float(input())
    list.append(rating2)
    if m<rating2:
        print(rating2)
        break
    
if m>rating2:
    print(list[n-1])
    