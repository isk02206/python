def color(genotype):
    '''

    :param genotype:
    :return:
    >>> color('CcDd')
    'seal'
    >>> color('ccdd')
    'lilac'
    '''
    if 'dd'in genotype:
        if 'cc' in genotype:
            final = 'lilac'
        else:
            final = 'blue'
    else:
        if 'cc' in genotype:
            final = 'chocolate'
        else:
            final = 'seal'
    return final

def combinations(genotype):
    '''

    :param genotype:
    :return:
    >>> combinations('CcDd')
    ['CD', 'Cd', 'cD', 'cd']
    >>> combinations('ccdd')
    ['cd', 'cd', 'cd', 'cd']
    '''
    cp,cm,dp,dm = genotype
    return [cp+dp, cp+dm, cm+dp, cm+dm]


def punnett(gene_m, gene_f, pprint=False):
    '''

    :param gene_m:
    :param gene_f:
    :param pprint:
    :return:
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
    com_m = combinations(gene_m)
    com_f = combinations(gene_f)
    c, final,line = 0, [], []
    for row in com_m:
        for col in com_f:
            line.append(row[0]+col[0]+row[1]+col[1])
        final.append(line)
        line = []

    if pprint:
        string = ''
        for i in final:
            string+=' '.join(i)+'\n'
        return string.strip()
    else:
        return final

def colorDistribution(m_gene, f_gene):
    '''

    :param m_gene:
    :param f_gene:
    :return:
    >>> colorDistribution('CcDd', 'CcDd')
    {'blue': 3, 'seal': 9, 'lilac': 1, 'chocolate': 3}
    >>> colorDistribution('cCDD', 'cCDD')
    {'seal': 12, 'chocolate': 4}
    >>> colorDistribution('ccDD', 'ccDD')
    {'chocolate': 16}
    >>> colorDistribution('ccdd', 'CcDd')
    {'blue': 4, 'lilac': 4, 'seal': 4, 'chocolate': 4}
    '''
    genelist = punnett(m_gene, f_gene)
    d={}
    for i in genelist:
        for k in i:
            if color(k) in d:
                d[color(k)]+=1
            else:
                d[color(k)] =1
    return d