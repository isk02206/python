'''
Created on 2018. 09. 11
@Subject : monkeys_and_coconuts
@Author : Son Jee Hun
@Student Number : 01406444
'''
line = int(input()) #the number of pirate
total_nut = int(input()) #the number of coconuts

n = 0 #sequential number of the pirate #n
while n != line:
    a = total_nut # the number of coconuts the pirate finds in the pile when he wakes up during the night
    b = a // line # the number of coconuts the pirate hides during the night
    c = a % line # the number of coconuts the pirate gives to the monkey during the night
    if c == 0:
        c = 'no' # when 0 comes out, it chages to string 'no'
    if c == 1:
        d = 'nut' # if number of coconuts = 1, output is nut
    else:
        d = 'nuts' # all integer number except 1, ouput is nuts
    #print(d)
    n += 1 # sequential number of the pirate # n + 1
    #print(n)
    print(a, 'nuts =', b, 'nuts for pirate#' + str(n), 'and', c, d, 'for the monkey')
    total_nut = b * (line - 1)
m_nut = total_nut // line #m nut is the number of coconuts each pirate gets in the morning
s_nut = total_nut % line #s_nut is the number of coconuts the monkey gets in the morning
if s_nut == 0:
    s_nut = 'no' # when 0 comes out, it chages to string 'no'
if s_nut == 1:
    ds_nut = 'nut' # if number of coconuts = 1, output is nut
else:
    ds_nut = 'nuts' # all integer number except 1, ouput is nuts
#print(m_nut,s_nut)
print('each pirate gets', m_nut, 'nuts and', s_nut, ds_nut, 'for the monkey')
