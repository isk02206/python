'''
Created on 2016. 1. 6.

@author: User
'''
word = str(input())
word.lower()
a=[]

for x in word:
    if x not in a:
        a.append(x) #����Ʈ�� ������ x�� �ѱ��ھ� ����Ʈ�� ��
                    #���� ��� aabbcc�� x�̸� abc�� ����Ʈ�� ��
b=0
for y in a:
    if word.count(y):
        if word.count(y) == 1:
            b-=1
            print(word.find(y))
            break
if b == 0:
    print(-1)