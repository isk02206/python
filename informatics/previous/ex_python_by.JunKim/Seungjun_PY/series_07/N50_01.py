'''
Created on 2015. 10. 23.

@author: USER
'''
def N50_decreasing(contigs, size= None):
    contigs = list(contigs)
    contigs = sorted(contigs)
    reverse = contigs[::-1]
    summ = 0
    i = 0
    if size == None:
        size = sum(contigs)
    while summ < size/2:
        summ += reverse[i]
        i += 1
    return reverse[i-1]
   
def N50_increasing(contigs, size= None):
    contigs = list(contigs)
    contigs = sorted(contigs)
    summ = 0
    a = 0
    if size == None:
        size = sum(contigs)
    while summ < size/2:
        summ += contigs[a]
        a += 1
    return contigs[a-1]

def N50(contigs, size=None):
    contigs = list(contigs)
    contigs = sorted(contigs)
    if size == None:
        count = 0
        size = sum(contigs)
        for y in range(len(contigs)):
            count += contigs[y]
        size = count
    else:
        size = size
        
    n1 = int(N50_decreasing(contigs, size=size))
    n2 = int(N50_increasing(contigs, size = size))
    n3 = (n1 + n2)/2
    return float(n3)
contigs = (2, 2, 2, 3, 3, 4, 8, 8)
print(N50(contigs))