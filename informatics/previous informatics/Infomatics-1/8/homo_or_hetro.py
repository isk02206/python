'''
Created on 2016. 2. 13.

@author: User
'''
def homoOrHetero(list1):
    list2 = []
    count = 0
    if len(list1) == 1:
        return 'nothing'
    else:
        for x in list1:
            list2.append(x)
            print(list2)
            if list1[0] == list1[2]:
                
            return 'homo'
    
print(homoOrHetero([1,1,1]))