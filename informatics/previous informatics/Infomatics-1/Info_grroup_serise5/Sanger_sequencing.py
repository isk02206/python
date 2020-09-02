'''
Created on 2016. 1. 25.

@author: User
'''
def sanger(DNA):
    
    Ad, Cy, Gu, Th = '','','',''
    S1, S2, S3, S4  = '', ' ' * 9, ' ' * 99, ' ' * 999   
    
    for Value in DNA:
        
        if Value == 'A':
            Ad += 'A'
            
        elif Value != 'A':
            Ad += '-'
        
        if Value == 'C':
            Cy += 'C'
        
        elif Value != 'C':
            Cy += '-'
            
        if Value == 'G':
            Gu += 'G'
            
        elif Value != 'G':
            Gu += '-'
            
        if Value == 'T':
            Th += 'T'
            
        elif Value != 'T':
            Th += '-'

    ALL = Ad + '\n' + Cy + '\n' + Gu + '\n' + Th

    for d in range(1, len(DNA) + 1):
        
        if len(str(d)) == 1:
            
            S1 += str(d)
            result = S1 + '\n' + ALL + '\n' + ('=' * len(DNA)) + '\n' + DNA
    
        elif len(str(d)) == 2:
            
            N = list(str(d))
            S2 += N[0]
            S1 += N[1]
            result = S2 + '\n' + S1 + '\n' + ALL + '\n' + ('=' * len(DNA)) + '\n' + DNA
            
        elif len(str(d)) == 3:
            
            N = list(str(d))
            S3 += N[0]
            S2 += N[1]
            S1 += N[2]     
            result = S3 + '\n' + S2 + '\n' + S1 + '\n' + ALL + '\n' + ('=' * len(DNA)) + '\n' + DNA
    
        elif len(str(d)) == 4:
            
            N = list(str(d))
            S4 += N[0]
            S3 += N[1]
            S2 += N[2]
            S1 += N[3]
            result = S4 + '\n' + S3 + '\n' + S2 + '\n' + S1 + '\n' + ALL + '\n' + ('=' * len(DNA)) + '\n' + DNA
    
    return result