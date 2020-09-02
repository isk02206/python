def massTable(text):
    '''
    >>> table = massTable('mass.txt')
    >>> table['A']
    71.03711
    >>> table['E']
    129.04259
    '''
    reader = open(text, 'r')
    table = {}
    data = reader.readlines()
    for x in data:
        alpha = ''
        digit = ''
        for i in x:
            if 65<=ord(i)<=90 or 97<=ord(i)<=122:
                alpha += i
            if 48<=ord(i)<=57 or ord(i)==46:
                digit += i
        table[alpha] = float(digit)
    return table

def proteinMass(codon,table,peptide=False):
    '''
    >>> table = massTable('mass.txt')
    >>> proteinMass('SKADYEK', table)
    839.40248
    >>> proteinMass('SKADYEK', table, peptide=True)
    821.3919199999999
    '''
    sum = 0
    for i in codon:
        sum += table[i]
    if peptide == True:
        return sum
    if peptide == False:
        sum += 18.01056
        return sum
