'''
Created on 2016. 1. 8.

@author: User
'''
import math
def luhn (number):
    if len(number) == 11:
        a = str(number)[::-1]
        b=int(a[0])+(int(a[1])*int(2))+int(a[2])+(int(a[3])*int(2))+int(a[4])+(int(a[5])*int(2))+int(a[6])+(int(a[7])*int(2))+int(a[8])+(int(a[9])*int(2))+int(a[10])
        c = int(a[1])*int(2)
        d=int(a[3])*int(2)
        e=int(a[5])*int(2)
        f=int(a[7])*int(2)
        g=int(a[9])*int(2)
        if c >=10:
            c = int(str(c)[0])+ int(str(c)[1])
        if d >=10:
            d = int(str(d)[0])+ int(str(d)[1]) 
        if e >=10:
            e = int(str(e)[0])+ int(str(e)[1]) 
        if f >=10:
            f = int(str(f)[0])+ int(str(f)[1])  
        if g >=10:
            g = int(str(g)[0])+ int(str(g)[1]) 
        
        for y in str(number):
            b = int(a[0])+c+int(a[2])+d+int(a[4])+e+int(a[6])+f+int(a[8])+g+int(a[10])
        return b
    elif len(number) == 12:
        a = str(number)[::-1]
        b=int(a[0])+(int(a[1])*int(2))+int(a[2])+(int(a[3])*int(2))+int(a[4])+(int(a[5])*int(2))+int(a[6])+(int(a[7])*int(2))+int(a[8])+(int(a[9])*int(2))+int(a[10])+int(a[11])*int(2)
        c = int(a[1])*int(2)
        d=int(a[3])*int(2)
        e=int(a[5])*int(2)
        f=int(a[7])*int(2)
        g=int(a[9])*int(2)
        h = int(a[11])*int(2)
        if c >=10:
            c = int(str(c)[0])+ int(str(c)[1])
        if d >=10:
            d = int(str(d)[0])+ int(str(d)[1]) 
        if e >=10:
            e = int(str(e)[0])+ int(str(e)[1]) 
        if f >=10:
            f = int(str(f)[0])+ int(str(f)[1])  
        if g >=10:
            g = int(str(g)[0])+ int(str(g)[1]) 
        if h >=10:
            h = int(str(h)[0])+ int(str(h)[1]) 
        for y in str(number):
            b = int(a[0])+c+int(a[2])+d+int(a[4])+e+int(a[6])+f+int(a[8])+g+int(a[10])+h
        return b


def valid(number):
    vari = luhn(number)
    if vari % 10 == 0:
        return True     
    else:
        return False   
    

def addcheck(number):
    a = 0
    number = number [ : : -1]
    for x in range(0, len(number)):
        y = int(number [x])
        if x % 2 == 0:
            y *= 2
            if y > 9 :
                y = list(str(y))
                y = int(y[0]) + int(y[1])          
        a+= int(y)
    z = math.ceil(a /10) * 10 - a
    number = number [ : : -1] + str(z)
    
    return number



print(luhn('49927938719'))                
print(addcheck('4992793871'))