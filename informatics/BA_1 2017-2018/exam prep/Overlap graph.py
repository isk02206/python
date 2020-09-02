
def overlap(seq1,seq2,k):
    '''
    >>> overlap('AAATTTT', 'TTTTCCC', 3)
    True
    >>> overlap('AAATTTT', 'TTTTCCC', 5)
    False
    >>> overlap('ATATATATAT', 'TATATATATA', 4)
    False
    >>> overlap('ATATATATAT', 'TATATATATA', 5)
    True
    '''
    new_seq1 = seq1[-k:]
    new_seq2 = seq2[:k]
    for i in range(k):
        x = new_seq1[i]
        y = new_seq2[i]
        if x != y:
            return False
    else:
        return True

def maximalOverlap(seq1,seq2):
    '''
    >>> maximalOverlap('AAATTTT', 'TTTTCCC')
    4
    >>> maximalOverlap('ATATATATAT', 'TATATATATA')
    9
    '''
    if len(seq1)>=len(seq2):
        y = len(seq2)
    if len(seq1)<len(seq2):
        y = len(seq1)
    boo = []
    for k in range(y):
        a = overlap(seq1,seq2,k+1)
        if a == True:
            boo.append(1)
        if a == False:
            boo.append(0)
    boo = boo[::-1]
    boo_len = len(boo)
    count = -1
    for i in boo:
        count+=1
        if i == 1:
            break
    return boo_len-count

def overlapGraph(reads,k):
    '''
    >>> reads = ['AAATAAA', 'AAATTTT', 'TTTTCCC', 'AAATCCC', 'GGGTGGG']
    >>> overlapGraph(reads, 3)
    {'AAATTTT': {'TTTTCCC'}, 'AAATAAA': {'AAATTTT', 'AAATCCC'}}
    >>> overlapGraph(reads, 4)
    {'AAATTTT': {'TTTTCCC'}}

    >>> reads = ['GACCTACA', 'ACCTACAA', 'CCTACAAG', 'CTACAAGT', 'TACAAGTT', 'ACAAGTTA', 'CAAGTTAG', 'TACAAGTC', 'ACAAGTCC', 'CAAGTCCG']
    >>> overlapGraph(reads, 6)
    {'CTACAAGT': {'ACAAGTCC', 'ACAAGTTA', 'TACAAGTC', 'TACAAGTT'}, 'TACAAGTT': {'CAAGTTAG', 'ACAAGTTA'}, 'ACCTACAA': {'CTACAAGT', 'CCTACAAG'}, 'ACAAGTCC': {'CAAGTCCG'}, 'ACAAGTTA': {'CAAGTTAG'}, 'GACCTACA': {'CCTACAAG', 'ACCTACAA'}, 'TACAAGTC': {'ACAAGTCC', 'CAAGTCCG'}, 'CCTACAAG': {'CTACAAGT', 'TACAAGTC', 'TACAAGTT'}}
    '''
    graph = {}
    for i in reads:
        read = reads
        read.remove(i)
        for j in read:
            x = overlap(i,j,k)
            if x == True and :


    return graph
