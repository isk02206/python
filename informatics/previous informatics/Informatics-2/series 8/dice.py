'''
Created on 2015. 10. 30.

@author: User
'''
dice6_1 = {1, 2, 3, 4, 5, 6}
dice6_2 = [1, 2, 2, 3, 3, 4]
dice6_3 = (1, 3, 4, 5, 6, 8)
def combination(x,y):
    list = []
    
    for a in x:
        for b in y:
            tuple = a,b
            list.append(tuple)
    
    haeun = {}    
    for p in list:
        L , R = p
        sum = L + R
        haeun.setdefault(sum, []).append(p)
    
    for q in haeun.values():
        q.sort()
                
    return haeun

throw = combination(dice6_1,dice6_2)

def distribution(x,y):
    
    dictionary = combination(x,y)
    result = {}
    list = []
    for a,b in dictionary.items():
        result[a] = len(b)
        
            
    return result


dice8_1 = {1, 2, 3, 4, 5, 6, 7, 8}
dice8_2 = (1, 3, 5, 5, 7, 7, 9, 11)
dice8_3 = (1, 2, 2, 3, 3, 4, 4, 5)
dice8_4 = (1, 2, 5, 5, 6, 6, 9, 10)
dice8_5 = (1, 2, 3, 3, 4, 4, 5, 6)
def equalDistribution(x,y):

    L,R = x
    L2,R2 = y
    return distribution(L,R) == distribution(L2,R2)

print(equalDistribution((dice8_1, dice8_1), (dice8_2, dice8_3)))
print(equalDistribution((dice8_1, dice8_1), (dice8_3, dice8_4)))
