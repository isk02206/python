def massTable(file):
    reading = open(file, 'r').readlines()
    
    dict1 = {}
    x = 0
    protein = ''
    num = ''
    
    for line in reading:
        
        line = line.replace(' ','')
        
        while x < len(line):
        
            if line[x].isalpha():
                protein += line[x]
                
            else:
                num += str(line[x])
            
            x += 1
        if num[-1] == '\n':    
            dict1[protein] = float(num[:-1])
        else:
            dict1[protein] = float(num)
        
        x = 0
        protein = ''
        num = ''
        
    return dict1

def proteinMass(protein, table, peptide = False):
    
    mass = 0
    for x in protein:
        mass += table[x]
        
    if peptide == True:
        return mass
    else:
        return mass + 18.01056


table = massTable('mass.txt')
print(proteinMass('SKADYEK', table))