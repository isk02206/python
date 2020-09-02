'''
Created on 2015. 11. 17.

@author: USER
'''
def carousel(blank, bag):
    ##print(bag)
    ##print(blank)    
    carousel = []
    for i in range(blank):
        carousel += ['None']
    position = 0
    for letter in bag:
        ##print(letter)
        ##print(carousel[position])                    
        if carousel[position] != 'None':
            position += 1
            carousel[position] = letter
            count = 0
            #position += 3
            while count < 3:
                position += 1
                if position == blank:
                    position = 0
                if carousel[position] != 'None':
                    position += 1
                    if position == blank:
                        position = 0
                count +=1

        elif carousel[position] == 'None':
            #carousel[position].replace(letter)
            carousel[position] = letter
            print(carousel)
            count1 = 0
            while count1 < 3:
                position += 1
                if position == blank:
                    position = 0
                if carousel[position] != 'None':
                    position += 1
                    if position == blank:
                        position = 0
                count1 +=1

    the_position = carousel.index(bag[-1])
    print(the_position)
print(carousel(8, 'ABCDE'))