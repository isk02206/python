'''
Created on 2015. 12. 2.

@author: USER
'''
def overlap(first, second, k):
    """
    >>> overlap(�섲AATTTT��, �셏TTTCCC��, 3)
    True
    >>> overlap(�섲AATTTT��, �셏TTTCCC��, 5)
    False
    >>> overlap(�섲TATATATAT��, �셏ATATATATA��, 4)
    False
    >>> overlap(�섲TATATATAT��, �셏ATATATATA��, 5)
    True
    """
    assert 0 < k <= min(len(first), len(second)), 'invalid arguments'
    # check if the first read ends in the same k bases that are found at the
    # start of the second read
    return first != second and first[-k:] == second[:k]

def maximalOverlap(first, second):
    """
    >>> maximalOverlap(�섲AATTTT��, �셏TTTCCC��)
    4
    >>> maximalOverlap(�섲TATATATAT��, �셏ATATATATA��)
    9
    """
    # find first overlap, starting with the longest possible overlap
    for k in range(min(len(first), len(second)), 0, -1):
        if overlap(first, second, k):
            return k
    # no overlap found
    return 0

def overlapGraph(reads, k):
    """
    >>> reads = [�섲AATAAA��, �섲AATTTT��, �셏TTTCCC��, �섲AATCCC��, �섻GGTGGG��]
    >>> overlapGraph(reads, 3)
    {�섲AATTTT��: {�셏TTTCCC��}, �섲AATAAA��: {�섲AATTTT��, �섲AATCCC��}}
    >>> overlapGraph(reads, 4)
    {�섲AATTTT��: {�셏TTTCCC��}}
    >>> reads = [�섻ACCTACA��, �섲CCTACAA��, �섴CTACAAG��, �섴TACAAGT��, �셏ACAAGTT��, �섲CAAGTTA��, ��
    CAAGTTAG��, �셏ACAAGTC��, �섲CAAGTCC��, �섴AAGTCCG��]
    >>> overlapGraph(reads, 6)
    {�섴TACAAGT��: {�섲CAAGTCC��, �섲CAAGTTA��, �셏ACAAGTC��, �셏ACAAGTT��}, �셏ACAAGTT��: {�섴AAGTTAG��, ��
    ACAAGTTA��}, �섲CCTACAA��: {�섴TACAAGT��, �섴CTACAAG��}, �섲CAAGTCC��: {�섴AAGTCCG��}, �섲CAAGTTA
    ��: {�섴AAGTTAG��}, �섻ACCTACA��: {�섴CTACAAG��, �섲CCTACAA��}, �셏ACAAGTC��: {�섲CAAGTCC��, ��
    CAAGTCCG��}, �섴CTACAAG��: {�섴TACAAGT��, �셏ACAAGTC��, �셏ACAAGTT��}}
    """
    # construct overlap graph by determining the maximal overlap between any
    # pair of different reads
    graph = {}
    for first in reads:
        for second in reads:
            if maximalOverlap(first, second) >= k:
                if first not in graph:
                    graph[first] = {second}
                else:
                    graph[first].add(second)
    # return the constructed overlap graph
    return graph