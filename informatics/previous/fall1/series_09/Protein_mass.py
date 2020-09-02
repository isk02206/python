def massTable(text):
    mass = open(text, 'r')
    table = mass.readlines()
    dic1 = {}
    
    for line in table:
        line = line.split()
        key, value = line[0], line[1]
        dic1[key] = float(value)
        
    return dic1
        
def proteinMass(proteins, func1, peptide=False):
    
    mass = 0
    
    for protein in proteins:
        
        mass += func1[protein]
        
    if peptide==True:
        
        return mass
    
    else:
        
        return mass + 18.01056