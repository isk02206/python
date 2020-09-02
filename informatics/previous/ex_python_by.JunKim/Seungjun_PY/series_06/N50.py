'''
Created on 2015. 10. 23.

@author: USER
'''
def median(contigs):
    import math
    x = len(contigs)
    y = sorted(contigs)
    if x % 2 == 0:
        first_number= (int(x)/2) - 1
        first_con = y[int(first_number)]
        second_number = first_number+1
        second_con = y[int(second_number)]
        value = (first_con+second_con)/2
        return(value)
    if x % 2 == 1:
        number = (int(x)/2) -1
        number_processed = math.ceil(number)
        number_con = y[number_processed]
        return(float(number_con))

contigs = (2, 2, 2, 3, 3, 4, 8, 8)
print(median(contigs))

number= 0
def extend(contigs):
    list2 = []
    for contigs2 in contigs:
        for number in range(int(contigs2)): 
            list2 += [contigs2]   
    return list2

contigs = (2, 2, 2, 3, 3, 4, 8, 8)
print(extend(contigs))

def N50(Input):
    return median(extend(contigs))

contigs = (2, 2, 2, 3, 3, 4, 8, 8)
print(N50(contigs))