def ouroboros(word):
    '''
    >>> ouroboros('agaragar')
    True
    >>> ouroboros('sensuousnesses')
    True
    >>> ouroboros('tattarrattat')
    False
    '''
    new_word = word + word
    counter_clock = word[::-1]

    if counter_clock in new_word:
        if word != counter_clock:
            return True
        else:
            return False
    else:
        return False

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
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    correct_count = 0
    word = word.lower()
    counter = 0
    for i in word:
        if 97 <= ord(i) <= 122:
            if i == alphabet[counter]:
                correct_count += 1
                counter += 1
            else:
                counter += 1
            if counter == 25:
                counter = 0
    return correct_count

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
    length = len(word)
    first_half = word[:length//2]
    second_half = word[length//2+1:]
    first = {}
    second = {}
    for i in first_half:
        if i in first:
            first[i] += 1
        if i not in first:
            first[i] = 1
    for j in second_half:
        if j in second:
            second[j] += 1
        if j not in second:
            second[j] = 1
    for k in first:
        if first[k] in second:
            if first[k] != second[k]:
                return False
        if k not in second:
            return False
    else:
        return True
