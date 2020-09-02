d = float(input()) # the initial density
r = float(input()) # fecundicity parameter
s = int(input()) # the number of time step

n = 1
while n <= s: # the number of time step = number of line 'stop'
    #print(n, s)
    print(d)
    d = r * d * (1 - d)
    #print(t)
    n += 1
