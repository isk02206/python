'''
Created on 2016. 1. 20.

@author: User
'''
def palindromic(num):
    #change the type of number into string
    num = str(num)
    #make one string which is the reverse version of the num
    num2 = num[::-1]
    #check whether it is palindromic.
    return num == num2

def palindromicmultiples(n,c):
    #set variables
    first = str(1)
    
    count = 0
    #make the starting number of consideration (whether it ispalindromic)
    for x in range(0, c-1):
        #���� ��� 1000 = c�� 4 �׷��� 0�� 3��
        #�׷��� 1���� 0 3�����̸� 1000
        first += str(0)
    #���� ����  #limit the positional numbers as the amount of c   
    while len(first) == c:
        #check every numbers within the positional numbers
         #whether it is the palindromic and it is the multiple of n
        if int(first) % n == 0 and palindromic(first):
            
            # if so, add one ������ ��� ���� �ɰ�� count+1
            count += 1
        
        first = str(int(first) + 1)
    #return the count which satisfies the following condition    
    return count