'''
Created on 2016. 1. 20.

@author: User
'''
def decode(text, column): # �ڷ��� ���ٿ� ��� ������ ����
    #set variables
    repeat = len(text) // column
    
    list1 = []
    
    count = 0
    
    answer = ''
    #arrange the text into the format according to the given column as term of the list
    for x in range(repeat):
        
        sub_text = ''
        
        for y in range(column):
            
            sub_text += text[count + y]
            
        list1 += [sub_text]
        
        count += len(sub_text)
    #reverse the list of every even row    
    for pos in range(0, len(list1)):
        
        if pos % 2 != 0: #¦�����ϋ� 
            
            list1[pos] = list1[pos][::-1]
    #arrange the lists into the string form        
    for w in range(column):
        
        for z in list1:
            
            answer += z[w]
            
    return answer