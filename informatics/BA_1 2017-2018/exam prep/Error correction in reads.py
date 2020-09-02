def hamming(codon1, codon2):
    '''
    >>> hamming('TTCAT', 'TTCAT')
    0
    >>> hamming('TTCAT', 'TTGAT')
    1
    >>> hamming('TTCAT', 'GAGGA')
    5
    >>> hamming('TTCAT', 'TTT')
    Traceback (most recent call last):
    AssertionError: strings should have equal length
    '''
    count = 0
    if len(codon1) == len(codon2):
        for i in range(len(codon1)):
           if codon1[i] != codon2[i]:
                count += 1
        return count
    raise AssertionError('strings should have equal length')
def complement(codon):
    '''
    >>> complement('TTCAT')
    'ATGAA'
    >>> complement('TTGAT')
    'ATCAA'
    >>> complement('GAGGA')
    'TCCTC'
    '''
    complementList = []
    reverse = codon[::-1]
    for code in reverse:
        if code == 'A':
            complementList.append('T')
        if code == 'G':
            complementList.append('C')
        if code == 'T':
            complementList.append('A')
        if code == 'C':
            complementList.append('G')
    return ''.join(complementList)

def normalform(codon):
    '''
    >>> normalform('TTCAT')
    'ATGAA'
    >>> normalform('TTGAT')
    'ATCAA'
    >>> normalform('GAGGA')
    'GAGGA'
    '''
    if sorted(codon) == codon:
        return complement(codon)
    else:
        return codon

def occurrences(reads):
    '''
    >>> reads = ['TCATC', 'TTCAT', 'TCATC', 'TGAAA', 'GAGGA', 'TTTCA', 'ATCAA', 'TTGAT', 'AGGCT']
    >>> occurrences(reads)
    {'GAGGA': 1, 'ATGAA': 1, 'TGAAA': 2, 'GATGA': 2, 'AGCCT': 1, 'ATCAA': 2}
    >>> reads = ['GATTA', 'GATTA', 'TAATC', 'GAATC', 'GATTA', 'TAAGC', 'TAATA']
    >>> occurrences(reads)
    {'GATTA': 4, 'TAATA': 1, 'GCTTA': 1, 'GAATC': 1}
    '''

def errors(reads):
    '''
    >>> reads = ['TCATC', 'TTCAT', 'TCATC', 'TGAAA', 'GAGGA', 'TTTCA', 'ATCAA', 'TTGAT', 'AGGCT']
    >>> errors(reads)
    ({'AGGCT'}, [('GAGGA', 'GATGA'), ('TTCAT', 'TTGAT')])
    >>> reads = ['GATTA', 'GATTA', 'TAATC', 'GAATC', 'GATTA', 'TAAGC', 'TAATA']
    >>> errors(reads)
    (set(), [('GAATC', 'TAATC'), ('TAAGC', 'TAATC'), ('TAATA', 'TAATC')])
    '''