'''
Created on 2018. 1. 7.

@author: TaeWoo
'''

first = input()
second = input()
spacer = ''
counter = 0 

while second != '-1':
    
    if len(first) == 3:
        
        first_print = first + ' '
        
    elif len(first) == 1:
        
        first_print = ' ' + first + '  '
        
    else:
        
        first_print = ' ' + first + ' '
        
    if len(second) == 3:
        
        second_print = second + ' '
        
    elif len(second) == 1:
        
        second_print = ' ' + second + '  '
        
    else:
        
        second_print = ' ' + second + ' '
    
    print('{}{}{}'.format(spacer, first_print, second_print.rstrip()))
    
    spacer += '  '
    first = str(sum([int(i) for i in first+second]))
    
    second = input()


if len(first) == 3:
        
    first_print = first + ' '
        
elif len(first) == 1:
        
    first_print = ' ' + first + '  '
        
else:
        
    first_print = ' ' + first + ' '

print('{}{}'.format(spacer, first_print.rstrip()))
