'''
name : Ha Young Kim
student number : 01603259
'''

def color(A):
    """
    >>> color('CcDd')
    'seal'
    >>> color('ccdd')
    'lilac'
    """
    
    #C-gene of the combinations of a C- and D-gene
    first = A[0]+A[1]
    #D-gene of the combinations of a C- and D-gene
    second = A[2]+A[3]
    
    #set the class of each alleles
    if first == 'CC':
        first = 'up'
    elif first == 'Cc':
        first = 'mid'
    elif first == 'cC':
        first = 'mid'
    elif first == 'cc':
        first = 'low'
    
    #set the class of each alleles
    if second == 'DD':
        second = 'up'
    elif second == 'Dd':
        second = 'mid'
    elif second == 'dD':
        second = 'mid'
    elif second == 'dd':
        second = 'low'
    
    #each genotypes are determined by the combinations of each classes of alleles
    if first == 'low' and second == 'low':
        return 'lilac'
    elif first == 'low':
        return 'chocolate'
    elif second == 'low':
        return 'blue'
    else:
        return 'seal'

def combinations(B):
    """
    >>> combinations('CcDd')
    ['CD', 'Cd', 'cD', 'cd']
    >>> combinations('ccdd')
    ['cd', 'cd', 'cd', 'cd']
    """
    
    list_c = []
    #the function must return the four possible combinations of C- and D-alleles that the Birman may pass on to its offspring, listed in the genetic order
    #those are the genetic orders
    list_c.append(B[0]+B[2])
    list_c.append(B[0]+B[3])
    list_c.append(B[1]+B[2])
    list_c.append(B[1]+B[3])
    return list_c

def punnett(C1,C2,pprint=False):
    """
    >>> punnett('CcDd', 'CcDd')
    [['CCDD', 'CCDd', 'CcDD', 'CcDd'], ['CCdD', 'CCdd', 'CcdD', 'Ccdd'], ['cCDD', 'cCDd', 'ccDD', 'ccDd'], ['cCdD', 'cCdd', 'ccdD', 'ccdd']]
    >>> punnett('CcDd', 'CcDd', pprint=True)
    CCDD CCDd CcDD CcDd
    CCdD CCdd CcdD Ccdd
    cCDD cCDd ccDD ccDd
    cCdD cCdd ccdD ccdd
    >>> punnett('cCDd', 'CcdD', pprint=True)
    cCDd cCDD ccDd ccDD
    cCdd cCdD ccdd ccdD
    CCDd CCDD CcDd CcDD
    CCdd CCdD Ccdd CcdD
    """
    
    
    if pprint == False:
        c_1 = combinations(C1)
        c_2 = combinations(C2)
        #if the value False was passed to the pprint argument, the result must be returned as a list of lists.
        list_big = []
        for i in c_1:
            #lists in lists
            list_small = []
            for j in c_2:
                #ordering the sequence of the genotypes
                list_small.append(i[0]+j[0]+i[1]+j[1])
            list_big.append(list_small)
        return list_big

    elif pprint == True:
        c_1 = combinations(C1)
        c_2 = combinations(C2)
        #if the value True was passed to the pprint argument, the result must be returned as a string.
        group_big = ''
        for i in c_1:
            #each 'group_small' are separated.
            group_small = ''
            for j in c_2:
                #ordering the sequence of the genotypes
                #the genotypes on the same row are separated from each other by a single space.
                group_small+=i[0]+j[0]+i[1]+j[1]+' '
            #the rows of the square are at separate lines
            group_big+=group_small.rstrip()+'\n'
        return group_big.rstrip()

print(punnett('cCDd', 'CcdD', pprint=True))

def colorDistribution(D1,D2):
    """
    >>> colorDistribution('CcDd', 'CcDd')
    {'blue': 3, 'seal': 9, lilac': 1, 'chocolate': 3}
    >>> colorDistribution('cCDD', 'cCDD')
    {'seal': 12, 'chocolate': 4}
    >>> colorDistribution('ccDD', 'ccDD')
    {'chocolate': 16}
    >>> colorDistribution('ccdd', 'CcDd')
    {'blue': 4, 'lilac': 4, 'seal': 4, 'chocolate': 4}
    """
    
    list_d = punnett(D1,D2)
    
    #make a new list to count each colors easy
    new_list_d = []
    for p in list_d:
        for q in p:
            new_list_d.append(color(q))
    
    #the function must return a dictionary whose keys are the point colors that may occur in the offspring of the two cats whose genotypes are given.
    group = {}
    for d in new_list_d:
        #for each color that is used as a key in the dictionary, the associated value must indicate how many of the 16 possible genotypes of the kittens result in that particular color.
        group[d] = group.get(d, 0)+1
    return group

if __name__ == '__main__':
    import doctest
    doctest.testmod()