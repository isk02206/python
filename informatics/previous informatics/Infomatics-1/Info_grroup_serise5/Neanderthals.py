'''
Created on 2016. 1. 22.

@author: User
'''
def score(seq1,seq2):
    
    if seq1 == '-' and seq2 == '-':
        return float(0) #0.0
        
    elif seq1 == '-' and seq2 != '-':
        return float(-1)
            
    elif seq1 != '-' and seq2 == '-':
        return float(-1)
            
    else:
        if seq1 == seq2:
            return float(1)
        else:
            return float(0)
    
def scores(list):
    
    return (list[2] - list[1]) / list[0]


def similarity(seq1,seq2):
    
    list1 = [seq1,seq2]
    
    list2 = []
    
    total = len(seq1)
    
    hole = 0
    
    match = 0
    
    mismatch = 0
    
    for x in range(len(seq1)):
        
        if seq1[x] == '-' and seq2[x] == '-':
            total -= 1
        
        elif seq1[x] == '-' and seq2[x] != '-':
            hole += 1
            
        elif seq1[x] != '-' and seq2[x] == '-':
            hole += 1
            
        else:
            if seq1[x] == seq2[x]:
                match += 1
            else:
                mismatch -= 1
                
    list2.append(total)
    list2.append(hole)
    list2.append(match)
    list2.append(mismatch)
    
    return scores(list2)

print(similarity('CTG-GGG---GTGTAC', 'CTACGGG---GCGTCC'))
print(score('C', 'C'))