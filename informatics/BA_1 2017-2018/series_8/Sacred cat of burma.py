def color(gene):
    '''
    >>> color('CcDd')
    'seal'
    >>> color('ccdd')
    'lilac'
    '''
    c_dict = {'CC':'9','Cc':'6','cC':'6','cc':'0'}
    d_dict = {'DD':'9','Dd':'6','dD':'6','dd':'0'}
    c_gene = gene[:2]
    d_gene = gene[2:]
    a = c_dict[c_gene]
    b = d_dict[d_gene]
    if a+b == '99' or a+b == '96' or a+b == '69'or a+b == '66':
        return 'seal'
    if a+b == '09' or a+b == '06':
        return 'chocolate'
    if a+b == '90' or a+b == '60':
        return 'blue'
    if a+b == '00':
        return 'lilac'

def combinations(gene):
    '''
    >>> combinations('CcDd')
    ['CD', 'Cd', 'cD', 'cd']
    >>> combinations('ccdd')
    ['cd', 'cd', 'cd', 'cd']
    '''
    a = gene[0]+gene[2]
    b = gene[0]+gene[3]
    c = gene[1]+gene[2]
    d = gene[1]+gene[3]
    genotype = [a,b,c,d]
    return genotype

def punnett(gene1,gene2,pprint=None):
    '''
    >>> print(punnett('CcDd', 'CcDd'))
    [['CCDD', 'CCDd', 'CcDD', 'CcDd'], ['CCdD', 'CCdd', 'CcdD', 'Ccdd'], ['cCDD', 'cCDd', 'ccDD', 'ccDd'], ['cCdD', 'cCdd', 'ccdD', 'ccdd']]
    >>> print(punnett('CcDd', 'CcDd', pprint=True))
    CCDD CCDd CcDD CcDd
    CCdD CCdd CcdD Ccdd
    cCDD cCDd ccDD ccDd
    cCdD cCdd ccdD ccdd
    >>> print(punnett('cCDd', 'CcdD', pprint=True))
    cCDd cCDD ccDd ccDD
    cCdd cCdD ccdd ccdD
    CCDd CCDD CcDd CcDD
    CCdd CCdD Ccdd CcdD
    '''
    genotype1 = combinations(gene1)
    genotype2 = combinations(gene2)
    total = []
    if pprint == None or pprint == False:
        for i in genotype1:
            col = []
            for j in genotype2:
                a = i[0]+j[0]+i[1]+j[1]
                col.append(a)
            total.append(col)
        return total
    if pprint == True:
        total = ''
        for i in genotype1:
            col = ''
            for j in genotype2:
                a = i[0]+j[0]+i[1]+j[1]
                col += a+' '
            x = col.rstrip() + '\n'
            total += x
        return total.rstrip()

def colorDistribution(gene1,gene2):
    '''
    >>> colorDistribution('CcDd', 'CcDd')
    {'blue': 3, 'seal': 9, 'lilac': 1, 'chocolate': 3}
    >>> colorDistribution('cCDD', 'cCDD')
    {'seal': 12, 'chocolate': 4}
    >>> colorDistribution('ccDD', 'ccDD')
    {'chocolate': 16}
    >>> colorDistribution('ccdd', 'CcDd')
    {'blue': 4, 'lilac': 4, 'seal': 4, 'chocolate': 4}
    '''
    identified = {}
    a = punnett(gene1,gene2)
    for i in a:
        for j in i:
            x = color(j)
            if x in identified:
                identified[x] += 1
            if x not in identified:
                identified[x] = 1
    return identified