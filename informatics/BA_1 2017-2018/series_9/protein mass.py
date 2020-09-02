def massTable(text):
    reader = open(text, 'r')

    data = reader.readlines()

    mass = {}
    for protein in data:
        protein = protein.split()
        key, value = protein[0], protein[-1]
        mass[key] = float(value)
    return mass


def proteinMass(protein, mass, peptide=False):
    sum = 0
    for each in protein:
        sum += mass[each]

    if peptide == True:
        return sum

    elif peptide == False:
        return sum + 18.01056