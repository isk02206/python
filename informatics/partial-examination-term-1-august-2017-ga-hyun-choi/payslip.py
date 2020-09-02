x = input('')
n = 0
d = {}
while x != 'stop':
    if n == 0:
        r = int(x)
    else:
        d['worker #{}'.format(n)] = int(x)
        print('worker #{}'.format(n), 'whispers €' + str(sum(d.values()) + r))
    n += 1
    x = input('')
a = sum(d.values()) / (n-1)
print('average salary: €' + str('{0:.2f}'.format(a)))
