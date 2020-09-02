def isISBN13(code):
    if len(code) != 13:
        return False
    if not code.isdigit():
        return False
    together = sum([factor * int(score) for factor, score in zip(6 * [1, 3], code[:-1])]) % 10

    together = (10 - together) % 10
    return together == int(code[-1])


def overview(number):
    '''
    >>> codes = [
    ...    '9789743159664', '9785301556616', '9797668174969', '9781787559554',
    ...    '9780817481461', '9785130738708', '9798810365062', '9795345206033',
    ...    '9792361848797', '9785197570819', '9786922535370', '9791978044523',
    ...    '9796357284378', '9792982208529', '9793509549576', '9787954527409',
    ...    '9797566046955', '9785239955499', '9787769276051', '9789910855708',
    ...    '9783807934891', '9788337967876', '9786509441823', '9795400240705',
    ...    '9787509152157', '9791478081103', '9780488170969', '9795755809220',
    ...    '9793546666847', '9792322242176', '9782582638543', '9795919445653',
    ...    '9796783939729', '9782384928398', '9787590220100', '9797422143460',
    ...    '9798853923096', '9784177414990', '9799562126426', '9794732912038',
    ...    '9787184435972', '9794455619207', '9794270312172', '9783811648340',
    ...    '9799376073039', '9798552650309', '9798485624965', '9780734764010',
    ...    '9783635963865', '9783246924279', '9797449285853', '9781631746260',
    ...    '9791853742292', '9781796458336', '9791260591924', '9789367398012'
    ... ]
    >>> overview(codes)
    English speaking countries: 8
    French speaking countries: 4
    German speaking countries: 6
    Japan: 3
    Russian speaking countries: 7
    China: 8
    Other countries: 11
    Errors: 9
    '''

    gather = {}
    for i in range(11):
        gather[i] = 0
    for code in number:
        if isISBN13(code):
            gather[int(code[3])] += 1
        else:
            gather[10] += 1

    print('{}: {}'.format('English speaking countries', gather[0] + gather[1]))
    print('{}: {}'.format('French speaking countries', gather[2]))
    print('{}: {}'.format('German speaking countries', gather[3]))
    print('{}: {}'.format('Japan', gather[4]))
    print('{}: {}'.format('Russian speaking countries', gather[5]))
    print('{}: {}'.format('China', gather[7]))
    print('{}: {}'.format('Other countries', gather[6] + gather[8] + gather[9]))
    print('{}: {}'.format('Errors', gather[10]))


if __name__ == '__main__':
    import doctest

    doctest.testmod()