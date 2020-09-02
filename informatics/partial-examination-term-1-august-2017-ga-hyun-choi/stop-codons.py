def isStopCodon(dna):
    '''
    indicate if the given sequence is stop codon or not
    :param dna:
    :return: bool
    >>> isStopCodon('TAA')
    True
    >>> isStopCodon('tag')
    True
    >>> isStopCodon('ATC')
    False
    '''
    # stop codon = TAG, TGA, TAA
    dna = str(dna)
    if dna.upper() in ['TAG', 'TGA', 'TAA']:
        return True
    else:
        return False


def reverseComplement(dna):
    '''
    retrun reverse complement of given DNA sequence in uppercase letters
    :param dna:
    :return:
    >>> reverseComplement('AAGTC')
    'GACTT'
    >>> reverseComplement('agcttcgt')
    'ACGAAGCT'
    >>> reverseComplement('AGTCTTACGCTTA')
    'TAAGCGTAAGACT'
    '''
    dna = reversed(list(dna.upper()))
    final = ''
    for i in dna:
        if i == 'A':
            i = 'T'
        elif i == 'G':
            i = 'C'
        elif i == 'C':
            i = 'G'
        else:
            i = 'A'
        final += i
    return final


def stopCodons(sequence, n):
    '''
    return number of stop codons in the given reading frame of the DNA sequence
    :param sequence:
    :param n:
    :return:
    >>> seq = 'TTTACTATAGTGATAGCCGGTAACATAGCTCCTAGAATAAAGGCAACGCAATACCCCTAGG'
    >>> stopCodons(seq, +1)
    1
    >>> stopCodons(seq, +2)
    5
    >>> stopCodons(seq, +3)
    2
    >>> stopCodons(seq, -1)
    3
    >>> stopCodons(seq, -2)
    0
    >>> stopCodons(seq, -3)
    1
    '''
    if n < 0:
        sequence = reverseComplement(sequence)
    sequence = sequence[abs(n)-1:]
    count = 0
    while True:
        if len(sequence) < 3:
            break
        current = sequence[:3]
        if isStopCodon(current):
            count += 1
        sequence = sequence[3:]
    return count


def codons(sequence, n):
    '''
    return string representation of splitting in codon
    :param sequence:
    :param n:
    :return:
    >>> seq = 'TTTACTATAGTGATAGCCGGTAACATAGCTCCTAGAATAAAGGCAACGCAATACCCCTAGG'
    >>> codons(seq, +1)
    'TTT-ACT-ATA-GTG-ATA-GCC-GGT-AAC-ATA-GCT-CCT-AGA-ATA-AAG-GCA-ACG-CAA-TAC-CCC-TAG-G'
    >>> codons(seq, +2)
    'T-TTA-CTA-TAG-TGA-TAG-CCG-GTA-ACA-TAG-CTC-CTA-GAA-TAA-AGG-CAA-CGC-AAT-ACC-CCT-AGG'
    >>> codons(seq, +3)
    'TT-TAC-TAT-AGT-GAT-AGC-CGG-TAA-CAT-AGC-TCC-TAG-AAT-AAA-GGC-AAC-GCA-ATA-CCC-CTA-GG'
    >>> codons(seq, -1)
    'CCT-AGG-GGT-ATT-GCG-TTG-CCT-TTA-TTC-TAG-GAG-CTA-TGT-TAC-CGG-CTA-TCA-CTA-TAG-TAA-A'
    >>> codons(seq, -2)
    'C-CTA-GGG-GTA-TTG-CGT-TGC-CTT-TAT-TCT-AGG-AGC-TAT-GTT-ACC-GGC-TAT-CAC-TAT-AGT-AAA'
    >>> codons(seq, -3)
    'CC-TAG-GGG-TAT-TGC-GTT-GCC-TTT-ATT-CTA-GGA-GCT-ATG-TTA-CCG-GCT-ATC-ACT-ATA-GTA-AA'
    '''
    if n < 0:
        sequence = reverseComplement(sequence)
    if sequence[:abs(n)-1]:
        l_sequence = [sequence[:abs(n)-1]]
    else:
        l_sequence = []
    sequence = sequence[abs(n)-1:]
    while True:
        if len(sequence) < 3:
            if sequence:
                l_sequence.append(sequence)
            break
        l_sequence.append(sequence[:3])
        sequence = sequence[3:]
    final = '-'.join(l_sequence)
    return final


if __name__ == "__main__":
    import doctest
    doctest.testmod()