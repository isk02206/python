'''
Name: SungJoon Park
ID: 01514170
'''
t = float(input())
sum_of_abc = round(t*10**2)
multi_of_abc = round(sum_of_abc*10**4)

for a in range(1, (sum_of_abc // 3)+1):
    if multi_of_abc % a == 0:
        multi_of_bc = multi_of_abc // a
        sum_of_bc = sum_of_abc - a
        for b in range(a, (sum_of_bc // 2)+1):
            if multi_of_bc % b == 0:
                c = multi_of_bc // b
                if b + c == sum_of_bc:
                    a = format(a / 100, "0.2f")
                    b = format(b / 100, "0.2f")
                    c = format(c / 100, "0.2f")
                    t = format(t, '0.2f')
                    print('$' + a, '+ $' + b, '+ $' + c, '= $' + a, 'x $' + b, 'x $' + c, '= $' + t)
