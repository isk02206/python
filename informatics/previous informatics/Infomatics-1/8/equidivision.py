'''
Created on 2016. 2. 13.

@author: User
'''
def groups(grid):
    
    dict1 = dict()
    pos1 = 0
    pos2 = 0
    #e.g. [[1,2,3][1,1,1][1,2,3]]
    #grid[pos1]ดย [1,2,3]
    #grid[pos1][pos2] ดย  [1]
    while pos1 < len(grid):
        while pos2< len(grid[pos1]):
            
            a = grid[pos1][pos2]
            dict1.setdefault(a, set()).add((pos1,pos2))
        
            pos2 += 1
        pos1 += 1
        pos2 = 0
        
    return dict1

def connected(list1):
    
    list1 = sorted(list(list1))
    start = list1[-1]
    
    while len(list1) != 1:
        
        a,b = start
        print(start)
        if tuple((a,b-1)) in list1:
            list1.remove(start)
            start = tuple((a,b-1))
            
        elif tuple((a-1,b)) in list1:
            list1.remove(start)
            start = tuple((a-1,b))
        
        else:
            return False
    else:
        return True
    
print(connected({(1, 2), (1, 3), (2, 2), (0, 3), (0, 4)}))

def equidivision(grid):
    
    dict1 = groups(grid)
    
    for val in dict1.values():
        
        if not connected(val):
            return False
        
    return True