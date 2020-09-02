def group(list):
    '''
    >>> group(['9Y', '7R', '9Y', '7R', '9Y', '7R', '9Y'])
    {'9Y': 4, '7R': 3}
    >>> group(['1Y', '7Y', '8Y', '12Y', '12B', '13B', '13B', '13Z', '13Y', '2Z', '3Z', '4Z', '11Z', '11Z', '4R', '5R'])
    {'8Y': 1, '12Y': 1, '13B': 2, '3Z': 1, '5R': 1, '7Y': 1, '1Y': 1, '13Y': 1, '4Z': 1, '13Z': 1, '12B': 1, '2Z': 1, '4R': 1, '11Z': 2}
    '''
    dict = {}
    for x in list:
        if x in dict:
            dict[x] = dict[x]+1
        else:
            dict[x] = 1
    return dict

def play(a,b):
    '''
    >>> meld = group(['13B', '13Z', '13Y'])
    >>> rack = group(['1Y', '7Y', '8Y', '12Y', '12B', '13B', '13B', '13Z', '13Y', '2Z', '3Z', '4Z', '11Z', '11Z', '4R', '5R'])
    >>> play(meld, rack)
    True
    >>> meld
    {'13B': 1, '13Y': 1, '13Z': 1}
    >>> rack
    {'8Y': 1, '12Y': 1, '13B': 1, '3Z': 1, '5R': 1, '7Y': 1, '1Y': 1, '4Z': 1, '12B': 1, '2Z': 1, '4R': 1, '11Z': 2}
    
    >>> meld = group(['12B', '12Z', '12Y'])
    >>> play(meld, rack)
    False
    >>> rack
    {'8Y': 1, '12Y': 1, '13B': 1, '3Z': 1, '5R': 1, '7Y': 1, '1Y': 1, '4Z': 1, '12B': 1, '2Z': 1, '4R': 1, '11Z': 2}
    '''
    meld = {}
    rack = {}
    meld = a
    rack = b
    if meld in rack:
        meld = {}
        return True
    else:
        return False

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    
'''
1. diff color and same numb
2. same color
meld: card want to use
rack: card have
'''
#use count()in dictionary
