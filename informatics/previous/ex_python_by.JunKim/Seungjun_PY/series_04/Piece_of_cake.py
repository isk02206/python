'''
Created on 2015. 10. 1.

@author: USER
'''

x = input()

length = len(x)
count = 0
evencount = 0
oddcount = 0

while x != str(123):
    for a in range(len(x)):
    
        y = x[a]
    
        if int(y) % 2 == 0:
            evencount += 1
        elif int(y) % 2 != 0:
            oddcount += 1
    
        count += 1

    x = str(evencount)+str(oddcount)+str(count)
    print(x)
    count = 0
    evencount = 0
    oddcount = 0