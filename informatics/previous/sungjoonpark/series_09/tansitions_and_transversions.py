def transitions(a,b):
    '''
    >>> transition('G', 'A')
    True
    >>> transition('t', 'g')
    False
    >>> transition('C', 'c')
    False
    '''
    a = a.lower()
    b = b.lower()
    if a == 'a' and b == 'g':
        return True
    if a == 'g' and b == 'a':
        return True
    if a == 'c' and b == 't':
        return True
    if a == 't' and b == 'c':
        return True
    else:
        return False

def transversion(a,b):
    '''
    >>> transversion('G', 'A')
    False
    >>> transversion('t', 'g')
    True
    >>> transversion('C', 'c')
    False
    '''
    a = a.lower()
    b = b.lower()
    if a == 'a':
        if b == 'c':
            return True
        if b == 't':
            return True
    if a == 'g':
        if b == 'c':
            return True
        if b == 't':
            return True
    if a == 'c':
        if b == 'a':
            return True
        if b == 'g':
            return True
    if a == 't':
        if b == 'a':
            return True
        if b == 'g':
            return True
    else:
        return False

def ratio(s1,s2):
    '''
    >>> ratio('ATTAGCATTATCATC', 'AAATAGGATATATGG')
    0.2222222222222222
    >>> seq1 = 'GCAACGCACAACGAAAACCCTTAGGGACTGGATTATTTCGTGATCGTTGTAGTTATTGGAAGTACGGGCATCAACCCAGTT'
    >>> seq2 = 'ttatctgacaaagaaagccgtcaacggctggataatttcgcgatcgtgctggttactggcggtacgagtgttcctttgggt'
    >>> ratio(seq1, seq2)
    1.2142857142857142
    '''
    for i in range(len(s1)):
        list_seq1 = []
        list_seq2 = []
        transition_count = 0
        transversion_count = 0
        list_seq1.append(s1[i+1])
        list_seq2.append(s2[i+1])
        if transitions(list_seq1,list_seq2) == True:
            transition_count = transition_count +1
        if transversion(list_seq1,list_seq2) == True:
            transversion_count = transversion_count +1
    
    return transition_count / transversion_count
    
