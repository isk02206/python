'''
Created on 2015. 9. 30.

@author: Seungjun Kim
'''
x = input()
while x!= 'stop':
    x1= x[0]
    x2= x[1]
    x3= x[2]
    x4= x[3]
    x5= x[4]
    x6= x[5]
    x7= x[6]
    x8= x[7]
    x9= x[8]
    x10=x[9]
    f =(int(x1)+2*int(x2)+3*int(x3)+4*int(x4)+5*int(x5)+6*int(x6)+7*int(x7)+8*int(x8)+9*int(x9)) % 11 
    if x10 == 'X':
        x10 =10 
    if f ==int(x10):
        print('OK')
    else :
        print('WRONG')
    x=input()
        