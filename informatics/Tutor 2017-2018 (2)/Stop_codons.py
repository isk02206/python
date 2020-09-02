'''
Created on 2018. 1. 16.

@author: TaeWoo
'''


def isStopCodon(codon):
    
    stop_codon = ['TAG', 'TGA', 'TAA']
    start_codon = ['ATG']
    
    return codon.upper() in stop_codon

def reverseComplement(seqeunce):
    
    complement = {'A':'T', 'T':'A', 'G':'C', 'C':'G'}
    reverse = ''
    
    for base in seqeunce[::-1].upper():
        
        reverse += complement[base]
    
    return reverse

def stopCodons(seq, frame):
    
    seq = seq.upper()
    
    if frame == +2:
        seq = seq[1:]
        
    elif frame == +3:
        seq = seq[2:]
        
    elif frame == -1:
        seq = reverseComplement(seq)
        
    elif frame == -2:
        seq = reverseComplement(seq)[1:]
        
    elif frame == -3:
        seq = reverseComplement(seq)[2:]
        
    divide = int(len(seq) // 3)
    start = 0
    stop = 3
    counter = 0
    
    for i in range(divide):
        
        if isStopCodon(seq[start:stop]) is True:
            counter += 1
        
        start += 3
        stop += 3
    
    return counter

def codons(seq, frame):
    
    result = ''
    
    if frame == +2:
        result += seq[0]
        seq = seq[1:]
        
        
    elif frame == +3:
        result += seq[:2]
        seq = seq[2:]
        
    elif frame == -1:
        seq = reverseComplement(seq)
       
    elif frame == -2:
        seq = reverseComplement(seq)
        result += seq[0]
        seq = seq[1:]
        
    elif frame == -3:
        seq = reverseComplement(seq)
        result += seq[:2]
        seq = seq[2:]
        
    divide = int(len(seq) // 3)
    start = 0
    stop = 3
    
    for i in range(divide):
        
        if result == '':
            result += seq[start:stop]
            
        else:
            result += '-' + seq[start:stop]
        
        start += 3
        stop += 3
    
    if len(seq)-1 >= stop-3:
        result += '-' + seq[stop-3:]
    
    return result
    
print(isStopCodon('tag'))
print(reverseComplement('AGTCTTACGCTTA'))
print(stopCodons('TTTACTATAGTGATAGCCGGTAACATAGCTCCTAGAATAAAGGCAACGCAATACCCCTAGG', +2))
