def molecularFormula(fomula):
    result = {}
    count = 0
    atom = ''

    list_of_atom = []

    while count < len(fomula):

        if fomula[count].isupper():

            atom = fomula[count]

            for j in fomula[count + 1:]:
                if j.islower():
                    atom += j
                elif not j.isalpha() or j.isupper():
                    break

            list_of_atom.append(atom)
        if atom:
            count += len(atom)
        else:
            count += 1

        atom = ''

    for i in list_of_atom:
        result[i] = list_of_atom.count(i)


    return result
# print(molecularFormula('OCaOSeOO'))

print(molecularFormula('A1E5B2E5C3D4E5'))
def isomers(structure1, structure2):
    if molecularFormula(structure1) == molecularFormula(structure2):
        return True
    return False
