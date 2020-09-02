'''
Created on 2015. 12. 2.

@author: User
'''
def  hamming(seq1,seq2):
    
    count = 0
    assert len(seq1)== len(seq2), 'strings should have equal length'
    for x in range(len(seq1)):
          if seq1[x] != seq2[x]:
            count += 1
    return count

def complement(seq):

    x = seq[::-1]
    count = ''
    for y in x:
        if y == 'T':
            count += 'A'
        elif y == 'C':
            count += 'G'
        elif y == 'A':
            count += 'T' 
        elif y == 'G':
            count += 'C' 
    return count

def normalform(seq):
    list1 = []
    vari = complement(seq)
    list1.append(seq)
    list1.append(vari)
    list.sort()
    return list1[0]
def occurrences(seq):
    list =[]
    dict = {}
    count = 0
    for x in seq:
        list.append(normalform(x))
    for seq in list:
        dict[seq] = list.append(seq)
    return

def errors(seq):
    seq = list(seq)
    correct = []
    incorrect = []
    group = set()
    list = set()
    list1 = []
    
    a = len(seq)
    seq1 = seq
    
    for x in range(len(seq)):
        if seq[x] != complement(seq[x]):
            seq1.append(object)
        
if __name__ == '__main__':
    import doctest
    doctest.testmod()
    
