# Set the input.
# Strip the right and left white spaces of the text.
text = input().strip()
maximum = int(input())
line = 0
original_text = text
# The division will be the words to be added to the sentence.
division = text.split()

# the number of line shouldn't be more than 10.
while line != 10:
    
    
    # by for loop, set the number of repetitions of adding words.
    for x in range(int(len(division)*4)):
        
        
        # Evaluating which word to be added to the sentence.
        
        if x +1 == len(division):
            x = x
            
        elif x + 1 != len(division):
            x = x % len(division)
        
        sequence = division[x]
        
        
        # Add the word after a space.
        text = str(text) +" " + str(sequence)
        
        # when the text length is smaller than the max,
        # just continue adding the word.
        if len(text) < maximum:
                        
            continue

        # After adding word, if the length exceeds the max,
        # print only until the text[-2]
        # stops the adding word to the line.
        elif len(text)  > maximum:
                        
            text = text.rsplit(' ', 1)[0].rstrip()
            line += 1
            print(text)
            break
        
        # if the following condition, print the whole text.
        elif len(text) == maximum:
            
            print(text)
            x = x + 1
            line += 1
            break
        
    # start a new line where the division is finished.
    text = ' '.join(division[x:])
    
    # form the check value.
    check = text.split()
    
    
    # Stops the loop once the first word of next line is same with that of original text.
    # or the length of check is 0.
    if len(check) == 0 or original_text.split()[0] == text.split()[0]:
        break
         