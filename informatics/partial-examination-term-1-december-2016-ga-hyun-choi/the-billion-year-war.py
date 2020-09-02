def reverseComplement(sequence):
    if isinstance(sequence, str):
        final = ''
        for i in range(len(sequence)-1, 0-1, -1):
            if sequence[i] == 'A':
                final += 'T'
            elif sequence[i] == 'T':
                final += 'A'
            elif sequence[i] == 'G':
                final += 'C'
            else:
                final += 'G'
        return final


def reversePalindrome(sequence):
    sequence1 = sequence[:int(len(sequence)/2)]
    final = sequence1+reverseComplement(sequence1)
    if sequence == reverseComplement(final):
        return True
    else:
        return False


def restrictionSites(sequence, minLength=4, maxLength=12):
    final = []

    if minLength % 2 == 0:
        hmin = int(minLength/2)
    else:
        hmin = int((minLength+1)/2)
    if maxLength % 2 == 0:
        hmax = int(maxLength/2)
    else:
        hmax = int((maxLength-1)/2)
    for i in range(len(sequence)):
        for n in range(hmin, hmax+1):
            seq = sequence[i:i+n]+reverseComplement(sequence[i:i+n])
            if seq == sequence[i:i+2*n]:
                final.append((i+1, seq))
    return list(final)
