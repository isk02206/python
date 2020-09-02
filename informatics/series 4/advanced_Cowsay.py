'''
Created on 2018. 09. 25
@Subject : cowsay
@Author : Son Jee Hun
@Student Number : 01406444
'''

import re # (input, remove, string)
import textwrap
sentence = input()
width = int(input())
remove_space_sentence = re.sub(' +', ' ', sentence) # all space remove and then that position add 1 space
word = ''

dedented_text = textwrap.dedent(remove_space_sentence).strip() #word divide space units
textwrap_text = textwrap.fill(dedented_text, width) # Remove any common leading whitespace from every line in text.
#print(textwrap_text.split('\n'))
line_textwrap_text = textwrap_text.split('\n') # line split

if len(textwrap_text) < width: # width bigger than sentence length
    width = len(textwrap_text) # change value width because text box become huge box
    top = '+-' + '-' * width + '-+' # top text box
    bottom = '+-' + '-' * width + '-+'# bottom text box

else:
    top = '+-' + '-' * width + '-+'# top text box
    bottom = '+-' + '-' * width + '-+'# bottom text box

for i in line_textwrap_text: #i is line split word
    word += '| ' + i.center(width, ' ') + ' |' + '\n' # word center str.center(length, fill value)

print(top)
print(word.strip())
print(bottom)
print('''        \   ^__^
         \  (oo)\_______
            (__)\       )\/\\
                ||----w |
                ||     ||''')