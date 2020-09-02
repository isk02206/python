def DNAPalindrome(base):
    new_dna = ''
    for dna in base:
        if dna == 'A':
            dna = 'T'
        
        elif dna == 'T':
            dna = 'A'
        
        elif dna == 'G':
            dna = 'C'
        
        elif dna == 'C':
            dna = 'G'
        
        new_dna += dna
    palindrome = new_dna[::-1]
    
    if base == new_dna[::-1]:
        return True
    
    else:
        return False
    
    

def longestPalindrome(base):
    #Using 2 for loops to find all combinations
    #For example [0:1] , [0:2  0:x] then [1:2 1:x] so on 
    max_base = ''
    for start_pos in range(len(base)):
        for end_pos in range(start_pos+1, len(base)):
            temp_base = base[start_pos:end_pos]
            #Applying the first function into the variable temp_base to check if it is a palindrome sequence
            if DNAPalindrome(temp_base) == True and len(temp_base) > len(max_base):
                max_base = temp_base
                
    return max_base