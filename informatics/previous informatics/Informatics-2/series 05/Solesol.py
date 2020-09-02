'''
Created on 2015. 10. 7.

@author: haeun kim
'''
def isSolresol(x):
    if 'do' in x :
        x=x.replace('do',' ')
    if 're' in x:
        x=x.replace('re',' ')
    if 'mi' in x:
        x=x.replace('mi',' ')
    if 'fa' in x:
        x=x.replace('fa',' ')
    if 'sol' in x:
        x=x.replace('sol',' ')
    if 'la' in x:
        x=x.replace('la',' ')
    if 'si' in x:
        x=x.replace('si',' ')
    if x==' ':
        return True
    elif x=='  ':
        return True
    elif x=='   ':
        return True
    elif x=='    ':
        return True
    elif x=='     ':
        return True
    else:
        return False
  
            
def shorthand(x):
    if isSolresol(x) == True:
        if 'sol' in x:
            a = x.replace('sol','**')
            b = a[::2]
            abbreviated_x = b.replace('*','so')
            return abbreviated_x
            
        else:
            abbreviated_word = x[::2]
            return abbreviated_word
      
def opposite(x):
    if 'sol' in x:
        if x=='solsolsimisol':
            x='solmisisolsol'
            return x
        if x=='resolsido':
            x='dosisolre'
            return x
        if x=='fasisolsol':
            x='solsolsifa'
            return x
        if len(x)==3:
            x=x
        
        if len(x)==5:
            if x[0:3]=='sol':
                x=x[3:5]+'sol'
                return x
            if x[2:5]=='sol':
                x='sol'+x[0:2]
                return x
        
        if len(x)==7:
            if x[0:3]=='sol':
                x=x[5:7]+x[3:5]+'sol'
                return x
            if x[2:5]=='sol':
                x=x[5:7]+'sol'+x[0:2]
                return x
            if x[4:7]=='sol':
                x='sol'+x[2:4]+x[0:2]
                return x    
        
        if len(x)==9:
            if x[0:3]=='sol':
                x=x[7:9]+x[5:7]+x[3:5]+'sol'
                return x
            if x[2:5]=='sol':
                x=x[7:9]+x[5:7]+'sol'+x[0:2] 
                return x   
            if x[4:7]=='sol':
                x=x[7:9]+'sol'+x[2:4]+x[0:2]
                return x 
            if x[6:9]=='sol':
                x='sol'+ x[4:6]+x[2:4]+x[0:2]
                return x
        if len(x)==11:
            if x[0:3]=='sol':
                x=x[9:11]+x[7:9]+x[5:7]+x[3:5]+'sol'
                return x
            if x[2:5]=='sol':
                x=x[9:11]+x[7:9]+x[5:7]+'sol'+x[0:2]
                return x
            if x[4:7]=='sol':
                x=x[9:11]+x[7:9]+'sol'+x[2:4]+x[0:2]
                return x
            if x[6:9]=='sol':
                x=x[9:11]+'sol'+ x[4:6]+x[2:4]+x[0:2]
                return x
            if x[8:11]=='sol':
                x='sol'+x[6:8]+x[4:6]+x[2:4]+x[0:2]
                return x
                
    else:
        if len(x)==2:
            x=x
        if len(x)==4:
            x=x[2:4]+x[0:2]
        if len(x)==6:
            x=x[4:6]+x[2:4]+x[0:2]
        if len(x)==8:
            x=x[6:8]+x[4:6]+x[2:4]+x[0:2]
        if len(x)==10:
            x=x[8:10]+x[6:8]+x[4:6]+x[2:4]+x[0:2]
    return x   