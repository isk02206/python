'''
Created on 2015. 10. 23.

@author: User
'''
def median(contigs):
    contigs1 = sorted(contigs)
    if len(contigs) % 2 == 0:
        l = int(len(contigs1) / 2)
        return float(contigs1[l] + contigs1[l-1]) / 2
    else:
        l = int((len(contigs1) - 1) / 2)
        return float(contigs1[l])
    
    
def extend(contigs):
    contigs2 = sorted(contigs)
    for j in range(len(contigs2)):
        for i in range(int(contigs2[j]) - 1):
            contigs2.append(contigs2[j])
    
    contigs1 = sorted(contigs2)
    return contigs1

def N50(contigs):
    contigs = sorted(contigs)
    return median(extend(contigs))

contigs = (2, 2, 2, 3, 3, 4, 8, 8)
print(median(contigs))
print(extend(contigs))
print(N50(contigs))
