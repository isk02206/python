def transition(nucleotide_1, nucleotide_2):
    if nucleotide_1.lower() == 'a':
        type = 'g'
    if nucleotide_1.lower() == 'g':
        type = 'a'
    if nucleotide_1.lower() == 'c':
        type = 't'
    if nucleotide_1.lower() == 't':
        type = 'c'
    if type == nucleotide_2.lower():
        return True
    else:
        return False
print(transition('G', 'A'))
print(transition('t', 'g'))
print(transition('C', 'c'))

def transversion(nucleotide_1, nucleotide_2):
    if nucleotide_2.lower() in ['c','t']:
        type = ['a', 'g']
    if nucleotide_2.lower() in ['a', 'g']:
        type = ['c', 't']
    if nucleotide_1.lower() in type:
        return True
    else:
        return False


print(transversion('G', 'A'))
print(transversion('t', 'g'))
print(transversion('C', 'c'))

def ratio(seq_1, seq_2):
    transition_count = 0
    transversion_count = 0
    for i in range(len(seq_1)):
        if transition(seq_1[i].lower(), seq_2[i].lower()) == True:
            transition_count += 1
        if transversion(seq_1[i].lower(), seq_2[i].lower()) == True:
            transversion_count += 1
    if transversion_count == 0:
        return 0.0
    return transition_count / transversion_count
print(ratio('ATTAGCATTATCATC', 'AAATAGGATATATGG'))
print(ratio('GCAACGCACAACGAAAACCCTTAGGGACTGGATTATTTCGTGATCGTTGTAGTTATTGGAAGTACGGGCATCAACCCAGTT', 'ttatctgacaaagaaagccgtcaacggctggataatttcgcgatcgtgctggttactggcggtacgagtgttcctttgggt'))
print(ratio('TTAACCCTAAGAGATGGACAATTCAATGCGCCGTAAG', 'TTAACCCTAAGAGATGGACAATTCAATGCGCCGTAAG'))



