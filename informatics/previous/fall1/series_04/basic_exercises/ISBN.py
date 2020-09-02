X = input()

while X!= 'stop':
    x1 = int(X[0])
    x2 = int(X[1])
    x3 = int(X[2])
    x4 = int(X[3])
    x5 = int(X[4])
    x6 = int(X[5])
    x7 = int(X[6])
    x8 = int(X[7])
    x9 = int(X[8])
    x10 = X[9]
    
    isbn = (x1+2*x2+3*x3+4*x4+5*x5+6*x6+7*x7+8*x8+9*x9)%11

    if X[9] == 'X':
        if 10 == isbn:
            print('OK')
        else:
            print('WRONG')
    else:
        if int(x10) == isbn:
            print('OK')
        else:
            print('WRONG')
    X = input()
            