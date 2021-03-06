'''
Created on 2015. 12. 2.

@author: User
'''
def molecular(molecule):
    
    dict1 = {}
    x = 0
    atom = ''
    
    list1 = []
    
    
    while x < len(molecule):
        
        if molecule[x].isupper():
            
            atom = molecule[x]
            
            for y in molecule[x+1:]:
                if y.islower():
                    atom += y
                elif not y.isalpha() or y.isupper():
                    break    
            
            list1.append(atom)
        if atom:
            x += len(atom)
        else:
            x += 1
            
        atom = ''
    
    for char in list1:
        dict1[char] = list1.count(char)
    
    
    return dict1
print(molecular('A1E5B2E5C3D4E5'))
def isomers(m1, m2):
    
    return molecular(m1) == molecular(m2)
