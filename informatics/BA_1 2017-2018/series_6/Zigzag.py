def isZigzag(seq):
    '''
    >>> isZigzag([10, 5, 6, 3, 2, 20, 100, 80])
    False
    >>> isZigzag((10, 5, 6, 2, 20, 3, 100, 80))
    True
    >>> isZigzag([20, 5, 10, 2, 80, 6, 100, 3])
    True
    '''
    total = len(seq)
    for i in range(total-1):
        n1 = seq[i]
        n2 = seq[i+1]
        if i%2 == 0:
            if n1 < n2:
                return False
        if i%2 != 0:
            if n1 > n2:
                return False
    else:
        return True

def zigzagSlow(seq):
    '''
    >>> seq = [10, 90, 49, 2, 1, 5, 23]
    >>> zigzagSlow(seq)
    >>> seq
    [2, 1, 10, 5, 49, 23, 90]
    '''
    newseq = []
    seq = seq.sort()
    length = len(seq)
    for i in range(length//2):
        i = i*2
        n1 = new1seq[i]
        n2 = new1seq[i+1]
        newseq.append(n2)
        newseq.append(n1)
    if length % 2 != 0:
        newseq.append(seq[-1])
