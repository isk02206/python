'''
Name: Sung Joon Park
ID: 01514170
'''
#reading the characters that are available in the image
original = str(input())
# character divided into 2 parts
character1 = original[0]
character2 = original[1]
row = 1 #vertical line number
column = 0 #horizontal line number
line = input() #reading the line of the map
while line:
    for i in line: # reading each character
        column += 1 #increasing 1 for column after each action of searching a character
        if i != character2 and i != character1:
            print("character '" + str(i) + "' only occurs at row ", row, "and column", column)
            break
            # if the character is different from the given characters the loop must be broken and output should be given
    column = 0 # resetting the column when loop for a line is over
    row += 1 #adding 1 to the variable row after a loop for a line is over
    line = input()