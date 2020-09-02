'''
ID:01514170
Name: SungJoon Park
'''
def color(x):
    '''
    >>> color('CcDd')
    'seal'
    >>> color('ccdd')
    'lilac'
    '''
    if x == 'CCDD' or color == 'CCDd' or x == 'CcDD' or x == 'CcDd' or x == 'CCdD' or x == 'CcdD' or x == 'cCDD' or x =='cCDd' or color == 'cCdD':
        return 'seal'
    if x == 'ccDd' or x == 'ccDD' or x == 'ccdD':
        return 'chocolate'
    if x == 'CCdd' or x == 'Ccdd' or x == 'cCdd':
        return 'blue'
    if x == 'ccdd':
        return 'lilac'
    
def combination(x):
    '''
    >>> combinations('CcDd')
    ['CD', 'Cd', 'cD', 'cd']
    >>> combinations('ccdd')
    ['cd', 'cd', 'cd', 'cd']
    '''
    combination = []
    a = x[0]+x[2]
    b = x[0]+x[3]
    c = x[1]+x[2]
    d = x[1]+x[3]
    combination.append(a,b,c,d)

def colorDistribution(x,y):
    for i in range(4):
        for j in range(4):
            
    
def punnett(x,y):
    if pprint == False:
        c_1 = combinations(C1)
        c_2 = combinations(C2)
        list_big = []
        for i in c_1:
            list_small = []
            for j in c_2:
                list_small.append(i[0] + j[0] + i[1] + j[1])
            list_big.append(list_small)
        return list_big

    elif pprint == True:
        c_1 = combinations(C1)
        c_2 = combinations(C2)
        group_big = ''
        for i in c_1:
            group_small = ''
            for j in c_2:
                group_small += i[0] + j[0] + i[1] + j[1] + ' '
            group_big += group_small.rstrip() + '\n'
        return group_big.rstrip()
'''
ex
colorTable = {'CC':{'DD':'seal','Dd': }}
return colorTalble[x][y] # == color
dict[key] = value
'|n'.join()
'''