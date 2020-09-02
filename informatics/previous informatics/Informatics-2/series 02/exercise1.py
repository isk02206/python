a=int(input())
b=int(input())
c=int(input())
d=int(input())
e=int(input())
f=int(input())
g=int(input())
h=int(input())
i=int(input())
j=int(input())
k=(a+b*2+c*3+d*4+e*5+f*6+g*7+h*8+i*9+j*10)%11
if k==0:
    print('OK')
if k!=0:
    print('WRONG')