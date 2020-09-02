'''
Created on 2016. 1. 25.

@author: User
'''
# set definition of canonical(codon)

def canonical(codon):
    
    # In the case where the middle base is replaced with the complementary base, x is the complementary base. 
    
    if codon[1] == 'A':
        x = 'T'
        
    elif codon[1] == 'T':
        x = 'A'
    
    elif codon[1] == 'G':
        x = 'C'
    
    elif codon[1] == 'C':
        x = 'G'
        
    # codon_1 is when the left and right bases are exchanged whereas the middle base is still on the same position.
    
    codon_1 = codon[2] + codon[1] + codon[0]
    
    # codon_2 is when the left and right bases are exchanged and the middle base is replaced with value x
    
    codon_2 = codon[2] + x + codon[0]
    
    # condon_3 is when the middle base is exchanged where the left and right bases are still on the same position.
    
    codon_3 = codon[0] + x + codon[2]   
    
    # Using sorted(), the four codons will be listed with the alphabetical order. 
    
    List = sorted([codon] + [codon_1] + [codon_2] + [codon_3])
    
    # If the list[0] is returned, the first alphabetic order will come out.
    
    return List[0]


# set definition for codon2aa(codon)

def codon2aa(codon):
    
    # Consider the all possible cases for each place of triples. 
    # Set distinct value for each base
    # Determine W value according to the base value. 
    
    if canonical(codon)[0] == 'G':
        W1 = 0
    elif  canonical(codon)[0] == 'T':
        W1 = 1
    elif canonical(codon)[0] == 'C':
        W1 = 2
    elif canonical(codon)[0] == 'A':
        W1 = 3
        
    if canonical(codon)[1] == 'G':
        W2 = 0
    elif  canonical(codon)[1] == 'T':
        W2 = 1
    elif canonical(codon)[1] == 'C':
        W2 = 2
    elif canonical(codon)[1] == 'A':
        W2 = 3
        
    if canonical(codon)[2] == 'G':
        W3 = 0
    elif  canonical(codon)[2] == 'T':
        W3 = 1
    elif canonical(codon)[2] == 'C':
        W3 = 2
    elif canonical(codon)[2] == 'A':
        W3 = 3
    
    # Operator this given function to determine the alphabet of the protein.
    
    P = (W1 + 4 * W2 + 16 * W3) % 25
    
    # If p = 0, the alphabet is A and the alphabet steps up one by one as the p value increases one by one. 
    # This means the following list can be used to to determine the alphabet according to the p value.
    
    List = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    
    # List[p] will give the protein for each codon.
    
    return List[P]

# Set definition for dna2protein(codon)

def dna2protein(codon):
    
    # set the under and upper limit. 
    
    under_limit = 0
    upper_limit = 3
    
    # set triple result as nothing to add through loop later.
    
    triple_result = ''
    
    # set the condition that the length of codon is not equal to the upper limit -1 because at the moment, it will be the final codon.
    
    while len(codon) != upper_limit - 1:
        
        # set triple in the codon with the range between upper and under limit. 
        
        triple = codon[under_limit: upper_limit]
        
        # Through this formula the protein will be arranged in the order.
        
        triple_result += codon2aa(triple)
        
        # Move the codon to the right direction with adding one to each upper and under limit
        
        under_limit += 1
        upper_limit += 1

    else: 
        return (triple_result)