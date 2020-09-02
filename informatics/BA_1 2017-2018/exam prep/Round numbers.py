a = int(input())
b = int(input())
c = int(input())
d = int(input())

print(str(a)+'-'+str(b)+'-'+str(c)+'-'+str(d))
while not a == b == c == d:
    a,b,c,d = abs(a-b),abs(b-c),abs(c-d),abs(d-a)
    print(str(a)+'-'+str(b)+'-'+str(c)+'-'+str(d))
