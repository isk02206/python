'''
Created on 2018. 1. 29.

@author: TaeWoo
'''
#image = '.8\n...........................................\n...........................................\n....................88.....................\n.................88888888..................\n...............888888888888................\n............888888......888888.............\n.........888888............888888..........\n......888888..................888888.......\n....888888......................888888.....\n....888............................888.....\n...........................................\n......888888888888888888888888888888.......\n........88888888888888888888888888.........\n...........................................\n...........................................\n........88..88..88..88..88..88..88.........\n........88..88..88..88..88..88..88.........\n........88..88..88..88..88..88..88.........\n........88..88..88..88..88..88..88.........\n........88..88..88..88..88..88..88.........\n........88..88..88..88..88..82..88.........\n........88..88..88..88..88..88..88.........\n........88..88..88..88..88..88..88.........\n........88..88..88..88..88..88..88.........\n........88..88..88..88..88..88..88.........\n........88..88..88..88..88..88..88.........\n........88..88..88..88..88..88..88.........\n...........................................\n...........................................\n......888888888888888888888888888888.......\n......888888888888888888888888888888.......\n...........................................\n....8888888888888888888888888888888888.....\n....8888888888888888888888888888888888.....\n...........................................\n...........................................'
image = input()

repeated = list(image)
image_list = []
row_position = 1

while True:
    image = input()
    column_position = 1
    
    for column in image:
        
        if column not in repeated:
            break
        
        column_position += 1
    
    if column not in repeated:
        break
    
    row_position += 1

print("character '{}' only occurs at row {} and column {}".format(column, row_position, column_position))