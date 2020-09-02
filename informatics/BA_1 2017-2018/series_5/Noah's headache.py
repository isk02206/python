def split(x):
    '''
    >>> split('scheep')
    ('sch', 'eep')
    >>> split('goat')
    ('g', 'oat')
    '''
    b = x.lower()
    prefix = []
    suffix = []
    vowel = ['a','e','i','o','u']
    for i in range(len(x)):
        a = b[i]
        for j in vowel:
            if a == j:
                prefix.append(x[:i])
                suffix.append(x[i:])
                return ''.join(prefix), ''.join(suffix)
                break

def hybridize(x, y):
    '''
    >>> hybridize('goat', 'sheep')
    ('geep', 'shoat')
    >>> hybridize('jaguar', 'leopard')
    ('jeopard', 'laguar')
    >>> hybridize('zebra', 'horse')
    ('zorse', 'hebra')
    '''
    a = split(x)
    b = split(y)
    a1 = a[0]
    a2 = a[1]
    b1 = b[0]
    b2 = b[1]
    return a1+b2, b1+a2


