'''
Created on 2015. 10. 9.

@author: Haeun Kim
@Student number: 01413456
'''
from string import punctuation


n=int(input()) #number of lines
text2=''


for text1 in range (int(n)):
    text1=input()
    changed_text=text1.replace(" ","")  #changed text is the removal of space in the text1
    text2 += changed_text  #fill changed text to text as a line
    x = text2.lower() #make all alphabet as small letter
count=0   #to calculate from 0
words=0
secret_message=''
Guess= False  #guess it is a given condition

for words in (x):                 
    
    if words in punctuation:
        Guess=True     #when the condition is satisfied, turns to true
    if Guess:           # guess turns true
        if words.isalpha():
            count += 1
        
    if count == 3:        
        secret_message += words  #write words after 3 punctuation
        Guess=False           # false when count is over 3
        count=0
                
print(secret_message.lower())
