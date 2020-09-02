'''
Created on 2018. 10. 17
@Subject : polka_dot
@Author : Son Jee Hun
@Student Number : 01406444
'''
def deal(list_tuple_string):
    '''
    >>> deal((0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
    [0, 2, 4, 6, 8, 10, 3, 7, 1, 9, 5]
    >>> deal([0, 8, 1, 6, 2, 10, 3, 7, 4, 9, 5])
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    >>> deal('ABCDEFGHIJKLMOP')
    ['A', 'C', 'E', 'G', 'I', 'K', 'M', 'P', 'D', 'H', 'L', 'B', 'J', 'F', 'O']
    >>> deal('ALBICODJEMFKGPH')
    ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'O', 'P']
    '''
    # type change list type
    list_word = list(list_tuple_string)
    new_list =[]
    # length of new_list equal length of list or tuple or string
    while len(new_list) != len(list_tuple_string):
        new_list.append(list_word[0])
        # list_word length more than 3
        if len(list_word) >= 3:
            list_word = list_word[2:] + [list_word[1]]
            #list word first value move final value
        else:
            new_list.append(list_word[-1])
            # list_word length < 3 fianl value append new list
    return new_list


def polka(list_tuple_string):
    '''
    >>> polka((0, 2, 4, 6, 8, 10, 3, 7, 1, 9, 5))
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    >>> polka([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    [0, 8, 1, 6, 2, 10, 3, 7, 4, 9, 5]
    >>> polka('ACEGIKMPDHLBJFO')
    ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'O', 'P']
    >>> polka('ABCDEFGHIJKLMOP')
    ['A', 'L', 'B', 'I', 'C', 'O', 'D', 'J', 'E', 'M', 'F', 'K', 'G', 'P', 'H']
    '''
    list_word = list(list_tuple_string)
    # make list type word
    length_list_word = len(list_word)
    filling_order = deal([i for i in range(length_list_word)])
    scheme = [ ['.'] * length_list_word ] * length_list_word
    # make list in list

    for i in range(length_list_word):
        char = list_word[i]
        column = filling_order[i]
        for j in range(length_list_word-i): # -i because filling value pass list
            row = -1-j
            update = list(scheme[row])
            #update scheme inside list
            update[column] = char
            scheme[row] = list(update)

    return scheme[-1]

if __name__ == '__main__':
    import doctest
    doctest.testmod()