'''
Created on 2016. 1. 3.

@author: User
'''
value = int(input())
lower_boundary = int(input())
upper_boundary = int(input())
quality_of_low = str(input())
quality_of_high = str(input())
if value < lower_boundary and value <upper_boundary and lower_boundary < upper_boundary:
    if quality_of_low == 'cold':
        print('too cold')
    if quality_of_low == 'small':
        print('too small')
    if quality_of_low == 'acidic':
        print('too acidic')
if value > lower_boundary and value <upper_boundary and lower_boundary < upper_boundary:
    print('just right')
if value > lower_boundary and value > upper_boundary and lower_boundary < upper_boundary:
    if quality_of_high == 'hot':
        print('too hot')
    if quality_of_high == 'large':
        print('too large')
    if quality_of_high == 'basic':
        print('too basic')
if value == lower_boundary or value == upper_boundary:
    print('just right')