'''
Created on 2014. 11. 4.

@author: TaeWoo Jung
'''

def groups(grid):
    
    position, counter = {}, 0
    
    for row in grid:
        for number in range(len(row)):
            index = (counter, number)
            
            if row[number] in position:
                position[row[number]].add(index)
            else:
                position[row[number]] =  position.get(index, {index})
                
        counter += 1
            
    return position

def connected(points):
    
    original = len(points)
    connected = {points.pop()}
    
    while points:
        check = set()
        
        for connected_point in connected:
            (x, y) = connected_point
            check.add((x + 1, y)), check.add((x - 1, y))
            check.add((x, y + 1)), check.add((x, y - 1))
            
        for point in points:
            if point in check:
                connected.add(point)
                break
        
        points.remove(point)

    if len(connected) == original:
        return True
            
    else:
        return False

def equidivision(grid):
    
    value_dic, check = groups(grid), set()
    positions = list(value_dic.values())
    length = set()
    
    for position in positions:
        
        length.add(len(position))
        check.add(connected(position))
    
        if False in check or len(length) != 1:
            
            return False
            break
    
    return True