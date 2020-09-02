'''
Created on 2015. 10. 9.

@author: Jun Kim
'''

def pigpenletter(alpha) :
    tb = [['  |', '| |', '|  '], ['--+', '+-+', '+--']]
    mid = [['  |', '| |', '|  '], [' .|', '|.|', '|. '], [' :|', '|:|', '|: ']]
    alpha = alpha.upper()
    digit = ord(alpha) - 64
    if digit < 10 :
        midnum = 0
    elif digit < 19 :
        midnum = 1
        digit -= 9
    elif digit < 28 :
        midnum = 2
        digit -= 18
    
    if digit % 3 == 1 :
        lrnum = 0
    elif digit % 3 == 2 :
        lrnum = 1
    elif digit % 3 == 0 :
        lrnum = 2
    if digit < 4 :
        topnum = 0
        bottomnum = 1
    elif digit < 7 :
        topnum = bottomnum = 1
    elif digit < 10 :
        topnum = 1
        bottomnum = 0
    top = tb[topnum][lrnum]
    bottom = tb[bottomnum][lrnum]
    middle = mid[midnum][lrnum]
    alpha = top + '\n' + middle + '\n' + bottom
    return alpha
def pigpen(string) :
    string = string.upper()
    pig = []
    temp = ''
    for i in string :
        temp = pigpenletter(i)
        pig.append(temp.split('\n'))
    string = ''
    for i in range(3) :
        for j in pig :
            string += j[i] + ' '
        string = string[:string.rfind(' ')]
        string += '\n'
    string = string.rstrip('\n')
    return string

#print(pigpenletter('A'))