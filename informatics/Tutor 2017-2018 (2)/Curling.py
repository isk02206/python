'''
Created on 2018. 7. 2.

@author: TaeWoo
'''

from math import pi, sqrt

def inHouse(x, y, inch=True):     # set default value
    
    '''
    >>> inHouse(70.0, 0.0)
    True
    >>> inHouse(70.0, 0.0, inch=False)
    False
    >>> inHouse(78.0, 0.0)
    False
    '''
    
    r_stone = 36 / (2*pi)   # radius of stone in inch
    r_house = 6 * 12        # radius of house in inch
    
    # Convert inch into meter
    if inch is False:
        r_stone *= 0.0254
        r_house *= 0.0254
        
    # Calculate distance from center of house to center of stone 
    distance = sqrt(float(x)**2 + float(y)**2)
    
    # Determine whether stone overlap with the house or not
    if distance > r_house:
        
        # Check whether stone overlaps or not
        # Stone overlap
        if r_house >= distance - r_stone:
            return True
        
        # Stone doesn't overlap
        return False
    
    # Case where stone in the house
    return True
    
def validPositions(positions, inch=True):
        
    r_stone = 36 / (2*pi)   # radius of stone in inch
    r_house = 6 * 12        # radius of house in inch
    
    # Convert inch into meter
    if inch is False:
        r_stone *= 0.0254
        r_house *= 0.0254
    
    # Set empty list to record color of stones present
    colors = []
    # Check whether number of stones are valid
    for position in positions:
        colors.append(position[2])
    
    # Count number of yellow stones and red stones    
    number_yellow = colors.count('Y')
    number_red = colors.count('R')
    
    # If number of either red or yellow stones are greater than 8, it is not valid 
    if number_yellow > 8 or number_red > 8:
        return False
    
    # Check whether positions of each stones are valid (OVERLAPPING IMPOSSIBLE)
    for p1 in positions:
        for p2 in positions:
            if p1 != p2:
                
                x1, x2 = float(p1[0]), float(p2[0])
                y1, y2 = float(p1[1]), float(p2[1])
                # Calculate distance between two stones
                distance = sqrt((x2-x1)**2 + (y2-y1)**2)
                
                # This means stones are overlapping
                if distance < (2 * r_stone):
                    return False
    
    # Positions of stones are valid
    return True


def score(positions, inch=True):
    
    # Check whether positions of each stones are valid
    assert validPositions(positions, inch) is True, 'invalid stone positions'
    
    # Remove all the stones which are out of house [THIS IS EXTRA]
    stones_inhouse = [position for position in positions if inHouse(position[0], position[1], inch)]
    
    # CASE 1: If no stones are in the house
    if len(stones_inhouse) == 0:
        return (0, 0)
    
    R_distance = []     # distance of each red stone from the center of house
    Y_distance = []     # distance of each yellow stone from the center of house
    
    # Record distance
    for position in stones_inhouse:
        x = float(position[0])
        y = float(position[1])
        # Calculate distance
        distance = sqrt(float(x)**2 + float(y)**2)
        
        if position[2] == 'R':
            R_distance.append(distance)
            
        else:
            Y_distance.append(distance)
    
    Score_R = 0
    Score_Y = 0
    
    # CASE 2: Only red stones in house
    if len(Y_distance) == 0:
        return (len(R_distance), Score_Y)
    
    # CASE 3: Only yellow stones in house
    if len(R_distance) == 0:
        return (Score_R, len(Y_distance))
    
    # CASE 4: Red stone is closest to the center of house
    if min(R_distance) < min(Y_distance):
        
        for distance in R_distance:
            if distance < min(Y_distance):
                Score_R += 1
                
    # CASE 5: Yellow stone is closest to the center of house
    if min(R_distance) > min(Y_distance):
        
        for distance in Y_distance:
            if distance < min(R_distance):
                Score_Y += 1
    
    # Return final score
    return (Score_R, Score_Y)

'''
>>> inHouse(70.0, 0.0)
True
>>> inHouse(70.0, 0.0, inch=False)
False
>>> inHouse(78.0, 0.0)
False

>>> validPositions([(20.0, 10.0, 'R'), (25.0, 22.0, 'Y'), (42.0, 37.0, 'R')])
True
>>> validPositions([(20.0, 10.0, 'R'), (25.0, 22.0, 'R'), (42.0, 37.0, 'Y')])
True
>>> validPositions([(20.0, 10.0, 'R'), (25.0, 22.0, 'R'), (42.0, 37.0, 'R')])
True
>>> validPositions([(20.0, 10.0, 'R'), (20.0, 22.0, 'Y'), (20.0, 10.0, 'Y')])
False

>>> score([(20.0, 10.0, 'R'), (25.0, 22.0, 'Y'), (42.0, 37.0, 'R')])
(1, 0)
>>> score([(20.0, 10.0, 'R'), (25.0, 22.0, 'R'), (42.0, 37.0, 'Y')])
(2, 0)
>>> score([(20.0, 10.0, 'R'), (25.0, 22.0, 'R'), (42.0, 37.0, 'R')])
(3, 0)
>>> score([(0.508, 0.254, 'R'), (0.635, 0.5588, 'Y'), (1.0668, 0.9398, 'R')], False)
(1, 0)
>>> score([(0.508, 0.254, 'R'), (0.635, 0.5588, 'R'), (1.0668, 0.9398, 'Y')], inch=False)
(2, 0)
>>> score([(0.508, 0.254, 'R'), (0.635, 0.5588, 'R'), (1.0668, 0.9398, 'R')], False)
(3, 0)
 
'''

if __name__ == "__main__":
    import doctest
    doctest.testmod()