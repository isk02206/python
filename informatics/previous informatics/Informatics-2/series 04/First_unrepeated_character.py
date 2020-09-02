'''
Created on 2016. 1. 6.

@author: User
'''
word = str(input())
word.lower()
a=[]

for x in word:
    if x not in a:
        a.append(x) #리스트에 넣으면 x가 한글자씩 리스트에 들어감
                    #예를 들어 aabbcc가 x이면 abc로 리스트에 들어감
b=0
for y in a:
    if word.count(y):
        if word.count(y) == 1:
            b-=1
            print(word.find(y))
            break
if b == 0:
    print(-1)