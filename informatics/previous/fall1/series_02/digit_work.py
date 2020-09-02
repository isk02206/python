
x = int(input())
y = int(input())

s1 = x * y
s2 = (((x - 5) + (y - 5)) * 10) + ((10 - x) * (10 - y))
s3 = 100 + 10 * ((x - 10) + (y - 10)) + (x - 10) * (y - 10)

if (x<=5 and y<=5) or (x==10 or y==10):
    print(x,"x",y,"=",s1)
elif (5 < x < 10) and (5 < y < 10):
    print(x,"x",y,"= 10 x ("+str(x-5),"+",str(y-5)+") + ("+str(10-x),"x",str(10-y)+") =",s2)    
elif (10<x<=15) and (10<y<=15):
    print(x,"x",y,"= 100 + 10 x ("+str(x-10),"+",str(y-10)+") + ("+str(x-10),"x",str(y-10)+") =",s3)
else:
    print(x,"x",y,"= 100 + 10 x ("+str(x-10),"+",str(y-10)+") + ("+str(x-10),"x",str(y-10)+") =",s3)