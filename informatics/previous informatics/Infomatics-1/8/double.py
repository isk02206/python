'''
Created on 2016. 2. 15.

@author: User
'''
def double(list1):
    
    for char in list1:
        
        if list1.count(char) >= 2:
            
            return char
            
            
print (double([1, 2, 3, 4, 2]))
print (double([1, 2, 3, 4]))
print (double([1, 2, 3, 4, 5, 6, 100, -234, 15, 0, -20000, 15]))
            
def doubles(list1):
    
    set1 = set()
    set2 = set()
    
    for char in list1:
        
        if list1.count(char) >= 2:
            
            set1.add(char)
            
        else:
            set2.add(char)

    return set2,set1