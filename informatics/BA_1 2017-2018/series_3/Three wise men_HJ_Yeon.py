num = float(input())
sum = round(num * 100)  # making the input to natural number to make the calculation easier
multi = round(sum * 10000)  # making the input to natural number to make the calculation easier
# multiplied value of numbers will be 1000000 times larger than the input
# 100^3 = 1000000
for a in range(1, sum // 3):
    if multi % a == 0:  # there should be no remainder when multiplied value is divided by value of a
        multi_of_bc = multi // a  # I can get the multiplied and total value of b and c
        sum_of_bc = sum - a  # got many 'a' values that are divisor of multiplied value

        for b in range(a, sum_of_bc // 2):  # range for b is given in question (0<a<=b<=c)
            if multi_of_bc % b == 0:  # same way with getting the a values
                c = multi_of_bc // b

                if b + c == sum_of_bc:
                    a = "%0.2f" % (a/100)  # rounding to second decimal place
                    b = "%0.2f" % (b/100)  # same procedure, getting a
                    c = "%0.2f" % (c/100)  # same procedure, getting a
                    # printing results
                    print('$'+str(a)+' + $'+str(b)+' + $'+str(c)+' = $'+str(a)+' x $'+str(b)+' x $'+str(c)+' = $'+str("%.2f" % num)+'')