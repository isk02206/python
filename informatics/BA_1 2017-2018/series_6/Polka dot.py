def deal(number):
    '''
    >>> deal((0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
    [0, 2, 4, 6, 8, 10, 3, 7, 1, 9, 5]
    >>> deal([0, 8, 1, 6, 2, 10, 3, 7, 4, 9, 5])
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    >>> deal('ABCDEFGHIJKLMOP')
    ['A', 'C', 'E', 'G', 'I', 'K', 'M', 'P', 'D', 'H', 'L', 'B', 'J', 'F', 'O']
    >>> deal('ALBICODJEMFKGPH')
    ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'O', 'P']
    '''
    list_number = []
    picked = []
    x = len(number)

    for i in number:
        list_number.append(i)
    count = 0
    while len(list_number) != 0:
        for i in range(len(list_number)//2 +1):

        count += 1


