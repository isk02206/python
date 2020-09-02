def massTable(text):
    dictionary = {}
    for line in open(text, 'r'):
        line = line.rstrip().split()
        key, value = line[0], line[1]
        #if key in dictionary:
            #dictionary[key].add(float(value))
            
        if key not in dictionary:
            dictionary[key] = float(value)
            
    return dictionary

    #print(massTable('mass.txt')) 

def proteinMass(protein, table, peptide = False):
    
    sum = 0
    
    if peptide == True:
        for line in protein:
            sum += float(table[line])
        
        return sum

    else:
        for line in protein:
            sum += float(table[line])
        sum += 18.01056
    
    return sum