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
    def __init__(self,text):
        reader = open(text, 'r')
        content = reader.readlines()
        code = {}
        for line in content:
            line = line.rstrip()
            code[line[0:3].upper()] = line[4]
        self.code = code

    def aminoacid(self,codon):
        if len(codon) != 3:
            raise AssertionError("'" + codon + "'" + ' is not a valid codon.')
        valid_codons = 'ATGCUatgcu'
        for i in codon:
            if i not in valid_codons:
                raise AssertionError("'"+codon+"'"+' is not a valid codon.')
        codon = codon.upper()
        new_codon = ''
        for i in codon:
            if i == 'U':
                new_codon += 'T'
            else:
                new_codon += i
        return self.code[new_codon]

    def protein(self,seq):
        translation = ''
        valid_codons = 'ATGCUatgcu'
        for i in seq:
            if i not in valid_codons:
                raise AssertionError('invalid DNA or RNA sequence.')
        if (len(seq) % 3)!= 0:
            seq = seq[:len(seq)-(len(seq)%3)]
        for j in range(len(seq)//3):
            codon = seq[3*j:3*j+3]
            trans = self.aminoacid(codon)
            translation += trans
        return translation
