'''
Created on 2015. 10. 7.

@author: Jun Kim
'''
def isSolresol(word) :
    
    note = word.count('do') + word.count('re') + word.count('mi') + word.count('fa') + word.count('sol') + word.count('la') + word.count('si')
    length = word.count('do')*2 + word.count('re')*2 + word.count('mi')*2 + word.count('fa')*2 + word.count('sol')*3 + word.count('la')*2 + word.count('si')*2
    if length == len(word) and note < 6:
        return True
    else :
        return False
def shorthand(word) :
    x = []
    short = ''
    for i in range(len(word) - 1) :
        if word[i] == 'd' or word[i] == 'r' or word[i] == 'm' or word[i] == 'f' or word[i] == 's' or word[i]== 'l' :
            if word[i] == 'l' and word[i+1] != 'a' :
                continue
            x.append(i)
            if word[i] == 's' and word[i+1] == 'o' :
                x.append(i+1)
   
                for i in x :
                    
                    short += word[i]
                    return short
def opposite(word) :
        x = []
        opposite = ''
        for i in range(len(word) - 1) :
            if word[i] == 'd' :
                x.append('do')
            elif word[i] == 'r' :
                x.append('re')
            elif word[i] == 'm' :
                x.append('mi')
            elif word[i] == 'f' :
                x.append('fa')
            elif word[i] == 's' :
                if word[i+1] == 'o' :
                    x.append('sol')
                else :
                    x.append('si')
            elif word[i] == 'l' :
                if word[i+1] == 'a' :
                    x.append('la')
            for i in range(len(x)) :
                opposite += x[len(x)-1-i]
                return opposite
    