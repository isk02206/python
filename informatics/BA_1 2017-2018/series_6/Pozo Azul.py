def crossSection(row, corride):
    '''
    >>> crossSection(4, 'NSSWNSSWNWNWEWSWNSSEEWSWEWSENSSWNENWNSNEEWEWSWSENWNESEEWNWNWSESW')
    [['NS', 'SW', 'NS', 'SW', 'NW', 'NW', 'EW', 'SW'], ['NS', 'SE', 'EW', 'SW', 'EW', 'SE', 'NS', 'SW'], ['NE', 'NW', 'NS', 'NE', 'EW', 'EW', 'SW', 'SE'], ['NW', 'NE', 'SE', 'EW', 'NW', 'NW', 'SE', 'SW']]
    >>> crossSection(4, 'NSSWNSSWNWNWEWSWNSS')
    Traceback (most recent call last):
    AssertionError: invalid cross section
    '''
    hor = (len(corride)//2)//row


    if (len(corride)//2)/row == hor:
        #group in 2
        i_count = 0
        group_in_2 = []
        row_group = []
        hor_group = []

        cave = []
        for i in corride:
            i_count+=1
            group_in_2.append(i)
            if i_count == 2:
                x = ''.join(group_in_2)
                row_group.append(x)
                i_count = 0
                group_in_2 = []
        j_count = 0
        for j in row_group:
            j_count += 1
            hor_group.append(j)
            if j_count == hor:
                j_count = 0
                cave.append(hor_group)
                hor_group = []
        return cave
    else:
        raise AssertionError('invalid cross section')

def depth(cave):
    '''
    >>> cave = crossSection(4, 'NSSWNSSWNWNWEWSWNSSEEWSWEWSENSSWNENWNSNEEWEWSWSENWNESEEWNWNWSESW')
    >>> depth(cave)
    11
    '''
    able = {'N':{'NS','SN','NE','EN',}}
    ver = len(cave) #vertical length
    hor = len(cave[0]) #horizontal length
    start = cave[0][0]#starting road
    for i in range(ver):
        for j in range(hor):






if __name__ == '__main__':
    import doctest
    doctest.testmod()


