loc1 = str(input())
loc2 = str(input())

hor = 'abcdefgh000'

x1 = hor.find(loc1[0])+1
x2 = int(loc1[1])

a = str(hor[x1])+str(x2+2)
b = str(hor[x1])+str(x2-2)
c = str(hor[x1-2])+str(x2+2)
d = str(hor[x1-2])+str(x2-2)
e = str(hor[x1+1])+str(x2+1)
f = str(hor[x1+1])+str(x2-1)
g = str(hor[x1-3])+str(x2+1)
h = str(hor[x1-3])+str(x2-1)
loc =[a,b,c,d,e,f,g,h]
if loc2 in loc:
    ok = 'can'
if loc2 not in loc:
    ok = 'cannot'

print('a knight',ok,'jump from',loc1,'to',loc2)