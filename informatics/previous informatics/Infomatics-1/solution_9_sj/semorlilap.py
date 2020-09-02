def dictionary(textfile):
    
    output = open(textfile, 'r').read().split('\n')
    
    set1 = set()
    
    for word in output:
        
        word = word.strip()
            
        set1.add(word.lower())
    
    return set1
    

def semordnilap(word, words):
    
    word = word.lower()
    
    return (word[::-1] not in words) and (word in words) and (word[::-1] != word)