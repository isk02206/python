'''
Created on 2017. 6. 16.

student_name: TaeWoo Jung

'''

def transition(b1, b2): # nucleotide 1, nucleotide 2
    
    '''
    >>> transition('G', 'A')
    True
    >>> transition('t', 'g')
    False
    >>> transition('C', 'c')
    False
    '''
    
    # make sure inputs are all uppercase letter
    b1, b2 = b1.upper(), b2.upper()
    # this is dictionary containing information about transition
    transition_guide = {'G': 'A', 'A': 'G', 'C':'T', 'T':'C'}
    
    # if replace cause transition mutation,
    if transition_guide[b1] == b2:
        return True
    # if those combinations doesn't cause transition mutation
    else:
        return False
    
def transversion(b1, b2): # nucleotide 1, nucleotide 2
    
    '''
    >>> transversion('G', 'A')
    False
    >>> transversion('t', 'g')
    True
    >>> transversion('C', 'c')
    False
    '''
    
    # make sure inputs are all uppercase letter
    b1, b2 = b1.upper(), b2.upper()
    # this is dictionary containing information about transversion
    transversion_guide = {'A':['C', 'T'], 'C':['A', 'G'], 'G':['C', 'T'], 'T':['A', 'G']}
    
    # if replace cause transversion mutation,
    if b2 in transversion_guide[b1] and b1 != b2:
        return True
    # if those combinations doesn't cause transversion mutation
    else:
        return False
    
def ratio(s1, s2): # DNA sequence 1, DNA sequence 2
    
    '''   
    >>> ratio('ATTAGCATTATCATC', 'AAATAGGATATATGG')
    0.2222222222222222

    >>> seq1 = 'GCAACGCACAACGAAAACCCTTAGGGACTGGATTATTTCGTGATCGTTGTAGTTATTGGAAGTACGGGCATCAACCCAGTT'
    >>> seq2 = 'ttatctgacaaagaaagccgtcaacggctggataatttcgcgatcgtgctggttactggcggtacgagtgttcctttgggt'
    >>> ratio(seq1, seq2)
    1.2142857142857142
    '''
    
    # make sure inputs are all uppercase letter
    s1, s2 = s1.upper(), s2.upper()
    
    # number of transition and transversion can occur between two sequences
    transition_count = 0
    transversion_count = 0
    # going through each sequence and compare it
    for base in range(len(s1)):
        
        # if two bases combination can cause transition mutation, 
        if transition(s1[base], s2[base]) is True:        
            transition_count += 1
        
        # if two bases combination can cause transversion mutation,
        if transversion(s1[base], s2[base]) is True:
            transversion_count += 1
    
    # if there is no transversion possibility, ratio is 0
    if transversion_count == 0:
        return 0.0
    
    # ratio by dividing number of transition by number of transversion
    return transition_count / transversion_count 

if __name__ == '__main__':
    import doctest
    doctest.testmod()
