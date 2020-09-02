'''
Created on 2016. 2. 15.

@author: User
'''
def heavenlyStem(num):
    
    dict1 = {0: 'yang wood', 1: 'yin wood', 2: 'yang fire', 3: 'yin fire',4: 'yang earth', 5: 'yin earth', 6: 'yang metal', 7: 'yin metal', 8: 'yang water', 9: 'yin water'}
    
    return dict1[num]

def earthlyBranch(num):
    dict1 = {0:'rat', 1: 'buffalo', 2: 'tiger',3: 'hare',4:'dragon', 5 : 'snake' ,6 : 'horse', 7: 'goat', 8: 'monkey' , 9 : 'chicken', 10:  'dog',11:  'pig'}
    
    return dict1[num]
    
def chineseYear(num):
    
    num = num + 2697 - 1
    
    a = num % 10

    b = num % 12
    
    return heavenlyStem(a) + '' + earthlyBranch(b)


print( heavenlyStem(3))
print (earthlyBranch(11))
print(chineseYear(2011))
