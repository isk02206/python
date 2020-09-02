'''
Created on 2015. 10. 1.

@author: JunKIm
'''
number= int(input())
number_name= input()
final_answer = ""
list = []
for i in range(number) :
    a = input()
    b = a.index(',')
    english_name = a[:b]
    Alphabat = a[b+2:]
    capital = Alphabat.lower()
    
    for i in range (len(capital)):
        count = 0
        value = int(ord(capital[i])) - (ord(capital[i])-1)
        count = count + value
        if english_name > count:
            print(str(english_name)+'['+str(count)+']')
