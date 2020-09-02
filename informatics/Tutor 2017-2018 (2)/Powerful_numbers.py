'''
Created on 2018. 7. 2.

@author: TaeWoo
'''

# Enter number to check
# Leave number as a string not integer
number = input()

# Set order
order = len(number)     # order = number of digit

# Set while loop to check order
while order < 100:
    
    # Set loop to find a sum
    result = sum([int(i)**order for i in number])
    
    '''
    or 
    sum = 0
    for i in number:
        result += int(i)**order

    '''
    
    # check whether the number is powerful number
    # if result and number is the same, number is powerful number
    if result == int(number):
        print('{} is a powerful number of order {}'.format(number, order))
        break

    order += 1
        
# if different, the number is not powerful number
if result != int(number):
    print('{} is not a powerful number'.format(number))