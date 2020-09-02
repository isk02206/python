'''
Created on 2016. 1. 25.

@author: User
'''

def selfdescribing(n):
    #무조건 스트링 으로 바꾸기
    n = str(n)
    
    pos = 0
    
    while pos < len(n):
           
        if n.count(str(pos)) != int(n[pos]):
            return False
        
        pos += 1
        
    else:
        return True