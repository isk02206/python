'''
Created on 2015. 11. 4.

@author: User
'''
def occurrences(word): 
    
    word = word.lower()
    result = dict()
    for a in word:
        for x in range(1,27):
            if a == chr(x+96):
                result[chr(x+ 96)]=word.count(chr(x+96))
    return result

print(occurrences('CHACHACHA'))
print(occurrences('Esophagographers'))
print(occurrences('happenchance'))



                
def isRepetitionWord(word, minimal_repetition=1):
    vari = occurrences(word)
    for x in vari.values():
        if x < minimal_repetition :
            return False
        
            break
        elif list(vari.values())[0] != x:
            
            return False
            break
    return True


def repetitionWords(file, minimal_repetition=1, minimal_length=1):
    
    reader = open(file, 'r')
    result = set()
    
    for word in reader.readlines():
        if isRepetitionWord(word, minimal_repetition) == True and len(word) >minimal_length:
            result.add(word[:-1])
    return result 
