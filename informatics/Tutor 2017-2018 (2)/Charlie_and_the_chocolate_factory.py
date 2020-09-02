'''
Created on 2018. 1. 8.

@author: TaeWoo
'''

budget = int(input())
cost = int(input())
exchange = int(input())
new = int(input())

number_of_chocolate = int(budget//cost)
final_number_of_chocolate = number_of_chocolate

while number_of_chocolate >= exchange:
    
    remaining = number_of_chocolate % exchange
    number_of_chocolate = int(number_of_chocolate//exchange) * new
    final_number_of_chocolate += number_of_chocolate
    number_of_chocolate += remaining
    
print(final_number_of_chocolate)