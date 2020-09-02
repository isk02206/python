'''
Created on 2015. 11. 18.

@author: USER
'''
def carousel(c,str1):
    list1=[]
    for i in range(c):
        list1.append(None)
    if len(str1) >= 1:
        list1[0]=str1[0]
    count=0
    pos=0
    check=True
    if len(str1)>=2:
        str1=str1[1:]
        while check:            
            for l in list1:
                if l==None:
                    count+=1
                if count==3:
                    list1[(pos)%c]=str1[0]
                    if len(str1)<=1:
                        check=False
                        if str1 in list1:
                            break
                    if len(str1)>=2:
                        str1=str1[1:]
                    count=0
                pos+=1
        last_letter=list1.index(str1[-1])
        list1=list1[last_letter:]+list1[:last_letter]   
    return list1
def rotated(list_2,list_3):
    checkdigit=0
    for i in range(len(list_2)):
        left=list_2[i:]
        right=list_2[:i]
        if list_3==left+right:
            checkdigit=1
    if checkdigit==1:
        return True
    if checkdigit==0:
        return False
print(carousel(8, 'ABCDE'))