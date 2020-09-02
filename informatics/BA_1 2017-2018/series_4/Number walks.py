import math
g = str(input())

numb = []
a = 0
b = 0

pos_x = {'0':0, '1':math.cos(math.radians(54)), '2' :math.cos(math.radians(18)) , '3':math.cos(math.radians(-18)), '4':math.cos(math.radians(-54)), '5':0, '6':math.cos(math.radians(-126)), '7':math.cos(math.radians(-162)), '8':math.cos(math.radians(162)), '9':math.cos(math.radians(126))}
pos_y = {'0':1, '1':math.sin(math.radians(54)), '2' :math.sin(math.radians(18)), '3':math.sin(math.radians(-18)), '4':math.sin(math.radians(-54)), '5':-1, '6':math.sin(math.radians(-126)), '7':math.sin(math.radians(-162)), '8':math.sin(math.radians(162)), '9':math.sin(math.radians(126))}

for x in g:
    if x != '.':
        numb.append(x)

for i in numb:
    a += pos_x[i]
    b += pos_y[i]

a = format(a,'0.2f')
b = format(b,'0.2f')

print('Number',g,'walks to position ('+a+',',b+').')