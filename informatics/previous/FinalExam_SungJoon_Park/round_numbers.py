a = int(input())
b = int(input())
c = int(input())
d = int(input())

print(a,'-',b,'-',c,'-',d)
while not a == b == c == d:
    a,b,c,d = abs(a-b),abs(b-c),abs(c-d),abs(d-a)
    print(a,'-',b,'-',c,'-',d)