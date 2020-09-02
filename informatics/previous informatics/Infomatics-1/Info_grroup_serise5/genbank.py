'''
Created on 2016. 1. 25.

@author: User
'''
def genbank(m,n,seq):
    #첫번쨰오는 숫자의 갯수를 구하는거 예) 932는 3개  , 23 은 2개
    positions = len(str(len(seq) - m*n))
    seq = seq.lower()
    
    list1 = []
    
    pos = 1
    
    if len(str(pos)) < positions:
        
        list2 = [(positions - len(str(pos))) * ' ' + str(pos)]
    
    sub = ''
    
    for char in seq:
        
        sub += char
        
        if len(sub) == m:
            
            list2.append(sub)
            
            sub = ''
        
        if len(list2) == n +1:
            
            pos += m*n
            
            list1.append(' '.join(list2))
            
            if len(str(pos)) <= positions:
        
                list2 = [(positions - len(str(pos))) * ' ' + str(pos)]
            
    if sub != '':
        list2.append(sub)
        
    if len(list2) != 1:
        
        
        list1.append(' '.join(list2))
            
    return '\n'.join(list1)
