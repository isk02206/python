from _hashlib import new
def  digits2letters(word1, word2):
    pos = 0
    dict1 = {}
    while pos < len(word1):
        dict1[word1[pos]] = word2[pos]
        
        pos += 1
    return dict1

def beghilosz2text(word, dict1):
    
    new = ''
    
    for char in word:
    
        new += dict1[char]
        
    return new

def letters2digits(dict1):
    
    dict2 = {}
    
    for x,y in dict1.items():
        dict2[y] = x
    
    return dict2

def text2beghilosz(word,dict1):
    
    new = ''
    
    for char in word:
    
        new += dict1[char]
        
    return new