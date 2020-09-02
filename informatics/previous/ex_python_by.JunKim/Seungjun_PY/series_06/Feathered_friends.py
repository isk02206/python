'''
Created on 2015. 11. 20.
@Group_number: 14
@author: Seungjun Kim
@student_number: 01503749
'''
# change the label, x, which is a number, into letter.
# change the label, y, into the given format. (adding one to y)

def coord2label(x, y):
    letter= chr(ord('A')+ x)
    number= y + 1
    return letter + str(number)

# reverse version of coord2label function.

def label2coord(x):
    letter= ord(x[0]) - 65
    z= ''
    for y in x:
        if y.isdigit():
            z += y
            number = int(z) - 1 
    return (letter, number)

def observation(row, map, coordinate):
    
    # calculate the length of one row.
    
    length_of_one_row = len(map)/row
    
    # make a blank string.
    
    num= ''
    
    # if the coordinate is on the first row,
    # consider only the position number of the coordinate in the first row.
    # From the front of the map, find the character after moving the given position number.
    
    if coordinate[0] == 'A':
        for char in coordinate:
            if char.isdigit() == True:
                num+= char
        observation = map[int(num)-1]        
    
    # if the coordinate isn't on the first row,
    # consider the row number with the position number.
    # After moving the row number, then consider the postiion number and find the character.
    
    elif coordinate[0] != 'A':
        row2 =  length_of_one_row * (ord(coordinate[0]) - 65)
        for char in coordinate:
            if char.isdigit() == True:
                num += char
        observation = map[int(row2)+int(num)-1]
    
    return observation

def endpoint(row, map, coordinate, direction):   
    
    # if the starting character isn't same with the identified component of the map, 
    # the route isn't valid so that return None in this case.
    
    if observation(row, map, coordinate) != direction[0]:
        return None
    
    # select only the movement symbols in the direction and put them into upper_case.
    
    upper_case= ''
    for x in direction:
        if x.isupper() == True:
            upper_case += x
    
    # find the starting position from the coordinate.
    
    number= ''
    for y in coordinate:
        if y.isdigit() == True:
            number += y
   
    # change the first number in the coordinate into letter.
    # change the other numbers in the coordinate into the given format.
    
    x_axis= ord(coordinate[0]) - 65
    y_axis= int(number) - 1
    
    # set blank strings
    z = ''
    check2 = ''
    
    # move the positions according to the directions in the upper_case.
    # Then, add the characters of destinations into a blank string.
    
    for direction2 in upper_case:
        if direction2 == 'U':
            x_axis -= 1
            if x_axis < 0:
                x_axis += 1

        if direction2 == 'D':
            x_axis += 1 
            if x_axis > row-1:
                x_axis -= 1

        if direction2 == 'L':
            y_axis -= 1
            if y_axis < 0:
                y_axis = 0

        if direction2 == 'R':
            y_axis += 1 
            if y_axis == len(map)//row: 
                y_axis = len(map)//row - 1

        z += observation(row, map, coord2label(x_axis, y_axis))
    
    # check whether the route was valid or not.
    # return the end point once the route is valid.
    # Otherwise, return None.
    
    for check in direction[2::2]:
        check2 += check
    if check2 != z:
        return None            
    return coord2label(x_axis, y_axis)

def beehives(row, map, direction):
    
    # make a blank list, 'answer', which will be filled with possible starting positions.
    
    answer= []
    
    # check every position of the map and check if the given route, 'direction', can be proceeded at the position.
    
    for x1 in range(row):
        set_row = chr(65+x1)
        for y1 in range(len(map)//row):
            set_column = set_row + str(y1 + 1)
            y = observation(row, map, set_column)
            if y == direction[0]:
                coordinate = set_column
                z = endpoint(row, map, coordinate, direction)
                if z == None:
                    z= ''
                else:
                    z1 = observation(row, map, z)

                    if z1 == direction[-1] and z not in answer:
                        answer += [z]
    
    # arrange the list in the lexicographical order.
    
    return sorted(answer)