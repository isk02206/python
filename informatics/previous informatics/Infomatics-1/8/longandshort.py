'''
Created on 2016. 2. 13.

@author: User
'''
table = {'hello': 1, 'world':1}
def longShort(table, n):
    first = 0
    second = 0
    for x,y in table.items():
        if len(x) == n:
            first += y
            second += 0
        
        if  n >= 10:
            if len(x)< n:
                first += 0
                second += y
        
        a = n - len(x)
        if a == 1:
            first += y
            second += y
            break
        
        
    return (first,second)


print(longShort(table, 5 ))
print(longShort(table, 6 ))