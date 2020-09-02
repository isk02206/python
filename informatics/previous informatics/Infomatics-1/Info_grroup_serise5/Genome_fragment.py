'''
Created on 2016. 1. 27.

@author: User
'''

def code2graph(sym):
    
    if sym[0] == 'F':
        
        return '=' * (int(sym[1])-1) + '>'
        
    if sym[0] == 'B':
        
        return '<' + '=' * (int(sym[1])-1)
    
    if sym[0] == 'N':
        
        return '-' * int(sym[1])
    

def symb2graph(seq):
    
    pos = 0
    
    result = ''
    
    while pos < len(seq):
        
        if seq[pos] == 'B':
        
            if pos + 2 < len(seq):
                
                if seq[pos+2] == 'F':
                    
                    result += code2graph(seq[pos:pos+2]) + '|'
                    
        else:
            result += code2graph(seq[pos:pos+2])
        
        pos += 2
        
    return result

def graph2symb(seq):
    
    #for
        #for 가능 하지만 랙 하나더는 불가능 
    result = ''
    
    pos = 0
    
    sec = ''
    
    while pos < len(seq):
        
        if seq[pos] == '-':
    
            for x in seq[pos:]:
                
                if x == '-':
                    
                    sec += x
                    
                elif x != '-':
                    break
            
            result += 'N' + str(len(sec)) 
            
            pos += len(sec)
            
            sec = ''
            
        elif seq[pos] == '=':
            
            for x in seq[pos:]:
                
                if x == '=':
                    
                    sec += x
                    
                elif x == '>':
                    
                    sec += x
                    break
                
            result += 'F' + str(len(sec))
            pos += len(sec)
            
            sec = ''
            
        elif seq[pos] == '<':
            
            sec += seq[pos]
            
            for x in seq[pos+1:]:
                
                if x == '=':
                    
                    sec += x
                    
                elif x != '=':
                    
                    break
                
            result += 'B' + str(len(sec))
            pos += len(sec)
            
            sec = ''
            
        elif seq[pos] == '|':
            
            pos += 1
            
    return result
