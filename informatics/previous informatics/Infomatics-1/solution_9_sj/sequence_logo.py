def readFasta(textfile):

    reader = open(textfile, 'r').read().split('>')[1:]
    
    list1 = []
    base = ''
    for seq in reader:
        
        seq = seq.replace('\n', '')
      
        if seq:
            seq = seq[3:]
            for char in seq:
                if char.isalpha():
                    base+= char
            if base:    
                list1.append(base)
                base = ''
    return list1

def sequenceLogo(sequences, alphabet = 'acgt'):
    
    pos = 0

    word = ''
    
    list2 = []
    
    list1 = []
    
    while pos < len(sequences[0]):
        
        assert len(sequences[0]) == len(sequences[pos]), 'not all sequences have the same length'
        
        for seq in sequences:
           
            assert seq[pos].upper() in alphabet.upper(), 'invalid residu'
            
            word += seq[pos].upper()
        
        for base in alphabet.upper():
            
            
            list2.append((word.count(base)/len(word)))
        
        list1.append(list2)
        
        word = ''
        pos += 1
        list2 = []
        
    return list1
            
            
sequences = readFasta('seq.fasta.txt')
print(sequences)
print(sequenceLogo(sequences))