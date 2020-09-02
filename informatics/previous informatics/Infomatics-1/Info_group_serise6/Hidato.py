'''
Created on 2016. 1. 29.

@author: User
'''
import math
def first(list1):
    
    for seq in list1:
        
        if 1 in seq:
            
            pos1 = list1.index(seq)
            pos2 = seq.index(1)
            
            return pos1,pos2
        
def successor(seq, row, column):
    
    val1 = seq[row][column]
    
    val2 = val1 + 1
    
    for list1 in seq:
        
        if val2 in list1:
            
            row2 = seq.index(list1)
            column2 = list1.index(val2)
    
            sub1 = int(math.fabs(row - row2))
            sub2 = int(math.fabs(column - column2))
    
            if (sub1 == 1 and sub2 == 1) or sub1 + sub2 == 1:
        
                return row2, column2
    
            else:
                return (None,None)
            
    return None,None
    
def last(list1):
    
    
    row,column = first(list1)
    
    while successor(list1, row, column) != (None,None):
        
        row,column = successor(list1, row, column)
        
    return row,column

def hidato(list1):
    
    last_one = 0
    
    for seq in list1:
        
        last_one += len(seq)
    
    row,column = last(list1)
    
    while (row,column) != (None,None):
        
        if list1[row][column] == last_one:
            
            return True
        
        else:
            return False
        
    else:
        return False