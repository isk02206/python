def transition(code1,code2):
    '''
    >>> transition('G', 'A')
    True
    >>> transition('t', 'g')
    False
    >>> transition('C', 'c')
    False
    '''
    code1 = code1.lower()
    code2 = code2.lower()

    if code1 == 'a':
        if code2 == 'g':
            return True
        else:
            return False
    if code1 == 'g':
        if code2 == 'a':
            return True
        else:
            return False
    if code1 == 'c':
        if code2 == 't':
            return True
        else:
            return False
    if code1 == 't':
        if code2 == 'c':
            return True
        else:
            return False

def transversion(code1,code2):
    '''
    >>> transversion('G', 'A')
    False
    >>> transversion('t', 'g')
    True
    >>> transversion('C', 'c')
    False
    '''
    code1 = code1.lower()
    code2 = code2.lower()

    if code1 == 't':
        if code2 == 'a':
            return True
        if code2 == 'g':
            return True
        else:
            return False
    if code1 == 'a':
        if code2 == 't':
            return True
        if code2 == 'c':
            return True
        else:
            return False
    if code1 == 'c':
        if code2 == 'a':
            return True
        if code2 == 'g':
            return True
        else:
            return False
    if code1 == 'g':
        if code2 == 't':
            return True
        if code2 == 'c':
            return True
        else:
            return False

def ratio(seq1,seq2):
    '''
    >>> ratio('ATTAGCATTATCATC', 'AAATAGGATATATGG')
    0.2222222222222222
    '''
    s1 = 0
    s2 = 0
    for i in range(len(seq1)):
        a = seq1[i]
        b = seq2[i]
        if transition(a,b) == True:
            s1 += 1
        if transversion(a,b) == True:
            s2 += 1
    if s2 == 0 or s1 == 0:
        return 0.0
    else:
        return s1/s2

