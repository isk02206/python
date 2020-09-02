def ouroboros(word):
    '''
    >> > ouroboros('agaragar')
    True
    >> > ouroboros('sensuousnesses')
    True
    >> > ouroboros('tattarrattat')
    False
    '''

    twice_word = word * 2
    # print(twice_word)
    reversed_twice_word = twice_word[::-1]
    # print(reversed_twice_word)
    if reversed_twice_word.count(word) == 1:
        return True
    return False


# print(ouroboros('agaragar'))
# print(ouroboros('sensuousnesses'))
# print(ouroboros('tattarrattat'))

def tsuchinoko(word):
    '''
    >>> tsuchinoko('Archetypical')
    5
    >>> tsuchinoko('RESTAURATEURS')
    0
    >>> tsuchinoko('recherche')
    3
    >>> tsuchinoko('A bad egg hit KLM wipers two ways.')
    16
    '''

    lower_case_alphabet = 'abcdefghijklmnopqrstuvwxyz' * 2
    word = word.lower()
    count = 0
    word = word.replace(' ', '')
    # print(word_lower_remove_space)
    for i in range(0, len(word)):
        if lower_case_alphabet[i] == word[i]:
            count += 1
        # print(lower_case_alphabet[i], word[i])
    return count


# print(tsuchinoko('Archetypical'))
# print(tsuchinoko('RESTAURATEURS'))
# print(tsuchinoko('recherche'))
# print(tsuchinoko('A bad egg hit KLM wipers two ways.'))


def amphisbaena(word):
    '''
    >>> amphisbaena('RESTAURATEURS')
    True
    >>> amphisbaena('Archetypical')
    False
    >>> amphisbaena('recherche')
    True
    '''
    word = word.lower()
    if len(word) % 2 == 0:
        right_word = word[:len(word) // 2]
        left_word = word[-len(word) // 2:]
    elif len(word) % 2 == 1:
        right_word = word[:len(word) // 2]
        left_word = word[len(word) // 2 + 1:]
    # print(right_word, left_word)
    right_word = ''.join(sorted(right_word))
    left_word = ''.join(sorted(left_word))
    # print(right_word, left_word)
    if right_word == left_word:
        return True

    return False


# print(amphisbaena('RESTAURATEURS'))
# print(amphisbaena('Archetypical'))
# print(amphisbaena('recherche'))

if __name__ == '__main__':
    import doctest
    doctest.testmod()
