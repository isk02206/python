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

def isogram(word):
    number_of_occurrences = [0] * 26
    for i in word.lower():
        if i in alphabet:
            a= alphabet.index(i)
            number_of_occurrences[a] += 1        
    #print(number_of_occurrences)
    if number_of_occurrences.count(2) or number_of_occurrences.count(3) != 0:
        return False
    else: 
        return True
'''
print(isogram('ambidextrously'))
print(isogram('DOCTORWHO'))
'''
def median(contigs):
    import math
    x = len(contigs)
    if x % 2 == 0:
        first_number= (int(x)/2) - 1
        first_con = contigs[int(first_number)]
        second_number = first_number+1
        second_con = contigs[int(second_number)]
        value = (first_con+second_con)/2
        return(value)
    if x % 2 == 1:
        number = (int(x)/2) -1
        number_processed = math.ceil(number)
        number_con = contigs[number_processed]
        return(number_con)
contigs = (2, 2, 2, 3, 3, 4, 8, 8)

def median_02(contigs):
    import math
    x = len(contigs)
    y = sorted(contigs)
    if x % 2 == 0:
        first_number= (int(x)/2) - 1
        first_con = y[int(first_number)]
        second_number = first_number+1
        second_con = y[int(second_number)]
        value = (first_con+second_con)/2
        return(value)
    if x % 2 == 1:
        number = (int(x)/2) -1
        number_processed = math.ceil(number)
        number_con = y[number_processed]
        return(float(number_con))
contigs = (3,27,1)


