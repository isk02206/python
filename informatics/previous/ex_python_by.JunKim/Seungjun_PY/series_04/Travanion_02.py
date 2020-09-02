'''
Created on 2015. 10. 7.

@author: USER
'''
import string

number = int(input())

message = ''
hidden_message = ''    

for i in range(number):
    message += input() 
    
punctuation_mark_found = False 
alpha_count = 0 


for character in message.lower(): 
    
    if character in string.punctuation: 
        punctuation_mark_found = True 
        
    if punctuation_mark_found:
        
        if character.isalpha(): 
            alpha_count += 1  
        
        if alpha_count == 3: 
            punctuation_mark_found = False 
            alpha_count = 0 
            hidden_message += character

print(hidden_message)
