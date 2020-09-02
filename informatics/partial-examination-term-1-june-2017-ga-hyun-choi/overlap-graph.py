def overlap(read1, read2, k):
    '''

    :param read1:
    :param read2:
    :param k:
    :return:
    >>> overlap('AAATTTT', 'TTTTCCC', 3)
    True
    >>> overlap('AAATTTT', 'TTTTCCC', 5)
    False
    >>> overlap('ATATATATAT', 'TATATATATA', 4)
    False
    >>> overlap('ATATATATAT', 'TATATATATA', 5)
    True

    '''
    final = False
    if read2[:k] == read1[-k:]:
        final = True
    return final

def maximalOverlap(read1, read2):
    '''

    :param read1:
    :param read2:
    :return:
    >>> maximalOverlap('AAATTTT', 'TTTTCCC')
    4
    >>> maximalOverlap('ATATATATAT', 'TATATATATA')
    9
    '''
    k = len(read1)
    while not overlap(read1, read2, k):
        k-=1
    return k


def overlapGraph(collection, k):
    '''

    :param collection:
    :param k:
    :return:
    >>> reads = ['AAATAAA', 'AAATTTT', 'TTTTCCC', 'AAATCCC', 'GGGTGGG']
    >>> overlapGraph(reads, 3)
    {'AAATTTT': {'TTTTCCC'}, 'AAATAAA': {'AAATTTT', 'AAATCCC'}}
    >>> overlapGraph(reads, 4)
    {'AAATTTT': {'TTTTCCC'}}

    >>> reads = ['GACCTACA', 'ACCTACAA', 'CCTACAAG', 'CTACAAGT', 'TACAAGTT', 'ACAAGTTA', 'CAAGTTAG', 'TACAAGTC', 'ACAAGTCC', 'CAAGTCCG']
    >>> overlapGraph(reads, 6)
    {'CTACAAGT': {'ACAAGTCC', 'ACAAGTTA', 'TACAAGTC', 'TACAAGTT'}, 'TACAAGTT': {'CAAGTTAG', 'ACAAGTTA'}, 'ACCTACAA': {'CTACAAGT', 'CCTACAAG'}, 'ACAAGTCC': {'CAAGTCCG'}, 'ACAAGTTA': {'CAAGTTAG'}, 'GACCTACA': {'CCTACAAG', 'ACCTACAA'}, 'TACAAGTC': {'ACAAGTCC', 'CAAGTCCG'}, 'CCTACAAG': {'CTACAAGT', 'TACAAGTC', 'TACAAGTT'}}

    >>> reads = ('CCTAGGCTG', 'CTGGGAGGAT', 'GCTGGGAGG', 'GCTGGGAG', 'AGGATGATAG', 'ATGATA', 'CCTAGGCTG', 'GGATGAT', 'TCCTAGGC', 'AGGATGATAG', 'AGGATGATAG', 'GCTGGGA', 'GGTAAAGCC', 'AGGCTGGGAG', 'TCCTAGG', 'TCCTAGGCTG', 'TGGGAGTA', 'CCTAGGC', 'TACTGAAG', 'ATTGTACC')
    >>> overlapGraph(reads, 4)
    {'AGGCTGGGAG': {'CTGGGAGGAT', 'GCTGGGAG', 'GCTGGGAGG', 'TGGGAGTA'}, 'CCTAGGC': {'CCTAGGCTG', 'AGGCTGGGAG'}, 'CCTAGGCTG': {'AGGCTGGGAG', 'GCTGGGA', 'GCTGGGAG', 'GCTGGGAGG'}, 'CTGGGAGGAT': {'AGGATGATAG', 'GGATGAT'}, 'GCTGGGA': {'CTGGGAGGAT', 'GCTGGGAG', 'GCTGGGAGG', 'TGGGAGTA'}, 'GCTGGGAG': {'CTGGGAGGAT', 'GCTGGGAGG', 'TGGGAGTA'}, 'GCTGGGAGG': {'CTGGGAGGAT'}, 'GGATGAT': {'ATGATA'}, 'TCCTAGG': {'CCTAGGC', 'CCTAGGCTG', 'TCCTAGGC', 'TCCTAGGCTG'}, 'TCCTAGGC': {'CCTAGGC', 'CCTAGGCTG', 'TCCTAGGCTG', 'AGGCTGGGAG'}, 'TCCTAGGCTG': {'AGGCTGGGAG', 'CCTAGGCTG', 'GCTGGGA', 'GCTGGGAG', 'GCTGGGAGG'}}
    '''
    d = {}
    tup = [(i,v) for i in collection for v in collection if v != i if maximalOverlap(i,v)>=int(k)]
    for i in tup:
        if i[0] not in d:
            d[i[0]]=set([i[1]])
        else:
            d[i[0]].update(set([i[1]]))
    return d