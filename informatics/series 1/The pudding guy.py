tnp = int(input())
cpp = float(input())
upc = int(input())
mile = int(input())

dol = tnp * cpp
con = tnp // upc

con2 = con * mile

print('Phillips spent', '$' + str(dol), 'for', con2, 'frequent-flyer miles.')