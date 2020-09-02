'''
Created on 2016. 1. 20.

@author: User
'''
def csum(num):
   #change the type of variable into string ,num 
    num = str(num)
    
    #Calculate the sum of every digit until the position of digit is one

    while len(num) != 1:
        
        sum = 0
        
        for x in range(len(num)):
        
            sum += int(num[x])
            
        num = str(sum)
        
    else:
        
        return num
print(csum(8))


def csum(n):
   #change the type of variable into string ,num 
    n = str(n)
    
    #Calculate the sum of every digit until the position of digit is one
    while len(n) != 1:
        count = 0
        for x in range(len(n)):
            count += int(n[x])
        n = str(count)
    else:
        if len(n) == 1:
            return int(n)