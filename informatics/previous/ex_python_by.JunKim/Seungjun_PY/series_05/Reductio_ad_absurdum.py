'''
Created on 2015. 10. 8.

@author: USER
'''
def equivalentFraction(a,b,c,d):
    if (int(a)/int(b)) == (int(c)/int(d)) :
        return True 
    else :
        return False 
    
def reduction(a, b):
    a = str(a)
    b = str(b)
    
    for digit in a :
        if digit in b :            
            a = a.replace(digit,'', 1)
            b = b.replace(digit,'', 1)
            if a == '':
                a ='-1'
            if b == '':
                b = '-1'
                
    return (int(a),int(b))

def validReduction(a, b):
    c = reduction(a, b)[0]
    d = reduction(a, b)[1]
    if d == 0 :
        return (a, b)
    if int(a)/int(b) == c/d :
        return (c, d)
    else :
        return (a, b)
print(validReduction(19,95))