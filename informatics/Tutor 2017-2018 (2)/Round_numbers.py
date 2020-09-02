'''
Created on 2018. 1. 7.

@author: TaeWoo
'''

first = int(input())

second = int(input())

third = int(input())

fourth = int(input())

circle = [first, second, third, fourth]

print('{}-{}-{}-{}'.format(circle[0], circle[1], circle[2], circle[3]))

while len(set(circle)) != 1:
    
    first = circle[0]
    
    second = circle[1]
    
    third = circle[2]
    
    fourth = circle[3]
    
    circle = [abs(first - second), abs(second - third), abs(third - fourth), abs(fourth - first)]
    
    print('{}-{}-{}-{}'.format(circle[0], circle[1], circle[2], circle[3]))
    