def group(list):
    '''
    >>> group(['4R', '4B', '4Y', '4K'])
    True
    >>> group({'6B', '7B', '8B', '9B', '10B'})
    False
    >>> group(('11R', '2B', '7Y', '2B', '9K'))
    False
    '''
    if len(list) < 3:
        return False
    number = {}
    color = {}
    for i in list:
        numb = ''
        for j in i:
            if j.isdigit() == True:
                numb += j
            if j.isalpha() == True:
                if j in color:
                    return False
                if j not in color:
                    color[j] = 1
        number[numb] = 1
    if len(number) == 1:
        return True
    else:
        return False
def run(list):
    '''
    >>> run(['4R', '4B', '4Y', '4K'])
    False
    >>> run({'6B', '7B', '8B', '9B', '10B'})
    True
    >>> run(('11R', '2B', '7Y', '2B', '9K'))
    False
    '''
    number = {}
    color = {}
    if len(list) < 3:
        return False
    for i in list:
        numb = ''
        for j in i:
            if j.isdigit() == True:
                numb += j
            if j.isalpha() == True:
                if j in color:
                    color[j] += 1
                if j not in color:
                    color[j] = 1
        if numb in number:
            return False
        if numb not in number:
            number[numb] = 1
    if len(color) != 1:
        return False
    number1 = []
    for key in number.keys():
        number1.append(int(key))
    number1 = sorted(number1)
    first = int(number1[0])-1
    for ele in number1:
        ele = int(ele)
        first += 1
        if ele != first:
            return False
    else:
        return True