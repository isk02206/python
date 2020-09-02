'''
Created on 2015. 10. 22.

@author: USER
'''
alphabet= ['a','b','c','d','e','f','g','h',
           'i','j','k','l','m','n','o','p','q','r',
           's','t','u','v','w','x','y','z']
#number_of_occurences = [0] * 26
def occurrences(word):
    number_of_occurrences = [0] * 26
    for i in word.lower():
        if i in alphabet:
            a= alphabet.index(i)
            number_of_occurrences[a] += 1
    return number_of_occurrences
'''
print(occurrences('ambidextrously'))
print(occurrences('DOCTORWHO'))
print(occurrences('uncopyrightable'))
'''
#value = 0
def isogram(word):
    value = 0
    nword = word.lower()
    for i in occurrences(nword):
        if i > 1:
            value +=1
    if value > 0:
        return False
    else:
        return True

'''
print(isogram('denotations'))
print(isogram('imperatives'))
print(isogram('logarithmic'))
'''
'''
def isogram(word):
    number_of_occurrences = [0] * 26
    for i in word.lower():
        if i in alphabet:
            a= alphabet.index(i)
            number_of_occurrences[a] += 1
    if number_of_occurrences[a] > 1:
        return False
    else:
        return True   
'''
    
'''
print(isogram('ambidextrously'))
print(isogram('DOCTORWHO'))
print(isogram('uncopyrightable'))
'''


def anagram(word1, word2):
    if occurrences(word1) == occurrences(word2):
        return True
    else:
        return False
'''  
print(anagram('DOCTORWHO', 'Torchwood'))
print(anagram('isogram', 'anagram'))
print(anagram('Aristotelian', 'retaliations'))
'''