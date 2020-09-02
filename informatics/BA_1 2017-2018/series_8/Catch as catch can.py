def missing_parameter(parameter,equation):
    '''
    >>> missing_parameter({'F':1.2, 'D':0.6, 'H':2, 'B':4}, 'FDVBH')
    'V'
    >>> missing_parameter({'D': 0.6, 'B': 4, 'V': 0.3, 'H': 2}, 'FDVBH')
    'F'
    >>> missing_parameter({'F':1.2, 'D':0.6, 'H':2, 'X':4}, 'FDVBH')
    Traceback (most recent call last):
    AssertionError: invalid parameters
    >>> missing_parameter({'F':1.2, 'D':0.6, 'H':2}, 'FDVBH')
    Traceback (most recent call last):
    AssertionError: invalid parameters
    '''
    letter = ''
    for i in parameter.keys():
        letter += i
    missing = 0
    for j in equation:
        if j not in letter:
            missing += 1
            y = j
    if missing > 1 or missing == 0:
        raise AssertionError('invalid parameters')
    else:
        return y

def juggle(value):
    '''
    >>> juggle({'F':1.2, 'D':0.6, 'H':2, 'B':4})
    {'F': 1.2, 'D': 0.6, 'B': 4.0, 'V': 0.3, 'H': 2.0}
    >>> juggle({'D': 0.6, 'B': 4, 'V': 0.3, 'H': 2})
    {'D': 0.6, 'V': 0.3, 'F': 1.2, 'H': 2.0, 'B': 4.0}
    >>> juggle({'F':1.2, 'D':0.6, 'H':2, 'X':4})
    Traceback (most recent call last):
    AssertionError: invalid parameters
    '''
    parameter = {}
    for i in value.keys():
        parameter[i] = value[i]
    equation = 'FDVBH'
    x = missing_parameter(parameter,equation)
    if x == 'F':
        d = parameter['D']
        v = parameter['V']
        b = parameter['B']
        h = parameter['H']
        f = (b/h)*(v+d) - d
        parameter['F'] = f
    if x == 'D':
        f = parameter['F']
        v = parameter['V']
        b = parameter['B']
        h = parameter['H']
        d = (b*v - h*f)/(h-b)
        parameter['D'] = d
    if x == 'V':
        f = parameter['F']
        d = parameter['D']
        b = parameter['B']
        h = parameter['H']
        v = (h/b)*(f+d) -d
        parameter['V'] = v
    if x == 'B':
        f = parameter['F']
        d = parameter['D']
        v = parameter['V']
        h = parameter['H']
        b = h*(f+d)/(v+d)
        parameter['B'] = b
    if x == 'H':
        f = parameter['F']
        d = parameter['D']
        v = parameter['V']
        b = parameter['B']
        h = b*(v+d)/(f+d)
        parameter['H'] = h
    new_parameter = {}
    for j in parameter.keys():
        k = parameter[j]
        new_parameter[j] = float(format(k,'.1f'))
    return new_parameter

