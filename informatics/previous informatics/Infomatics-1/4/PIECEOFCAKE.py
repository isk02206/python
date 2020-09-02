'''
Created on 2015. 12. 3.

@author: User
'''
4.3 Piece of cake
# read the given number from input
number = input()
# repeat the procedure until it reaches the number 123
while number != ¡¯123¡¯:
# determine the number of even and odd digits
even, odd = 0, 0
for digit in number:
if int(digit) % 2:
odd += 1
else:
even += 1
# string together the three numbers to come up with a new number
number = ¡¯{}{}{}¡¯.format(even, odd, len(number))
# write the number to output
print(number)
4.4 Words and numbers
# read how many numbers are contained in the input
numbers = int(input())
# initialize output
output = ¡¯¡¯
# determine for each number in the input whether or not its word value is
# smaller than the value of the number itself
for _ in range(numbers):
# read the next line
line = input()
# split line into the number and the English name of the number
number, name = line.split(¡¯, ¡¯, 1)
# determine word value of the number
wordValue = 0
for character in name.lower():
if character.isalpha():
wordValue += ord(character) - ord(¡¯a¡¯) + 1
# add number to the list if its word value is smaller than the value of the
# number itself
if wordValue < int(number):
if output:
output += ¡¯, ¡¯
output += ¡¯{}[{}]¡¯.format(number, wordValue)
# print the list of numbers having a smaller word value than the value of the
10
# numbers themselves
print(output)
4.5 The blank column
# read the given sentence
sentence = input()
# read the maximal width of a line
width = int(input())
# initialize the line index and the line content
index, line = 0, ¡¯¡¯
# print completed lines until the next line restarts with the first word of the
# given sentence or ten lines have been printed
while index < 10 and line != sentence:
# increment the line counter
index += 1
# keep appending the sentence until the line exceeds the maximal width
while len(line) <= width:
line += ¡¯ ¡¯ + sentence if line else sentence
# print maximal portion of the line that does not exceed the maximal width
position = width
while not line[position].isspace():
position -= 1
print(line[:position])
# retain the remainder of the line
line = line[position + 1:]