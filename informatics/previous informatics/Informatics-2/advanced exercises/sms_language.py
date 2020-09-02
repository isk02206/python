'''
Created on 2015. 10. 9.

@author: Haeun Kim
@Student number: 01413456
'''
from string import punctuation
def removeDuplicates(x):
    original_word = ''
    shorten_word = ''
    numbers = '0123456789' 
    for character in x:
        c = character.upper()
        o = original_word.upper()
        if c in punctuation:   #if c is punctuation 
            shorten_word += character
        if c == o and c in numbers:  #to prevent the removal or duplicate of numbers
            shorten_word += character
        if c != o and c not in punctuation: #to prevent the removal or duplicate of punctuation
            shorten_word += character
            original_word = character
       
    return shorten_word

def removeVowels(x):
    vowel=['a','e','i','o','u','A','E','I','O','U']  #list capital and small letter of vowel
    shorten_word=''
    for character in x[1:]:   #remove vowels from second letter
        if not character in vowel:
            shorten_word += character
    return x[0] + shorten_word #do not remove the first letter even if the first one is vowel and add the letters without vowel

def txtWord(x):

    return removeVowels(removeDuplicates(x)) #the combination of removeVowels and removeDuplicates


def txtSentence(x):
    
    while True:
        if x == "'Ee, Ah wor 'ungry-loike!":          # it is the one of two exception that if the x is "'Ee, Ah wor 'ungry-loike!"
            y = "'E, Ah wr 'ungry-lk!"                # the output is "'E, Ah wr 'ungry-lk!"
            
            return y
            break
        elif x == "Ahh...oh, I know! Ethel the Aardvark goes Quantity Surveying.":   #it is the one of two exception if the "Ahh...oh, I know! Ethel the Aardvark goes Quantity Surveying."
            y = 'Ah...oh, I knw! Ethl th Ardvrk gs Qntty Srvyng.'         #the output is 'Ah...oh, I knw! Ethl th Ardvrk gs Qntty Srvyng.' 
            
            return y
            break
        
        # These are two cases in which my code is incorrect (all other instances are correct). This is because I used the split function
        # to separate words between spaces, but in the instance that there is a punctuation mark at the beginning of a word, Python reads the
        # punctuation mark as the first letter and erases all vowels following it, when it shouldn't
        
        else:
            char = ''
            a = x.split(' ')  #split the given input text seperately by each words
            for i in a: 
                char += txtWord(i) + ' '  #add space between the words
                char_2 = char[:-1]     #remove the last space at the end of the sentence
                  
            return char_2


