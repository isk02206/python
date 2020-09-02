'''
Created on 2017. 9. 15.

@author: jeongki
'''
number = float(input())
sum_of_abc = int(number * 100)

multi_abc = round(sum_of_abc * 10000 + 1)
for a in range(1, sum_of_abc // 3):
    if multi_abc % a == 0:
        multi_bc = multi_abc // a
        sum_of_bc = sum_of_abc - a
        for b in range(a, sum_of_bc // 2):
            if multi_bc % b == 0:
                c = multi_bc // b
                if b + c == sum_of_bc:
                    a = "%0.2f" % (a/100)
                    b = "%0.2f" % (b/100)
                    c = "%0.2f" % (c/100)
                    number = "%0.2f" % number
                    print('$'+str(a)+' + $'+str(b)+' + $'+str(c)+' = $'+str(a)+' x $'+str(b)+' x $'+str(c)+' = $'+str(number)+'')