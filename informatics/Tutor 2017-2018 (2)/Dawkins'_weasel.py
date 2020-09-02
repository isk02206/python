'''
Created on 2018. 1. 24.

@author: TaeWoo
'''

from string import ascii_uppercase
import random

def fitness(word1, word2):
    
    assert len(word1) == len(word2), 'strings must have equal length'
    
    match = 0
    position = 0
    
    for letter in word1:
        
        if letter == word2[position]:
             match += 1
             
        position += 1
    
    return match

def mutation(word, mutations=1):
    
    assert mutations <= len(word), 'invalid number of mutations'
    
    positions = [i for i in range(len(word))]
    uppercase = list(ascii_uppercase)
    uppercase.append(' ')
    mutated = []
    
    while mutations != len(mutated):
        rand_position = positions[random.randint(0, len(positions)-1)]
        
        if rand_position not in mutated:
            mutated.append(rand_position)
            
        
    mutated = sorted(mutated, key=int)
    result = ''

    for position in range(len(word)):
        
        if position in mutated:
            random_letter = random.choice(uppercase)
            
            while word[position] == random_letter:
                random_letter = random.choice(uppercase)
                
            result += random_letter
             
        else:
            result += word[position]
    
    return result

def crossover(word1, word2, point=None):
    
    assert len(word1) == len(word2), 'strings must have equal length'
    
    if point == None:
        positions = [i for i in range(1,len(word1))]
        point = random.choice(positions)
    
    assert point > 0 and point < len(word1), 'invalid crossover point'
    
    new_word1 = word1[:point] + word2[point:]
    new_word2 = word2[:point] + word1[point:]
    
    return (new_word1, new_word2)
    
           
print(fitness('WEASEL', 'WETSEL'))
print(mutation('WEASEL'))
print(crossover('METHINKS', 'AARDVARK'))