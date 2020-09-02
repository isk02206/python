'''
Created on 2018. 1. 23.

@author: TaeWoo
'''

def profile(seqs):
    
    assert len(set([len(i) for i in seqs])) == 1, 'sequences should have equal length'
    result = {'A':[], 'T':[], 'C':[], 'G':[]}
    
    for column in range(len(seqs[0])):
        
        bases = [i[column] for i in seqs]
        
        result['A'].append(bases.count('A'))
        result['C'].append(bases.count('C'))
        result['G'].append(bases.count('G'))
        result['T'].append(bases.count('T'))
    
    return result

def consensus(profile):
    
    counts = []
    adjust = [profile['A'], profile['C'], profile['G'], profile['T']]
    
    for column in range(len(profile['A'])):
        counts.append([i[column] for i in adjust])
    
    result = ''
    positions = {0:'A', 1:'C', 2:'G', 3:'T'}
    
    for column in counts:
        highest = max(column)
        if column.count(highest) == 1:
            result += positions[column.index(highest)]
        
        else:
            result += 'N'
    
    return result

seqs = ['GCAAAACG', 'GCGAAACT', 'TACCTTCA', 'TATGTTCA', 'GCCTTAGG', 'GACTTATA', 'TCGGATCC']
print(consensus(profile(seqs)))
