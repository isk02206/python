pirates = int(input())
coconuts = int(input())
a = coconuts
c = coconuts % pirates
if c == 0:
    show_c = 'no nuts'
if c >= 1:
    show_c = c
b = coconuts - c
n = pirates
print(a,'nut(s) =',b,'nut(s) for pirate#'+str(n),'and',c,' nut(s) for the monkey')
for i in range(pirates):

    print()