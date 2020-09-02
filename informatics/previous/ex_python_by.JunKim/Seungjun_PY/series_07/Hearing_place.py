'''
Created on 2015. 10. 23.

@author: USER
'''
set1 = ['ou','a','e','i','o','u','y','ee','ei','ie']
set2 = ['t','b','d','f','k','l','m','n','p','r']

def digit2letters(integer, first = True):
    
    if first == True:
        
        return set1[int(integer)]
    
    elif first == False:
        
        return set2[int(integer)]
    
def coord2word(coo):
    
    coo = coo.replace('¡Æ','').split("'")
    
    latitude = coo[0]
    answer = ''
    
    for x in range(len(latitude)):
        
        if int(x) % 2 == 0:
            
            answer += digit2letters(latitude[x])
            
        
        else:
            
            answer += digit2letters(latitude[x], False)
    
    
    if coo[1] == 'S':
        answer = 'S' + answer
    elif coo[1] == 'W':
        answer = 'V' + answer
    
    return answer.title()

def placename(p1, p2 = None):
    
    if p2 == None:
        
        answer = ''
        
        p1 = p1.replace(' ','').split(',')
        
        for x in p1:

            answer += coord2word(x) + ' '
             
        return answer[:-1]
    else:
        
        return coord2word(p1) + ' ' + coord2word(p2)
    
    
#print(placename("34¡Æ61'S, 58¡Æ38'E"))