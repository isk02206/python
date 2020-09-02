def pattern(word):
    '''
    >>> pattern('AC Melon')
    '_C M_l_n'
    >>> pattern('slipstack')
    'sl_pst_ck'
    >>> pattern('Wander Women')
    'W_nd_r W_m_n'
    '''
    vowel = ['a','e','i','o','u','A','E','I','O','U']
    newword= ''
    for i in word:
        if i in vowel:
            newword += '_'
        else:
            newword += i
    return newword

def bloopers(textfile,occurences=1,length=1):
    '''
    >>> bloopers('wheeloffortune.txt', length=13)
    {'B_tm_n _nd R_b_n': {'Batman and Robin', 'Batmen and Reban'}}
    >>> bloopers('wheeloffortune.txt', occurrences=3)
    {'W_nd_r W_m_n': {'Wander Women', 'Winder Woman', 'Wonder Woman'}}
    >>> bloopers('wheeloffortune.txt', occurrences=2, length=12)
    {'W_nd_r W_m_n': {'Wander Women', 'Winder Woman', 'Wonder Woman'}, 'B_tm_n _nd R_b_n': {'Batman and Robin', 'Batmen and Reban'}}
    '''
    reader = open(textfile, 'r')
    bloop = {}
    for j in reader:
        x = pattern(j.rstrip())
        if x not in bloop:
            bloop[x] = set()
            bloop[x].add(j.rstrip())
        if x in bloop:
            bloop[x].add(j.rstrip())
