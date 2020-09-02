def transition(n1, n2):
    '''
    return bool that indicate transition
    :param n1:
    :param n2:
    :return:
    >>> transition('G', 'A')
    True
    >>> transition('t', 'g')
    False
    >>> transition('C', 'c')
    False
    '''
    n1, n2 = n1.upper(), n2.upper()
    if n1 == 'A' and n2 == 'G' or n1 == 'G' and n2 == 'A' or n1 == 'C' and n2 == 'T' or n1 == 'T' and n2 == 'C':
        return True
    else:
        return False


def transversion(n1, n2):
    '''

    :param n1:
    :param n2:
    :return:
    >>> transversion('G', 'A')
    False
    >>> transversion('t', 'g')
    True
    >>> transversion('C', 'c')
    False
    '''
    if not transition(n1, n2) and n1.upper() != n2.upper():
        return True
    else:
        return False


def ratio(s1, s2):
    '''

    :param s1:
    :param s2:
    :return:
    >>> ratio('ATTAGCATTATCATC', 'AAATAGGATATATGG')
    0.2222222222222222

    >>> seq1 = 'GCAACGCACAACGAAAACCCTTAGGGACTGGATTATTTCGTGATCGTTGTAGTTATTGGAAGTACGGGCATCAACCCAGTT'
    >>> seq2 = 'ttatctgacaaagaaagccgtcaacggctggataatttcgcgatcgtgctggttactggcggtacgagtgttcctttgggt'
    >>> ratio(seq1, seq2)
    1.2142857142857142
    '''
    transi, transv = 0, 0
    for i in range(len(s1)):
        if transition(s1[i], s2[i]):
            transi += 1
        if transversion(s1[i], s2[i]):
            transv += 1
    if transv:
        final = transi/transv
    else:
        final = 0.0
    return final

if __name__ == "__main__":
    import doctest
    doctest.testmod()
