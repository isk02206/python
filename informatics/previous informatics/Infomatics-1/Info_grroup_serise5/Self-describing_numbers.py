'''
Created on 2016. 1. 25.

@author: User
'''

def selfdescribing(n):
    #������ ��Ʈ�� ���� �ٲٱ�
    n = str(n)
    
    pos = 0
    
    while pos < len(n):
           
        if n.count(str(pos)) != int(n[pos]):
            return False
        
        pos += 1
        
    else:
        return True