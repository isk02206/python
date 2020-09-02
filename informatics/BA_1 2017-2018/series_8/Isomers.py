def molecularFormula(structuralFormula):
    '''
    >>> structuralFormula1 = 'OCaOSeOO'
    >>> structuralFormula2 = 'HHCHHCHHCHHCHH'
    >>> structuralFormula3 = 'HHCHHHCCHHHCHH'

    >>> molecularFormula(structuralFormula1)
    {'Ca': 1, 'Se': 1, 'O': 4}
    >>> molecularFormula(structuralFormula2)
    {'H': 10, 'C': 4}
    >>> molecularFormula(structuralFormula3)
    {'C': 4, 'H': 10}
    '''
    element = {}
    molecule = ''
    structuralFormula=structuralFormula+'O'
    for i in range(len(structuralFormula)-1):
        if 65 <= ord(structuralFormula[i]) <= 90 and 97 <= ord(structuralFormula[i+1]) <= 122: #capital+ lowercase
            molecule = structuralFormula[i] + structuralFormula[i+1]
            if molecule in element:
                element[molecule] += 1
            if molecule not in element:
                element[molecule] = 1
            molecule = ''
        if 65 <= ord(structuralFormula[i]) <= 90 and 65 <= ord(structuralFormula[i+1]) <= 90: # only capital
            molecule = structuralFormula[i]
            if molecule in element:
                element[molecule] += 1
            if molecule not in element:
                element[molecule] = 1
            molecule = ''
        if 97 <= ord(structuralFormula[i]) <= 122: # only lowercase
            pass
    return element

def isomers(structuralFormulaA, structuralFormulaB):
    '''
    >>> structuralFormula1 = 'OCaOSeOO'
    >>> structuralFormula2 = 'HHCHHCHHCHHCHH'
    >>> structuralFormula3 = 'HHCHHHCCHHHCHH'
    >>> isomers(structuralFormula1, structuralFormula2)
    False
    >>> isomers(structuralFormula1, structuralFormula3)
    False
    >>> isomers(structuralFormula2, structuralFormula3)
    True
    '''
    element1 = molecularFormula(structuralFormulaA)
    element2 = molecularFormula(structuralFormulaB)
    for i in element1:
        if element1[i] != element2[i]:
            return False
    else:
        return True