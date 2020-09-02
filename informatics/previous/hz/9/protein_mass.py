def massTable(text):
    reader = open(text, 'r')
    data = reader.readlines()
    
    dict_1 = {}
    for d in data:
        d = d.split()
        key,value = d[0],d[1]
        dict_1[key] = float(value)
    return dict_1


def proteinMass(protein, dict_1, peptide=False):
    total = 0
    for p in protein:
        total+=dict_1[p]
    
    if peptide==True:
        return total
    else:
        return total+18.01056

table = massTable('mass.txt')
print(table['A'])
print(proteinMass('SKADYEK', table, peptide=True))