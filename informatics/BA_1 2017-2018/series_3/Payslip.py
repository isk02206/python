a = int(input())
b = input()

count = 0
an = a

while b != 'stop':
    b = int(b)
    count += 1
    an = an + b
    print('worker #'+format(count),'whispers €'+format(an))
    b = input()

if b == 'stop':
    an = (an - a)/count
    an = format(an ,'.2f')
    print('average salary: €'+an)