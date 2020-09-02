'''
Created on 2015. 12. 3.

@author: User
'''
def  homoOrHetero(list1):
    dict = {}
    for x in list1:
        dict[x] = list1.count(x)
    
    groupA = []
    groupB = []
    
    for key, value in dict.items():
        groupA += [key]
        groupB += [value]
    
    if len(groupA) == 1:
        if groupB[0] != 1:
            return 'homo'
        else:
            return 'nothing'
    elif len(groupA) != 1:
        for y in groupB:
            if y != 1:
                return 'both'
        else:
            if list1 == []:
                return 'nothing'       
        
            else:
                return 'hetero'
                
    
print(homoOrHetero([]))