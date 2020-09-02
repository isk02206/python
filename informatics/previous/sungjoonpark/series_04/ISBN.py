x = input()

while x !='stop':
    x1 = int(x[0])
    x2 = int(x[1])
    x3 = int(x[2])
    x4 = int(x[3])
    x5 = int(x[4])
    x6 = int(x[5])
    x7 = int(x[6])
    x8 = int(x[7])
    x9 = int(x[8])
    x10 = int(x[9])
    
    ISBN = (x1 + 2*x2 + 3*x3+ 4*x4 + 5*x5 + 6*x6 + 7*x7 + 8*x8 + 9*x9) % 11
    
    if ISBN == x10:
        print('OK')
    else:
        print('WRONG')
    x = input()