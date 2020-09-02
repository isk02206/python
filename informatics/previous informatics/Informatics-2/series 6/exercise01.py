'''
Created on 2015. 10. 23.

@author: User
'''


def isISBN(x):
    
    if type(x) != str:
        return False

    if len(x) != 13:
        return False
    
    if x[1] != '-':
        return False
    elif x[6] != '-':
        return False
    elif x[-2] != '-':
        return False
    
    else:
        
        if '-' in x:
            a = x.replace('-','')
        
        x10 = a[9]
        
        b = ''
        
        if x10 == 'X':
            x10 = 10
            b = a[:9]+str(x10)   
        elif str.isdigit(x10):
            x10 = int(a[9])
            b = a[:9]+str(x10)
        else:
            return False
        
        if str.isdigit(b):
            x1 = int(a[0])
            x2 = int(a[1])
            x3 = int(a[2])
            x4 = int(a[3])
            x5 = int(a[4])
            x6 = int(a[5])
            x7 = int(a[6])
            x8 = int(a[7])
            x9 = int(a[8])
                
            y = int((x1+2*x2+3*x3+4*x4+5*x5+6*x6+7*x7+8*x8+9*x9)%11)
        
            if y == x10:
                return True
            else:
                return False
        else:
            return False
        
    
print(isISBN('9-9715-0210-0') )