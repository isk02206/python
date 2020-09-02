def hamming(read1,read2):
    '''
    >>> hamming('TTCAT', 'TTCAT')
    0
    >>> hamming('TTCAT', 'TTGAT')
    1
    >>> hamming('TTCAT', 'GAGGA')
    5
    >>> hamming('TTCAT', 'TTT')
    
    '''
    assert len(read1) == len(read2), 'strings should have equal length'
    count = 0
    
    for x in range(len(read1)):
        if read1[x] != read2[x]:        
            count += 1
    return count

def complement(read):
    
    read = read[::-1]
    new = ''
    
    for x in range(len(read)):
        if read[x] == 'T':
            new += 'A'
        elif read[x] == 'A':
            new += 'T'
        elif read[x] == 'C':
            new += 'G'
        elif read[x] == 'G':
            new += 'C'
    return new

def normalform(read):
    
    list1 = []
    read2 = complement(read)
    list1.append(read)
    list1.append(read2)
    list1.sort()
    
    return list1[0]

def occurrences(reads):
    
    new = []
    dict1 = {}
    count = 0
    
    for x in reads:
        new.append(normalform(x))
    
    for seq in new:
        dict1[seq] = new.count(seq)
    
    return dict1

def errors(reads):
    reads = list(reads)
    correct = []
    incorrect = []
    group = set()
    list1 = set()
    list3 = []
    
    a = len(reads)
    new_read = reads
    
    for x in range(len(reads)):
        if reads[x] != complement(reads[x]):
            new_read.append(complement(reads[x]))

    for num in range(a):
        
        if new_read.count(new_read[num]) == 1:
            incorrect.append(new_read[num])
    
    for char in new_read:
        if new_read.count(char) >= 2:
            correct.append(char)
    
    for read1 in incorrect:
        for read2 in correct:
            if hamming(read1, read2) == 1:
                list1.add((read1, read2))
                list3.append(read1)
    
    for char in incorrect:
        if char not in list3:
            group.add(char)
            
    return group, sorted(list(list1))

if __name__ == '__main__':
    import doctest
    doctest.testmod()
