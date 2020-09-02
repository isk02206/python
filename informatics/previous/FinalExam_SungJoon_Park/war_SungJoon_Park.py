def reverseComplement(x):
    '''
    >>> reverseComplement('GATATC')
    'GATATC'
    >>> reverseComplement('GCATGC')
    'GCATGC'
    >>> reverseComplement('AGCTTC')
    'GAAGCT'
    '''
    reverse = []
    for i in x:
        if i == 'A':
            reverse.append('T')
        if i == 'T':
            reverse.append('A')
        if i == 'G':
            reverse.append('C')
        if i == 'C':
            reverse.append('G')
    return ''.join(reverse)

def reversePalindrome(x):
    '''
    >>> reversePalindrome('GATATC')
    True
    >>> reversePalindrome('GCATGC')
    True
    >>> reversePalindrome('AGCTTC')
    False
    '''
    front = x[:3]
    back = x[3:]
    reverseback = reverseComplement(back)
    if front == reverseback[::-1]:
        return True
    else:
        return False
    
def restrictionSites(x):
    site = []
    for i in range(len(x)):
        for j in range()