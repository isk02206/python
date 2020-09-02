temp = float(input())

nat = 100/36.8

e = 100 / temp

if e < nat - 0.1:
    state = 'a fever'
if e > nat + 0.1:
    state = 'hypothermia'
if e >= nat - 0.1 and e <= nat +0.1:
    state = 'a normal body temperature'

print('you have',state)