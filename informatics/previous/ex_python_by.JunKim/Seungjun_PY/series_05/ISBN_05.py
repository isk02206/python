'''
Created on 2015. 10. 5.

@author: Jun Kim
'''

# code = '123456789X'
def isISBN(code):
    # if isinstance(code, int): >>> False
    if not isinstance(code, str):
        return False
    
    list = '0123456789X'
    
    for x in range(10):
        if not code[x] in list:
            return False
        
    
    a = int(code[0])
    b = int(code[1])
    c = int(code[2])
    d = int(code[3])
    e = int(code[4])
    f = int(code[5])
    g = int(code[6])
    h = int(code[7])
    i = int(code[8])
    l = code[9]
    j =((a + 2*b + 3*c + 4*d + 5*e + 6*f + 7*g + 8*h + 9*i) % 11) 
              
    if code[9] == 'X' :
        l = 10
    else:
        l = int(code[9])
    
    if j == l:
        return True
    else:
        return False
    
print(isISBN(4378580136))