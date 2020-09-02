class GeneticCode:
    '''
    >>> code = GeneticCode('standard_code.txt')

    >>> code.aminoacid('AGT')
    'S'
    >>> code.aminoacid('cga')
    'R'
    >>> code.aminoacid('UCU')
    'S'
    >>> code.aminoacid('ABC')
    Traceback (most recent call last):
    AssertionError: 'ABC' is not a valid codon.
    >>> code.aminoacid('aagc')
    Traceback (most recent call last):
    AssertionError: 'aagc' is not a valid codon.

    >>> code.protein('ATGCTGATGATGGGCTATTATCGAT')
    'MLMMGYYR'
    >>> code.protein('uauccuaguguc')
    'YPSV'
    >>> code.protein('AAGTCGTAGCTACGXXXXGAGAAGGAT')
    Traceback (most recent call last):
    AssertionError: invalid DNA or RNA sequence.
    '''

    def __init__(self, code):

        reader = open(code, 'r')
        content = reader.readlines()

        codes = ''
        for line in content:
            codes += line.rstrip() + ' '

        self.codes = codes

    def aminoacid(self, codon):
        uppercodon = codon.upper()
        for i in uppercodon:
            if i == 'U':
                uppercodon = uppercodon.replace(i, 'T')

        if uppercodon not in self.codes:
            raise AssertionError("'{}' is not a valid codon.".format(codon))
        if len(uppercodon) >= 4:
            raise AssertionError("'{}' is not a valid codon.".format(codon))

        if uppercodon in self.codes:
            position = self.codes.index(uppercodon) + 4
            return self.codes[position]