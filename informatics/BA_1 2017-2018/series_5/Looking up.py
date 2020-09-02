def swap(x):
    '''
    >>> swap('FBFFFBFFBF')
    'BFBBBFBBFB'
    >>> swap('BFFBFBFFFBFBBBFBBBBFF')
    'FBBFBFBBBFBFFFBFFFFBB'
    >>> swap('FFBFBFBFBFBFBFBBFBFBFBFBBFBFBBFBF')
    'BBFBFBFBFBFBFBFFBFBFBFBFFBFBFFBFB'
    '''
    swap = []
    for i in x:
        if i == 'B':
            swap.append('F')
        if i == 'F':
            swap.append('B')
    return ''.join(swap)

def next(code):
    '''
    >>> next('FBFFFBFFBF')
    'FFBBBFBBFF'
    >>> next('BFFBFBFFFBFBBBFBBBBFF')
    'FBBFBFBBBFBFFFBFFFFFF'
    >>> next('FFBFBFBFBFBFBFBBFBFBFBFBBFBFBBFBF')
    'FFFBFBFBFBFBFBFFBFBFBFBFFBFBFFBFF'
    '''
    code1 = ''
    code2 = ''
    n = 0
    m = 0
    code_reverse = code[::-1]
    if code.find('B') == -1:
        code1 = code
    else:
        for i in range(0,len(code)):
            if code[i] == 'F':
                code1+='F'
                n += 1
            if code[i] == 'B':
                break
        for j in range(0,len(code)):
            if code_reverse[j] == 'F':
                code2 += 'F'
                m += 1
            if code_reverse[j] == 'B':
                break
        for k in range(n,len(code)-m):
            if code[k] == 'F':
                code1 += 'B'
            if code[k] == 'B':
                code1 += 'F'
        code1 += code2
    return code1

def turns(code):
    '''
    >>> turns('FBFFFBFFBF')
    3
    >>> turns('BFFBFBFFFBFBBBFBBBBFF')
    6
    >>> turns('FFBFBFBFBFBFBFBBFBFBFBFBBFBFBBFBF')
    14
    '''




