'''
Created on 2018. 10. 21
@Subject : stable_marriage
@Author : Son Jee Hun
@Student Number : 01406444
'''
def matchmaking(preference_men, preference_women):
    '''
    >>> preference_men = [[1, 0, 2, 3], [3, 0, 1, 2], [0, 2, 1, 3], [1, 2, 0, 3]]
    >>> preference_women = [[0, 2, 1, 3], [2, 3, 0, 1], [3, 1, 2, 0], [2, 1, 0, 3]]
    >>> matchmaking(preference_men, preference_women)
    ((0, 0), (1, 3), (2, 2), (3, 1))

    >>> preference_men = [[0, 2, 1], [1, 0, 2], [1, 2, 0]]
    >>> preference_women = [[2, 1, 0], [2, 1, 0], [1, 2, 0]]
    >>> matchmaking(preference_men, preference_women)
    ((0, 2), (1, 0), (2, 1))

    >>> preference_men = [[0, 2, 1, 3], [2, 1, 3, 0], [0, 3, 1, 2], [1, 2, 0, 3]]
    >>> preference_women = [[1, 0, 2, 3], [0, 2, 3, 1], [3, 0, 1, 2], [1, 3, 2, 0]]
    >>> matchmaking(preference_men, preference_women)
    ((0, 0), (1, 2), (2, 3), (3, 1))
    '''
    #make filled * list
    couples = ['*'] * len(preference_men)
    man = 0

    while '*' in couples:

        preference = 0

        while couples[man] == '*':
            woman = preference_men[man][preference]
            if woman in couples:
                # If there is a competitor
                competitor = couples.index(woman)
                # they should be in the favorable order of the women.
                if preference_women[woman].index(competitor) > preference_women[woman].index(man):
                    # The loser is remade into a *
                    couples[competitor] = '*'
                    couples[man] = woman
            else:
                couples[man] = woman

            preference += 1

        man += 1
        # recheck man
        if len(couples) == man:
            man = 0
    # make list final matching couples
    final_couples = list()
    for couple in range(len(couples)):
        final_couples.append((couple, couples[couple]))

    return tuple(final_couples)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
