'''
Created on 2016. 2. 1.

@author: User
'''
def SNP(seq1, seq2):
    
    if len(seq1) != len(seq2):
        return None
    
    list1 = []
    pos = 0
    
    while pos < len(seq1):
        
        if seq1[pos] != seq2[pos]:
            list1.append((pos,seq1[pos],seq2[pos]))
            
        pos += 1
                
    if len(list1) == 1:
        return list1[0]
    
def SNPs(DNA, seq):
    
    pos = 0
    std = len(seq)
    list1 = []
    
    while std <= len(DNA):
        
        if SNP(DNA[pos:std],seq):
            count = pos + SNP(DNA[pos:std],seq)[0]
            list1.append(count)
            
        pos += 1
        std += 1
            
    return sorted(list1)