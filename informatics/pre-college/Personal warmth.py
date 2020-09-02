a = float(input())

e = 100 / 36.8
ec = 100 / a

if float(e) - 0.1 > ec:
    print('you have a fever')
elif float(e) + 0.1 < ec:
    print('you have hypothermia')
else:
    print('you have a normal body temperature')