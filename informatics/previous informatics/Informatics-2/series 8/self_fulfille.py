'''
Created on 2015. 10. 30.

@author: User
'''
penstrokes = [3, 3, 1, 2, 4, 3, 2, 3, 1, 2, 3, 2, 4, 3, 1, 2, 2, 3, 1, 2, 1, 2, 4, 2, 3, 3]
def lettervalue(penstrokes):
    count=65
    k=0
    a=dict()
    for x in penstrokes:
        a[chr(count)]=x
        count += 1
        
    return a

def wordvalue(word, penstrokes):
    words = ''
    for y in word:
        if y.isalpha():
            words += y
    
    words=words.upper().replace(' ','')
    value = lettervalue(penstrokes)
    b = 0
    for x in words:
        b += value[x]
    return b
print(wordvalue('Twenty-nine', penstrokes))    