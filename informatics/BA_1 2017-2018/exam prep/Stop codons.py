def isStopCodon(codon):
    '''
    >>> isStopCodon('TAA')
    True
    >>> isStopCodon('tag')
    True
    >>> isStopCodon('ATC')
    False
    '''
    codon = codon.lower()
    if codon == 'tag' or codon == 'tga' or codon == 'taa':
        return True
    else:
        return False

def reverseComplement(codon):
    '''
    >>> reverseComplement('AAGTC')
    'GACTT'
    >>> reverseComplement('agcttcgt')
    'ACGAAGCT'
    >>> reverseComplement('AGTCTTACGCTTA')
    'TAAGCGTAAGACT'
    '''
    reverseComplement = []
    reverseCodon = codon[::-1]
    for code in reverseCodon:
        if code == 'a' or code == 'A':
            reverseComplement.append('T')
        if code == 'g' or code == 'G':
            reverseComplement.append('C')
        if code == 't' or code == 'T':
            reverseComplement.append('A')
        if code == 'c' or code == 'C':
            reverseComplement.append('G')
    return ''.join(reverseComplement)


def stopCodons(seq, number):
    '''
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
    if number < 0:
        seq = reverseComplement(seq)
        number = abs(number)

    a = number-1
    b = -((len(seq)-(number-1))%3)
    if b == 0:
        b = len(seq)+1
    sequence = seq[a:b]
    count = 0
    for i in range(len(sequence)//3):
        code = sequence[i*3:(i+1)*3]
        if isStopCodon(code) == True:
            count += 1
    return count

def codons(seq, number):
    '''
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
    codon = []
    count = 0

    if number < 0:
        seq = reverseComplement(seq)
        number = abs(number)

    if number == 1:
        count = 0
    if number == 2:
        count = 2
    if number == 3:
        count = 1

    for i in range(len(seq)):
        codon.append(seq[i])
        count +=1
        if count == 3 and i != (len(seq)-1):
            count = 0
            codon.append('-')

    return ''.join(codon)