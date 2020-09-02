'''
Created on 2016. 1. 27.

@author: User
'''

def letter2digits(char,seq1,seq2,seq3):
    
    num_seq2 = seq1.find(' ')
    num_seq3 = seq1.rfind(' ')
    
    list1 = []
    list1.append(seq1)
    list1.append(seq2)
    list1.append(seq3)
    
    for lists in list1:
        
        if char in lists:
            
            pos1 = list1.index(lists)
            pos2 = lists.find(char)
            break
    
    if pos1 == 0:
                
        return str(pos2)
            
    elif pos1 == 1:
                
        return str(num_seq2) + str(pos2)
            
    elif pos1 == 2:
                
        return str(num_seq3) + str(pos2)
            
def digits2letter(num,seq1,seq2,seq3):
    
    num_seq2 = seq1.find(' ')
    num_seq3 = seq1.rfind(' ')
    
    list1 = []
    list1.append(seq1)
    list1.append(seq2)
    list1.append(seq3)
    
    if len(num) == 2:
        if int(num[0]) == num_seq2:
            return list1[1][int(num[1])]
            
        elif int(num[0]) == num_seq3:
            return list1[2][int(num[1])]
        
    else:
        pos = int(num[0])
        return list1[0][pos]
    
    
def code(sen, seq1, seq2, seq3):
    
    result = ''
    
    for char in sen:
      
        result += letter2digits(char, seq1, seq2, seq3)
        
    return result

def decode(code,seq1,seq2,seq3):
    
    num_seq2 = seq1.find(' ')
    num_seq3 = seq1.rfind(' ')
    
    result = ''
    
    pos = 0
    
    while pos < len(code):
        
        if code[pos] == str(num_seq2) or code[pos] == str(num_seq3):
            
            num = code[pos:pos+2]
            
            result += digits2letter(num, seq1, seq2, seq3)
            
            pos += 2
            
        else:
            
            result += digits2letter(code[pos], seq1, seq2, seq3)
            
            pos += 1
            
    return result