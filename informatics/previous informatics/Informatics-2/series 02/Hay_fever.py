'''
Created on 2016. 1. 3.

@author: User
'''
n=int(input())
recommendation = str()
if n == 0:
    recommendation = 'no'
    print('There is',recommendation ,'risk of an allergic reaction at', n ,'pollen per cubic metre.')
if 1 <= n <=5:
    recommendation = 'weak'
    print('There is',recommendation ,'risk of an allergic reaction at', n ,'pollen per cubic metre.')
if 6<= n <=30:
    recommendation = 'moderate'
    print('There is',recommendation ,'risk of an allergic reaction at', n ,'pollen per cubic metre.')
if n > 30:
    recommendation = 'high'
    print('There is',recommendation ,'risk of an allergic reaction at', n ,'pollen per cubic metre.')

