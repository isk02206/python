'''
Created on 2016. 2. 13.

@author: User
'''
protein = 'AQITGRPEWI'
kd = { 
    'A': 1.8, 'R':-4.5, 'N':-3.5, 'D':-3.5, 'C': 2.5,  
    'Q':-3.5, 'E':-3.5, 'G':-0.4, 'H':-3.2, 'I': 4.5,   
    'L': 3.8, 'K':-3.9, 'M': 1.9, 'F': 2.8, 'P':-1.6, 
    'S':-0.8, 'T':-0.7, 'W':-0.9, 'Y':-1.3, 'V': 4.2
    }

def hydrofobicity(protein,kd):
    list1 = []
    for x in protein:
        list1.append(kd[x])
    return list1
datapoints = hydrofobicity(protein, kd)
print(datapoints)
