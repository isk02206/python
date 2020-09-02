'''
Created on 2016. 1. 20.

@author: User
'''
def crackRSA(num, difference):
    #set variable
    p1 = 0
    # iterate adding one to each p1 and difference variable 
    #until the multiple of p1 and difference is equal as the num
    while p1 * difference != num:
        #while True:
        p1 += 1
        
        difference += 1
        #if p1 * difference == num:
        #break
    # return the factors in a tuple    
    return p1, difference

p1 = num 의 약수

1 5  #different = 4
2 6
3 7 = 21
     둘의 곱이 num이될떄까지 loop돌림