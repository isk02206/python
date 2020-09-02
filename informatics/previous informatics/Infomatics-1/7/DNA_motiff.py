'''
Created on 2016. 2. 5.

@author: User
'''
def motifs(seq, sub, begin = None, end = None):
    
    if begin == None:
        begin = 0
        
    if end == None:
        end = len(seq)
        
    list1 = []
    
    while begin < end:
            #예를 들어서 begin이 0일떄 sub가 2일떄
            #seq[0:2] 
        if seq[begin:begin +len(sub)] == sub:
            
            list1.append(begin)
            
        begin += 1
            
    return list1