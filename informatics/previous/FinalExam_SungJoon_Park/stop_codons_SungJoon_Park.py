'''
name : Sung Joon Park
student number : 01514170
'''

def isStopCodon(codon):
    '''
    >>>isStopCodon('TAA')
    True
    >>>isStopCodon('tag')
    True
    >>>isStopCodon('ATC')
    False
    '''
    codon = codon.lower() #lowercased codons available
    
    if codon == 'tag' or codon =='tga' or codon =='taa': #identifying stop codons
        return True
    else: #other codon
        return False

def reverseComplement(sequence):
    '''
    >>>reverseComplement('AAGTC')
    'GACTT'
    >>>reverseComplement('agcttcgt')
    'ACGAAGCT'
    >>>reverseComplement('AGTCTTACGCTTA')
    'TAAGCGTAAGACT'
    '''
    sequence = sequence.lower() #lowercased codons available
    reverse = []
    for dna in sequence: #changing into pairs
        if dna == 'a':
            reverse.append('T')
        if dna == 't':
            reverse.append('A')
        if dna == 'g':
            reverse.append('C')
        if dna == 'c':
            reverse.append('G')
    complement = ''.join(reverse) #changiing from list form
    reverseComplement = complement[::-1] #reversing the sequence
    return reverseComplement

def stopCodons(seq,frame):
    '''
    >>>seq = 'TTTACTATAGTGATAGCCGGTAACATAGCTCCTAGAATAAAGGCAACGCAATACCCCTAGG'
    >>>stopCodons(seq,+1)
    1
    >>>stopCodons(seq,+2)
    5
    >>>stopCodons(seq,+3)
    2
    >>>stopCodons(seq,-1)
    3
    >>>stopCodons(seq,-2)
    0
    >>>stopCodons(seq,-3)
    1
    '''
    read = len(seq)//3
    count = 0
    for i in range(read):
        if frame == +1:
            seq = seq[:-1] #cutting frame
            codon = []
            n = i-1
            a= seq[n:n+2]
            codon.append(a) #making the long codon easy to identify stop codon
            if isStopCodon(codon) == True: #identifying whether if the codon is a stop codon
                count = count + 1
        if frame == +2:
            seq = seq[1:]
            codon = []
            n = i-1
            a= seq[n:n+2]
            codon.append(a)
            if isStopCodon(codon) == True:
                count = count + 1
        if frame == +3:
            seq = seq[2:-2]
            codon = []
            n = i-1
            a= seq[n:n+2]
            codon.append(a)
            if isStopCodon(codon) == True:
                count = count + 1
        if frame == -1:
            seq = reverseComplement(seq) #making into reverse complment form
            seq = seq[:-1]
            codon = []
            n = i-1
            a= seq[n:n+2]
            codon.append(a)
            if isStopCodon(codon) == True:
                count = count + 1
        if frame == -2:
            seq = reverseComplement(seq)
            seq = seq[1:]
            codon = []
            n = i-1
            a= seq[n:n+2]
            codon.append(a)
            if isStopCodon(codon) == True:
                count = count + 1
        if frame == -3:
            seq = reverseComplement(seq)
            seq = seq[2:-2]
            codon = []
            n = i-1
            a= seq[n:n+2]
            codon.append(a)
            if isStopCodon(codon) == True:
                count = count + 1
    return count

def codons(seq, frame):
    '''
    >>>codons(seq, frame)
    'TTT-ACT-ATA-GTG-ATA-GCC-GGT-AAC-ATA-GCT-CCT-AGA-ATA-AAG-GCA-ACG-CAA-TAC-CCC-TAG-G'
    >>>codons(seq, frame)
    'T-TTA-CTA-TAG-TGA-TAG-CCG-GTA-ACA-TAG-CTC-CTA-GAA-TAA-AGG-CAA-CGC-AAT-ACC-CCT-AGG'
    >>>codons(seq, frame)
    'TT-TAC-TAT-AGT-GAT-AGC-CGG-TAA-CAT-AGC-TCC-TAG-AAT-AAA-GGC-AAC-GCA-ATA-CCC-CTA-GG'
    >>>codons(seq, frame)
    'CCT-AGG-GGT-ATT-GCG-TTG-CCT-TTA-TTC-TAG-GAG-CTA-TGT-TAC-CGG-CTA-TCA-CTA-TAG-TAA-A'
    >>>codons(seq, frame)
    'C-CTA-GGG-GTA-TTG-CGT-TGC-CTT-TAT-TCT-AGG-AGC-TAT-GTT-ACC-GGC-TAT-CAC-TAT-AGT-AAA'
    >>>codons(seq, frame)
    'CC-TAG-GGG-TAT-TGC-GTT-GCC-TTT-ATT-CTA-GGA-GCT-ATG-TTA-CCG-GCT-ATC-ACT-ATA-GTA-AA'
    '''
    
    seq_list = []
    if frame == +1:
        for i in range(len(seq-1)):
            if (i+1) % 3 == 0: #stopping every third codon to put a dash
                seq_list.append(seq[i])
                seq_list.append('-') #adding dashes codons
            else:
                seq_list.append(seq[i])
        return ''.join(seq_list)+'-'+seq[-1] #returning the value adding the framed codons
    
    if frame == +2:
        for i in range(len(seq-1)):
            if (i+1) % 3 == 0:
                seq_list.append(seq[i+1])
                seq_list.append('-')
            else:
                seq_list.append(seq[i+1])
        return seq[0]+'-'+''.join(seq_list)
    if frame == +3:
        for i in range(len(seq-4)):
            if (i+1) % 3 == 0:
                seq_list.append(seq[i+1])
                seq_list.append('-')
            else:
                seq_list.append(seq[i+1])
        return seq[0:1]+'-'+''.join(seq_list)+'-'+seq[-2:-1]
    if frame == -1:
        for i in range(len(seq-1)):
            seq = reverseComplement(seq) #reverse complementing the negative frame
            if (i+1) % 3 == 0:
                seq_list.append(seq[i])
                seq_list.append('-')
            else:
                seq_list.append(seq[i])
        return ''.join(seq_list)+'-'+seq[-1]
    
    if frame == -2:
        for i in range(len(seq-1)):
            seq = reverseComplement(seq)
            if (i+1) % 3 == 0:
                seq_list.append(seq[i+1])
                seq_list.append('-')
            else:
                seq_list.append(seq[i+1])
        return seq[0]+'-'+''.join(seq_list)
    if frame == -3:
        for i in range(len(seq-4)):
            seq = reverseComplement(seq)
            if (i+1) % 3 == 0:
                seq_list.append(seq[i+1])
                seq_list.append('-')
            else:
                seq_list.append(seq[i+1])
        return seq[0:1]+'-'+''.join(seq_list)+'-'+seq[-2:-1]

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    