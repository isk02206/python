import re # (input, remove, string)
sentence = input()
width = int(input())
remove_space_sentence = re.sub(' +', ' ', sentence)
word = ''
count_string = 0

import textwrap

dedented_text = textwrap.dedent(remove_space_sentence).strip()
textwrap_text = textwrap.fill(dedented_text, width)
#print(textwrap_text.split('\n'))
line_textwrap_text = textwrap_text.split('\n')

if len(textwrap_text) < width:
    width = len(textwrap_text)
    top = '+-' + '-' * (width) + '-+'
    bottom = '+-' + '-' * (width) + '-+'

else:
    top = '+-' + '-' * width + '-+'
    bottom = '+-' + '-' * width + '-+'

for i in line_textwrap_text:

    word += '| ' + i.center(width, ' ') + ' |' + '\n'

print(top)
print(word.strip())
print(bottom)
print('''        \   ^__^
         \  (oo)\_______
            (__)\       )\/\\
                ||----w |
                ||     ||''')


'''


for width in [ 20, 60, 80 ]:
    print()
    print('%d Columns:\n' % width)
    print(textwrap.fill(dedented_text, width=width))
'''

'''
print('+-' + '-' * width + '-+')
for i in remove_space_sentence:
    if width == count_string:
        word += '\n'
        count_string = 0

    if
    word += i
    count_string += 1
print(word)
'''