'''
Created on 2015. 11. 3.

@student_name: Seungjae Kim
@student_number: 01406225
'''

def vector(seq):
    
    '''
    >>> vector('GACCCTTGT')
    [(0, 0), (0, -1), (-1, -1), (-1, 0), (-1, 1), (-1, 2), (0, 2), (1, 2), (1, 1), (2, 1)]
    >>> vector('CTGGGGTAA')
    [(0, 0), (0, 1), (1, 1), (1, 0), (1, -1), (1, -2), (1, -3), (2, -3), (1, -3), (0, -3)]
    
    '''
    
    # set variables for recording vector moves.
    # set the origin variable.
    vector_move = []
    vector_move.append((0,0))
    
    # according to the sequence, record the moves in the list, 'vector move'
    for char in seq:
        pos_x = vector_move[-1][0]
        pos_y = vector_move[-1][1]
        
        if char == 'G':
            pos_y -= 1
            
        elif char == 'C':
            pos_y += 1
            
        elif char == 'A':
            pos_x -= 1
        
        elif char == 'T': 
            pos_x += 1
            
        vector_move.append((pos_x,pos_y))
    
    # return the recorded vector moves.
    return vector_move

def replication(seq):
    
    '''
    >>> replication('GACCCTTGT')
    (5, 1)
    >>> replication('CTGGGGTAA')
    (1, 6)
    '''
    
    # record the moves of the replication.
    vector_move = vector(seq)
    
    # set blank variables to store only the y-coordinate moves.
    list_y = []
    
    # From the vector moves, only take the y-coordinate moves.
    for pointx,pointy in vector_move:
        list_y.append(pointy)
    
    # find the highest and lowest y values.
    highest = max(list_y)
    lowest = min(list_y)
    
    # return when the highest and the lowest appears
    return list_y.index(highest), list_y.index(lowest)

def sequence(vector_move):

    '''
    >>> sequence([(0, 0), (0, -1), (-1, -1), (-1, 0), (-1, 1), (-1, 2), (0, 2), (1, 2), (1, 1), (2, 1)])
    'GACCCTTGT'
    >>> sequence([(0, 0), (0, 1), (1, 1), (1, 0), (1, -1), (1, -2), (1, -3), (2, -3), (1, -3), (0, -3)])
    'CTGGGGTAA'
        
    '''

    # set blank string.
    seq = ''
    
    # set the origins
    originx, originy = vector_move[0]
    
    # From the vector moves, record which base incurred such moves in the 'seq' string.
    for pointx,pointy in vector_move[1:]:
        
        if originx + 1 == pointx:
            seq += 'T'
        elif originx - 1 == pointx:
            seq += 'A'
        elif originy + 1 == pointy:
            seq += 'C'
        elif originy - 1 == pointy:
            seq += 'G'
        
        originx = pointx
        originy = pointy
        
    return seq

if __name__ == '__main__':
    import doctest
    doctest.testmod()