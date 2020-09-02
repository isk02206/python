'''
name : Ha Young Kim
student number : 01603259
'''

def reverseComplement(sqs):
    """
    >>> reverseComplement('GATATC')
    'GATATC'
    >>> reverseComplement('GCATGC')
    'GCATGC'
    >>> reverseComplement('AGCTTC')
    'GAAGCT'
    """
    
    #forming a reversing 'sqs' by using list(because the reverse complement is formed by reversing the string)
    sqs = list(sqs)
    sqs.reverse()
    new_sqs = ''
    #the reverse complement is taking the complement of each character.
    for s in sqs:
        if s == 'A':
            new_sqs += 'T'
        elif s == 'C':
            new_sqs += 'G'
        elif s == 'G':
            new_sqs += 'C'
        elif s == 'T':
            new_sqs += 'A'
    return new_sqs

def reversePalindrome(B):
    """
    >>> reversePalindrome('GATATC')
    True
    >>> reversePalindrome('GCATGC')
    True
    >>> reversePalindrome('AGCTTC')
    False
    """
    
    #A DNA sequence is a reverse palindrome if it is equal to its reverse complement.
    if reverseComplement(B) == B:
        return True
    elif reverseComplement(B) != B:
        return False

def restrictionSites(C, minLength = 4, maxLength = 12):
    """
    >>> restrictionSites('TCAATGCATGCGGGTCTATATGCAT')
    [(4, 'ATGCAT'), (5, 'TGCA'), (6, 'GCATGC'), (7, 'CATG'), (17, 'TATA'), (18, 'ATAT'), (20, 'ATGCAT'), (21, 'TGCA')]
    >>> restrictionSites('AAGTCATAGCTATCGATCAGATCAC',minLength=5)
    [(6, 'ATAGCTAT'), (7, 'TAGCTA'), (12, 'ATCGAT')]
    >>> restrictionSites('ATATTCAGTCATCGATCAGCTAGCA',maxLength=5)
    [(1, 'ATAT'), (12, 'TCGA'), (14, 'GATC'), (18, 'AGCT'), (20, 'CTAG')]
    """
    
    
    result = []
    for i in range (len(C)):
        #the function has two additional optional arguments minLength and maxLength that respectively take the minimal and maximal length of the palindromes that must be taken into account to determine the restriction sites.
        for j in range (minLength,maxLength+1):
            if reversePalindrome(C[i:i+j]) == True:
                answer = (i+1, C[i:i+j])
                #to remove some exception that 'j' doesn't function because of the limitation, 'i'(from '0' to the length of 'C')
                if minLength<=len(C[i:i+j])<=maxLength:
                    result.append(answer)
                else:
                    pass
    #to remove some overlapped result by using set
    result = set(result)
    #the answer must be taken as the form of list
    return list(sorted(result))

if __name__ == '__main__':
    import doctest
    doctest.testmod()