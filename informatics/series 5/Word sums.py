def lettervalue(word):
    '''
    >>> lettervalue('A')
    1
    >>> lettervalue('j')
    10
    >>> lettervalue('!')
    0
    '''
    import string
    lower_case_alphabet = string.ascii_lowercase
    word_lower = word.lower()
    if word_lower in lower_case_alphabet:
        return lower_case_alphabet.find(word_lower) + 1
    if word_lower not in lower_case_alphabet:
        return 0


def wordvalue(word):
    '''
    >>> wordvalue('arm')
    32
    >>> wordvalue('BEND')
    25
    >>> wordvalue('elbow')
    57
    '''
    count = 0
    for i in word:
        count_i = lettervalue(i)
        count += count_i
    return count


def wordsum(word_1, word_2, word_3):
    '''
    >>> wordsum('arm', 'BEND', 'elbow')
    True
    >>> wordsum('KING', 'chair', 'THRONE')
    True
    >>> wordsum('Monty', 'Python', 'SHRUBBERY')
    False
    '''
    if wordvalue(word_1) + wordvalue(word_2) == wordvalue(word_3):
        return True

    return False


if __name__ == '__main__':
    import doctest
    doctest.testmod()