'''
Created on 2016. 1. 4.

@author: User
'''
capital = int(input())
state = str(input())
c1 = str(input())
c2 = str(input())
state1 = str(input())
c3 = str(input())
c4 = str(input())
state2 = str(input())
c5 = str(input())
c6 = str(input())
s=str(input())
count = 0
count1 = capital*2
count2 = count1*2
for x in state:
    if state == 'everything':
        everything = int(capital)
        if c1 == c2:
            count=capital*2
            print(count)
            if state1 == 'everything':
                everything = int(capital)
                if c3 == c4:
                    count=count1*2
                    print(count)
                    if state2 == 'everything':
                        everything = int(capital)
                        if c5 == c6:
                            count=count2*2
                            print(count)
                            if s == 'stop':
                                if count <= capital:
                                    print("You can't gamble",capital,'dollar if you only have',count,'dollar.')
                                else:
                                    print('You end up with',count,'dollar.')
                                    break
                    elif state2 != 'everything':
                        state = int()