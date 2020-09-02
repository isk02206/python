'''
Created on 2016. 9. 30.

@author: jeongkihong
@student_number: 01514158
'''
# import math module to use square root
import math
# new function that determines whether the integer is prime number or not
# used Eratosthenes' sieve
def primecheck(n):
    if n == 2 or n == 3:         # if n equals to 2, or 3, it's a prime number
        return True
    if n % 2 == 0 or n == 1:        # if n equals to 1 or n is even number, it's not a prime number
        return False
    for i in range(3, int(math.sqrt(n)) + 1):         # in range of 3 from square root of n, if n can be devided certain integer, it's not a prime number
        if n % i == 0:
            return False
    return True 

# initializations
m = int(input())

n = int(input())
# blank list for prime numbers
lists = []

# m < t**2 < n
for t in range(m,n):
    
    p = int(round(t**0.5))
    # if integer p is prime number, p goes into the list
    if primecheck(p) == True: 
        lists.append(p)

# need largest prime number        
largest_primenumber = max(lists)      

# print prime number
print("There are "+str(largest_primenumber)+" Martians having "+str(largest_primenumber)+" fingers each.")
