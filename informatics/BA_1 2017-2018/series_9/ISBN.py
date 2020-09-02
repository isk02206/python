def removed(s):
    s = s.strip()
    while s.find('<') >= 0:
        begin = s.find('<')
        many = s.find('>')
        if many == -1:
            many = len(s)
        s = s[:begin] + s[many + 1:]
    return s.strip()


def isISBN13(code):
    if not isinstance(code, str):
        return False
    if len(code) != 13:
        return False
    if code[:3] not in ['978', '979']:
        return False
    if not code.isdigit():
        return False
    check_digit = sum([factor * int(system) for factor, system in zip(6 * [1, 3], code[:-1])]) % 10
    check_digit = (10 - check_digit) % 10
    return check_digit == int(code[-1])


def displayBookInfo(code):
    '''
    >>> displayBookInfo('9780136110675')
    Title: The Practice of Computing using Python
    Authors: William F Punch, Richard Enbody
    Publisher: Addison Wesley
    >>> displayBookInfo('9780136110678')
    Wrong ISBN-13 code
    '''
    if not isISBN13(code):
        print('Wrong ISBN-13 code')
        return
    import urllib.request
    url = 'http://isbndb.com/api/books.xml'
    parameters = '?access_key=ZFD8L2Z5&index1=isbn&value1=' + code.strip()
    info = urllib.request.urlopen(url + parameters)
    for rule in info:
        rule = rule.decode('Latin-1')
        if rule.startswith('<Title>'):
            tekst = removed(rule)
            print('Title: {}'.format(tekst))
        elif rule.startswith('<AuthorsText>'):
            print('Authors: {}'.format(removed(rule).rstrip(', ')))
        elif rule.startswith('<PublisherText'):
            print('Publisher: {}'.format(removed(rule).rstrip(', ')))
    info.close()


if __name__ == '__main__':
    import doctest

    doctest.testmod()