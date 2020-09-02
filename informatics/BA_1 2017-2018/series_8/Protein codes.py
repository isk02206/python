def aminoword(x):
    '''
    >>> aminoword('ALEA')
    True
    >>> aminoword('iacta')
    True
    >>> aminoword('Proline')
    False
    '''
    x = x.lower()
    y = x.count('a')
    if y == 0:
        return False
    else:
        return True
def position(protein, x):
    '''
    >>> protein = 'HGLAVPFRTTHPSLECGRTSWARWSLDIAEFWLAWEASDCITDEDTKFQGDAVVAQM'
    >>> positions(protein, 'A')
    [3, 21, 28, 33, 36, 51, 54]
    >>> positions(protein, 't')
    [8, 9, 18, 41, 45]
    '''


def proteincode(protein, p, s, l):

def proteinsearch(protein,x):

