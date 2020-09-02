'''
Created on 2015. 10. 8.

@author: JunKim
'''

def removeDuplicates(word):
    previous_character, compressed_word = '', ''
    for character in word:
        if character.lower() != previous_character.lower():
            compressed_word += character
            previous_character = character
    return compressed_word

def removeVowels(word):

    if not word:
        return ''
    vowels, compressed_word = 'aeiou', word[0]

    for character in word[1:]:
        if character.lower() not in vowels:
            compressed_word += character
    return compressed_word
 
def txtWord(word):
    
    return removeVowels(removeDuplicates(word))

def txtSentence(sentence):
    word, compressed_sentence = '', ''
    
    for character in sentence:
        if character.isalpha():
            word += character
        else:
            if word:
                compressed_sentence += txtWord(word) 
                word = ''
            compressed_sentence += character
            return compressed_sentence
    if word:
        compressed_sentence += txtWord(word)
    return compressed_sentence

print(removeDuplicates('bookkeeper'))
print(removeDuplicates('Aardvark'))
print(removeDuplicates('Aardvark'))
print(removeVowels('bookkeeper'))
print(removeVowels('Aardvark'))
print(removeVowels('eELGRASS'))
print(txtWord('Some'))
print(txtWord('people'))
print(txtWord('compress'))
print(txtWord('text'))
print(txtWord('messages'))
print(txtSentence('And now for something completely different!'))
print(txtSentence('Some people compress text messages by replacing doubled letters with single letters and by retaining only those vowels that begin a word.'))