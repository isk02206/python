'''
Created on 2016. 2. 12.

@author: User
'''
def rowKey(char, keyboard = 'QWERTYUIOP|ASDFGHJKL|ZXCVBNM'):
    
    char = char.upper()
    keyboard = keyboard.upper()
    #lower case�� �ٲܼ� �ִ�
    
    row = 1
    
    for x in keyboard:
        #while roof�� �ٲܼ� �ִ�
        
        if x == '|':
            row += 1
            
        elif x == char:
            return row

def rowWord(word, keyboard = 'QWERTYUIOP|ASDFGHJKL|ZXCVBNM'):
    #word�� �ҹ��ڷ� �ü��ֱ� ������ upper�� �ٲ���
    word = word.upper()
    keyboard = keyboard.upper()
    
    list1 = []
    
    
    for char in word:
        
        if not rowKey(char, keyboard) in list1:
            # ���� ���ڰ� ���°�� �ϳ��� ���´�
            list1.append(rowKey(char, keyboard))
            
        elif rowKey(char, keyboard) == None:
            #������� ? �� ���ڰ� ���ð��
            return None
            
    if len(list1) == 1:
        
        return list1[0]
    
def longestWord(list1, keyboard = 'QWERTYUIOP|ASDFGHJKL|ZXCVBNM', row = None):
    
    keyboard = keyboard.upper()
    list2 = []
    
    
    for word in list1:
            
        if rowWord(word, keyboard) == None:
            #�Ѱ��� �ٷθ� �̷������ �ƴ�
            list1.remove(word)
            #�� ����Ʈ���� ���� ����
        if row:
            #row�� �־��� ���
            if rowWord(word, keyboard) == row:
                #�ο���尡 �־��� �ο�� ������쿡
                list2.append(word)
                #����Ʈ ���� ��������
    if row:
        #list1 ��list2�� ���ƾ���
        list1 = list2
    #list3 = []
    #for word2 inlis1:
    #list3.append(lwn(word2))
    
    #for word in list1:
        #if len(word) == max(list3)
            #return word
            
            #������ ���� �ٸ��� �ٲٴ� ���
    for word in list1:
        if len(word) == max(len(x) for x in list1):
                        # list1 �ȿ��ִ� x���� ���ؼ� ���� �� len �� ���� x�� �̾Ƴ�
            return word
        

print(longestWord(['Alaghsas', 'Erattupetta', 'Hazorasp', 'Piripiri', 'Tuntum'], row=3))