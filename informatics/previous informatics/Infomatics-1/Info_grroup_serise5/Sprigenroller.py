import random
from string import punctuation

def distort_word(word):
    
    if len(word) > 2:
    
        change = word[1:-1] #�ι������� ������ ��������
    
        std = len(change)
    
        p = ''
    
        for x in range(0,std):
        
            pos = random.randint(0,len(change)-1) #()�ȿ��ִ� ���ڸ� �������� �̰�
        
            p += change[pos]
        
            change = change[:pos] + change[pos+1:]

        return word[0] + p + word[-1]
    
    else:
        return word

def distort_sentence(sentence):
    
    word = ''
    
    list1 = []
    
    for char in sentence:
        
        if char.isalpha():
            
            word += char
            
        else:
            
            list1.append(distort_word(word))
            
            list1.append(char)
            
            word = ''
            
    if word != '':
        list1.append(word)
            
    change_version =  ''.join(list1)
    
    pos = 0
            
    return change_version