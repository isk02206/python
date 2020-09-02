'''
Created on 2016. 2. 12.

@author: User
'''
def rowKey(char, keyboard = 'QWERTYUIOP|ASDFGHJKL|ZXCVBNM'):
    
    char = char.upper()
    keyboard = keyboard.upper()
    #lower case로 바꿀수 있다
    
    row = 1
    
    for x in keyboard:
        #while roof로 바꿀수 있다
        
        if x == '|':
            row += 1
            
        elif x == char:
            return row

def rowWord(word, keyboard = 'QWERTYUIOP|ASDFGHJKL|ZXCVBNM'):
    #word가 소문자로 올수있기 때문에 upper로 바꿔줌
    word = word.upper()
    keyboard = keyboard.upper()
    
    list1 = []
    
    
    for char in word:
        
        if not rowKey(char, keyboard) in list1:
            # 같은 숫자가 나온경우 하나만 적는다
            list1.append(rowKey(char, keyboard))
            
        elif rowKey(char, keyboard) == None:
            #예를들어 ? 나 숫자가 나올경우
            return None
            
    if len(list1) == 1:
        
        return list1[0]
    
def longestWord(list1, keyboard = 'QWERTYUIOP|ASDFGHJKL|ZXCVBNM', row = None):
    
    keyboard = keyboard.upper()
    list2 = []
    
    
    for word in list1:
            
        if rowWord(word, keyboard) == None:
            #한가지 줄로만 이루어진게 아님
            list1.remove(word)
            #그 리스트에서 월드 지움
        if row:
            #row가 주어진 경우
            if rowWord(word, keyboard) == row:
                #로우월드가 주어진 로우와 같을경우에
                list2.append(word)
                #리스트 투에 집에넣음
    if row:
        #list1 을list2로 갈아엎음
        list1 = list2
    #list3 = []
    #for word2 inlis1:
    #list3.append(lwn(word2))
    
    #for word in list1:
        #if len(word) == max(list3)
            #return word
            
            #마지막 루프 다르게 바꾸는 방법
    for word in list1:
        if len(word) == max(len(x) for x in list1):
                        # list1 안에있는 x들을 비교해서 제일 긴 len 를 가진 x를 뽑아냄
            return word
        

print(longestWord(['Alaghsas', 'Erattupetta', 'Hazorasp', 'Piripiri', 'Tuntum'], row=3))