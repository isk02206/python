def profile(seqs):
    '''
    >>> seqs = ['GCAAAACG', 'GCGAAACT', 'TACCTTCA', 'TATGTTCA', 'GCCTTAGG', 'GACTTATA', 'TCGGATCC']
    >>> profile(seqs)
    {'A': [0, 3, 1, 2, 3, 4, 0, 3], 'C': [0, 4, 3, 1, 0, 0, 5, 1], 'T': [3, 0, 1, 2, 4, 3, 1, 1], 'G': [4, 0, 2, 2, 0, 0, 1, 2]}
    '''
    length = len(seqs[0])
    for i in seqs:
        if len(i) != length:
            raise AssertionError('sequences should have equal length')
    

