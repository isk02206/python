'''
Created on 2016. 1. 29.

@author: User
'''

def repeatlength(seq1, check):
    
    seq1 = seq1.upper()
    check = check.upper()
    list1 = []
    
    pos = 0
    
    count = 0
    
    while pos < len(seq1):
        
        if seq1[pos:pos + len(check)] == check:
            
            count += 1
            
            pos += len(check)
            
        else:
            
            list1.append(count)
            
            count = 0            
            pos += 1
            
    list1.append(count)
    
    return max(list1)
    # y 가 x에 속해있고y가 list에 속해있는 경우
    #return max(x for x in list,y for y in x)
def HuntingtonDiagnosis(seq):
    
    count = repeatlength(seq, 'CAG')
    
    if count < 27:
        return 'normal'
    
    elif 27 <= count <= 35:
        
        return 'low risk'
    
    elif 36 <= count <= 39:
        
        return 'increased risk'
    
    elif count > 39:
        
        return 'absolute risk'