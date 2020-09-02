'''
Created on 2015. 12. 2.

@author: User
'''
def atomicmass(file):
    dict1 = {}
    for line in file.readlines():
        if 'atomic' in line:
            pass
        else:
            
            for char in line.split('\n'):
                if char.split() != []:
                    dict1[char.split()[1]] = float(char.split()[-1])
    return dict1

def molecularmass(molecule, index):
    
    list1= molecule.split('-')
    atom = ''
    num = ''
    mass = 0
    
    for x in list1:
        for y in x: 
            if y.isalpha():
                atom += y
            elif y.isdigit():
                num += y
        
        if num:
            mass += index[atom] * int(num)
        else:
            mass += index[atom]
        
        atom = ''
        num = ''
        
    return mass 
    
index = atomicmass(open('periodic_system.txt'))
print(index['Si'])
print(molecularmass('H2-S-O4', index))        