'''
Created on 2018. 1. 16.

@author: TaeWoo
'''

def merge(chutes, ladders):
    
    board = dict()
    
    for chute in chutes:
        
        assert chute > chutes[chute], 'invalid configuration'
        assert chute not in ladders, 'invalid configuration'
        board[chute] = chutes[chute] - chute
        
    for ladder in ladders:
        
        assert ladder < ladders[ladder], 'invalid configuration'
        assert ladder not in chutes, 'invalid configuration'
        board[ladder] = ladders[ladder] - ladder
        
    return board

def spaces(moves, chutes, ladders):
    
    position = 0
    board = merge(chutes, ladders)
    path = []
    
    for move in moves:
        
        if position + move <= 100:
            position += move
        
        if position in chutes:
            position = chutes[position]
            
        elif position in ladders:
            position = ladders[position]
            
        path.append(position)
        
    return path
    


chutes = {98: 78, 95: 75, 93: 73, 87: 24, 64: 60, 62: 19, 56: 53, 49: 11, 47: 26, 16: 6}
ladders = {1: 38, 4: 14, 9: 31, 21: 42, 28: 84, 36: 44, 51: 67, 71: 91, 80: 100}
print(merge(chutes, ladders))
print(spaces([6] * 14, chutes, ladders))