a=input()
while a!='stop':
    b=int(input())
    c=int(input())
    d=int(input())
    e=int(input())
    f=int(input())
    g=int(input())
    h=int(input())
    i=int(input())
    j=int(input())
    k=(int(a)+b*2+c*3+d*4+e*5+f*6+g*7+h*8+i*9)%11
    if j==k:
        print('OK')
    else:
        print('WRONG')
    a=input()