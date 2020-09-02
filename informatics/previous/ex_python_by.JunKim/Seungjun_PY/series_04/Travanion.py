'''
Created on 2015. 10. 4.

@author: Jun Kim
@student_number : 01503749
'''

from string import punctuation # import punctuation
A = int(input())# Sentence number
sen = ''
for x in range(A): # generate for loop in order to make the paragraph in one long sentence.
    B  = input()
    sen += B
sen = sen.replace(" ","") # remove the spaces.
count = 0
answer = ''
x = 0
while x < len(sen) - 3: # generate the while loop to check all the characters in the sentence.
    a = x+1
    if sen[x] in punctuation: # start consideration at the point where the punctuation exists.
       
        for i in range(len(sen[a:])): #generate another for loop in order to traverse to third alphabet from point x.
            
            if sen[a:][i].isalpha():
                count += 1
                
                if count == 3: # add the character to a blank string, 'answer'.
                    answer += sen[a:][i]
                    print(x)
                    count = 0 # return count to 0.
                    break # break the for loop and goes back to the while loop.
    
        x = x + i # modify the starting point to the character.
       
    x += 1   # if point x is not punctuation, moves to next character.
print(answer.lower()) # lowering the answer.

