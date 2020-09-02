def isISBN(x):
    
    if type(x) != str: #prevent the outcome is string
        return False 
    if len(x) != 10:  #prevent the exeption of outcome
        return False
    
    a = int(x[0])
    b = int(x[1])
    c = int(x[2])
    d = int(x[3])
    e = int(x[4])
    f = int(x[5])
    g = int(x[6])
    h = int(x[7])
    i = int(x[8])
    j = str(x[9]) #the value of x is not integral
     
    if j == 'X':
        j = 10
    else:
        j = int(x[9])


    l = int((a+2*b+3*c+4*d+5*e+6*f+7*g+8*h+9*i)%11)
    
    if j == l:
        return True
    else:
        return False
    
print(isISBN('9971502108') )