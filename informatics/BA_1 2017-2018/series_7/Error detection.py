import random
def draw(drawn = None):
    '''
    >>> draw()
    '6S'
    >>> draw(['6H', '3C', '3D', '8C', 'AD', '9D', '7D', 'QC'])
    '4D'
    >>> draw(drawn=('3S', '8H', '8C', '2H', 'AC'))
    'XH'
    >>> draw({'4C', 'AH', 'JS', '7S', '9H', '2H', 'QC', '2S', '3H', '7C'})
    '9S'
    '''
    rank = ['A','2','3','4','5','6','7','8','9','X','J','Q','K']
    suit = ['S','H','C','D']
    total = []
    if drawn != None:
        for shape in suit:
            for number in rank:
                card = number + shape
                if card not in drawn:
                    total.append(card)
    if drawn == None:
        for shape in suit:
            for number in rank:
                card = number + shape
                total.append(card)
    return random.choice(total)

def arrange(rows = None, cols = None):
    '''
    >>> arrange(rows=3, cols=4)
    [['5D', '4D', '4C', '9S'], ['2D', '6C', '4S', 'AD'], ['QH', 'QS', '2S', '3D']]
    >>> arrange(rows=7, cols=8)
    Traceback (most recent call last):
    AssertionError: invalid grid

    '''
    if rows == None:
        rows = 5
    if cols == None:
        cols = 5
    if rows * cols < 53:
        total = []
        row = []
        for i in range(rows):
            col = []
            for j in range(cols):
                drawn = draw(total)
                total.append(drawn)
                col.append(drawn)
                if j == cols-1:
                    row.append(col)
        return row
    if rows * cols > 52:
        raise AssertionError('invalid grid')

def extend(grid):
    row = len(grid)
    col = len(grid[0])
    total = []
    new = []
    if (row+1)*(col+1)<=52:
        for i in grid:
            for j in i:
                total.append(j)
        for x in grid:
            new_row= []
            count = 0
            for y in x:
                new_row.append(y)
                count += 1
                if count == col:
                    a = draw(total)
                    total.append(a)
                    new_row.append(a)
                    new.append(new_row)

        add_row = []
        for y in range(col+1):
            b = draw(total)
            add_row.append(b)
            total.append(b)
        new.append(add_row)
        grid.clear()
        for f in new:
            col = []
            for g in f:
                col.append(g)
            grid.append(col)
        return grid
        return extend(grid)
    if (row+1)*(col+1) > 52:
        raise AssertionError('invalid grid')

def select(grid):
    x = len(grid)
    y = len(grid[0])
    row = []
    col = []
    for i in range(x):
        row.append(i)
    for j in range(y):
        col.append(j)

    a = random.choice(row)
    b = random.choice(col)
    postion = [a,b]
    return tuple(postion)