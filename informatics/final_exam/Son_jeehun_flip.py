'''
Created on 2018. 11. 30
@Subject : flip_floppers
@Author : Son Jee Hun
@Student Number : 01406444
'''
odd_condition = str(input())
even_condition = str(input())
alternation_count = 0
error = 0
while True:
    other_odd_condition = str(input())
    other_even_condiiton = str(input())
    if other_even_condiiton == 'stop' or other_odd_condition == 'stop':
        break
    # if stop is loop stop
    if odd_condition[odd_condition.index(';')+1::] == other_odd_condition[other_odd_condition.index(';')+1::] and even_condition[even_condition.index(';')+1::] == other_even_condiiton[other_even_condiiton.index(';')+1::]:
        alternation_count += 1
        # same odd_conditon == other odd condition alternation count + 1
    elif odd_condition[odd_condition.index(';')+1::] != other_odd_condition[other_odd_condition.index(';')+1::]:
        error += 1
        # not same count error + 1
        if error == 1:
            print('alternating sequence with one exception:', other_odd_condition[:other_odd_condition.index(';')])
            break
    elif even_condition[even_condition.index(';')+1::] == other_even_condiiton[other_even_condiiton.index(';')+1::]:
        error += 1
        if error == 1:
            print('alternating sequence with one exception:', other_even_condiiton[:other_even_condiiton.index(';')])
            break
if alternation_count == 0: # not alternation no alternating sequence
    print('no alternating sequence')

elif alternation_count > 0 and error == 0:
    print('alternating sequence')

'''
Alexander III;bald
Nicholas II;hairy
Vladimir Lenin;bald
Joseph Stalin;hairy
Nikita Khrushchev;bald
Leonid Brezhnev;hairy
Yuri Andropov;bald
Konstantin Chernenko;hairy
Mikhail Gorbachev;bald
Boris Yeltsin;hairy
Vladimir Putin;bald
Dmitry Medvedev;hairy
Vladimir Putin;bald
stop
'''

'''
1;A
2;B
3;A
4;B
5;B
6;B
7;A
8;B
9;A
stop
'''