'''
Created on 2015. 10. 5.

@author: Jun Kim
@student_number : 01503749
'''
#letter = input()

sentence = input()
max= int(input())
line = sentence
line_count = 0
#line count maximum :10 (because line should not be over 10)
while line_count < 10:
    line_count += 1
    
    while len(line) <= max: #when line equals to the max

        line += ' '+ sentence 
    
    position = max
    while not line[position].isspace():#When the conditions are not met , turn the while loop 
                                       #.isspace() is used to remove space
        position = position-1
            
       
    print(line[0:position]) #starts 0 position

    if line[position-1] == line[-1]:
        break #loop stop
    
    line = line[position+1:]      
                          
     
    
    
#print(len('The quick brown fox jumps over the lazy dog. The quick'))
