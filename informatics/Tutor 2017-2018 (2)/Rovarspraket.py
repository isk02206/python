'''
Created on 2018. 1. 14.

@author: TaeWoo
'''

'''
>>> encode('robber language')
'rorobbobberor lolangonguagoge'
>>> encode('Kalle Blomkvist')
'Kokallolle Bloblomkvomkvistost'
>>> encode('Astrid Lindgren')
'Astrostridod Lolindgrondgrenon'

'''

def encode(sentence):
    
    vowel = ['a', 'e', 'i', 'o', 'u', "'", ',', '.', '?', '-']
    
    words = sentence.split(' ')
    codes = list()
    consonants = ''
    
    for word in words:
        
        code = ''
        letter_list = []
        
        for letter in word:
            
            if letter.lower() in vowel:   
                
                if consonants != '':    
                    letter_list.append(consonants)
                
                letter_list.append(letter)
                consonants = ''
            
            else:
                consonants += letter
        
        if consonants != '':
            letter_list.append(consonants)
            consonants = ''
        
        for parts in letter_list:
            
            if word[0] == parts and parts.lower() in vowel:
                code += parts
            
            elif parts not in vowel:
                code += parts + 'o' + parts.lower()
                
            else:
                code += parts
                
        codes.append(code)
        
    return ' '.join(codes)
    

def decode(codes):
    
    codes_list = codes.split(' ')
    vowel = ['a', 'e', 'i', 'o', 'u', "'", ',', '.', '?', '-']
    sentence = list()
    
    for code in codes_list:
        
        part = ''
        vowel_count = 0
        consonants_list = []
        consonants = ''
        
        while code[0].lower() in vowel:
            part += code[0]
            code = code[1:]
            
            if len(code) == 0:
                break
        
        counter = 0
        
        for letter in code:
            
            if letter.lower() in vowel:
                
                if code[counter-1] in vowel:
                    part += letter
                    
                else:
                    vowel_count += 1
                
                    if vowel_count % 2 != 0:
                        part += consonants
                        consonants = ''
                    
                    elif vowel_count % 2 == 0:
                        part += letter
                
            elif vowel_count % 2 == 0:
                consonants += letter
            
            counter += 1
        
        sentence.append(part)
        
    return ' '.join(sentence)
print(decode('rorobbobberor lolangonguagoge'))
#print(decode('Nariko-San, Girl of Japan'))

if __name__ == '__main__':
    import doctest
    doctest.testmod() 