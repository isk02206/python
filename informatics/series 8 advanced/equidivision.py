'''
Created on 2018. 11. 14
@Subject : equidivision
@Author : Son Jee Hun
@Student Number : 01406444
'''
def groups(grid):
    '''
    >>> grid = [[1, 1, 1], [2, 2, 3], [2, 3, 3]]
    >>> groups(grid)
    {1: {(0, 1), (0, 0), (0, 2)}, 2: {(2, 0), (1, 0), (1, 1)}, 3: {(1, 2), (2, 1), (2, 2)}}
    >>> grid = [[1, 1, 1, 5, 5], [2, 1, 5, 5, 4], [2, 1, 5, 4, 4], [2, 2, 4, 4, 3], [2, 3, 3, 3, 3]]
    >>> groups(grid)
    {1: {(0, 1), (0, 0), (0, 2), (2, 1), (1, 1)}, 2: {(3, 0), (2, 0), (1, 0), (3, 1), (4, 0)}, 3: {(4, 1), (4, 4), (3, 4), (4, 3), (4, 2)}, 4: {(3, 2), (2, 3), (2, 4), (1, 4), (3, 3)}, 5: {(1, 2), (0, 3), (1, 3), (2, 2), (0, 4)}}
    '''
    result = {}
    for row in range(len(grid)):
        for column in range(len(grid[row])):
            number = grid[row][column] #find grid index position
            if number in result: # if list in list value in result add index position
                result[number].add((row, column))
            else: # if list in list value none add key
                result[number] = {(row, column)}
    return result

def connected(position):
    '''
    >>> connected({(1, 2), (1, 3), (2, 2), (0, 3), (0, 4)})
    True
    >>> connected({(1, 2), (1, 4), (2, 2), (0, 3), (0, 4)})
    False
    '''
    neighbor = set()
    connect = position
    neighbor.add(connect.pop()) #choose one and then remove choose one

    while neighbor:
        position_x, position_y = neighbor.pop() # neighbor choose one value x,y
        spacing = ((0, 1), (0, -1), (-1, 0), (1, 0)) # possible moving space
        for moving_x, moving_y in spacing:
            if (position_x + moving_x, position_y + moving_y) in connect:
                neighbor.add((position_x + moving_x, position_y + moving_y)) # add neighbor position
                connect.remove((position_x + moving_x, position_y + moving_y))
                # connet position remove because connet postion
    if not connect:
        return True
    return False


def equidivision(grid):
    '''
    >>> grid = [[1, 1, 1], [2, 2, 3], [2, 3, 3]]
    >>> equidivision(grid)
    True

    >>> grid = [[1, 1, 1], [2, 2, 3], [3, 3, 2]]
    >>> equidivision(grid)
    False

    >>> grid = [[1, 1, 1, 5, 5], [2, 1, 5, 5, 4], [2, 1, 5, 4, 4], [2, 2, 4, 4, 3], [2, 3, 3, 3, 3]]
    >>> equidivision(grid)
    True
    '''
    for group in groups(grid).values():
        if len(group) != len(grid): # length of dictionary value not equal length of list is False
            return False
        if not connected(group): # not connet False
            return False
    return True

if __name__ == '__main__':
    import doctest
    doctest.testmod()

