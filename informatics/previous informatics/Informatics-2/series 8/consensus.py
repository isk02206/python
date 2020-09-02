'''
Created on 2015. 12. 2.

@author: User
'''
def profile(seqs):
    dict = {}
    for x in range(len(seqs[0])):
        count_A = 0
        count_T = 0
        count_C = 0
        count_G = 0
        for seq in seqs:
            assert len(seq)== len(seqs[0]),'sequences should have equal length'
            if seq[x] == 'A':
               count_A += 1
            elif seq[x] == 'T':
               count_T += 1
            elif seq[x] == 'C':
               count_C += 1
            elif seq[x] == 'G':
               count_G += 1
        dict.setdefault('A',[]).append(count_A)
        dict.setdefault('G',[]).append(count_G)
        dict.setdefault('T',[]).append(count_T)
        dict.setdefault('C',[]).append(count_C)
            
        count_A = 0
        count_T = 0
        count_C = 0
        count_G = 0
    return dict

def consensus(profile):
    result = ''
    
    group_value = []
    group_key = []
    
    for keys,values in profile.items():
        group_value.append(values)
        group_key.append(keys)
    compare = []
    
    for pos in range(len(group_value[0])):
        for char in group_value:
            compare.append(char[pos])
        if compare.count(max(compare)) >= 2:
            result += 'N'
        else:
            result += group_key[compare.index(max(compare))]
        compare = []
    return result
