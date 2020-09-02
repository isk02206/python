def listRepresentation(digits, columns):
    '''
    >>> listRepresentation('111222333', 3)
    [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
    >>> listRepresentation('123321123', 3)
    [[1, 2, 3], [3, 2, 1], [1, 2, 3]]
    >>> listRepresentation('424313424', 3)
    [[4, 2, 4], [3, 1, 3], [4, 2, 4]]
    >>> listRepresentation('1541253263631421', 4)
    [[1, 5, 4, 1], [2, 5, 3, 2], [6, 3, 6, 3], [1, 4, 2, 1]]
    >>> listRepresentation('1541253263631421', 5)
    Traceback (most recent call last):
    AssertionError: invalid string representation
    '''
    major = []
    minor = []
    count = 0
    if len(digits) % columns != 0:
        raise AssertionError('invalid string representation')
    for i in digits:
        minor.append(int(i))
        count += 1
        if count == columns:
            major.append(minor)
            minor = []
            count =0
    return major

def neighbours(row, column, grid):
    '''
    >>> grid = [[1, 5, 4, 1], [2, 5, 3, 2], [6, 3, 6, 3], [1, 4, 2, 1]]
    >>> neighbours(2, 2, grid)
    {1, 2, 3, 4, 5}
    >>> neighbours(2, 3, grid)
    {1, 2, 3, 6}
    >>> neighbours(0, 0, grid)
    {2, 5}
    >>> neighbours(4, 4, grid)
    Traceback (most recent call last):
    AssertionError: invalid position
    '''
    total_row = len(grid) - 1
    total_column = len(grid[0]) - 1
    result = []
    if row > total_row or column > total_column:
        raise AssertionError('invalid position')
    chosen = grid[row][column]

    if total_column - column == 0:
        b, y = 2, row-1
        if total_row - row == 0:
            a, x = 2, column-1
        if row == 0:
            a, x = 2, column
        if total_row - row != 0 and row != 0:
            a, x = 3, column-1
    elif column == 0:
        b, y = 2, row
        if total_row - row == 0:
            a, x = 2, column-1
        if row == 0:
            a, x = 2, column
        if total_row - row != 0 and row != 0:
            a, x = 3, column-1
    if column != 0 and total_column - column != 0:
        b, y = 3, row-1
        if total_row - row == 0:
            a, x = 2, column-1
        if row == 0:
            a, x = 2, column
        if total_row - row != 0 and row != 0:
            a, x = 3, column-1
    if y == -1:
        y = 0

    for i in range(a):  # row
        sel_grid = grid[y + i]
        for j in range(b):  # column
            result.append(sel_grid[x + j])
    result.remove(chosen)
    return set(result)
