def pattern(x):
    '''
    >>> pattern('AC Melon')
    '_C M_l_n'
    >>> pattern('slipstack')
    'sl_pst_ck'
    >>> pattern('Wander Women')
    'W_nd_r W_m_n'
    '''
    vowels = ['a','e','i','o','u','A','E','I','O','U']
    new = ''
    for i in x:
        if i not in vowels:
            new += i
        if i in vowels:
            new += '_'
    return new

def bloopers(textfile,occurences=None, length=None):
    '''
    >>> candidates = bloopers('wheeloffortune.txt')
    >>> candidates['_C M_l_n']
    {'AC Melon', 'AC Milan'}
    >>> candidates['sl_pst_ck']
    {'slapstick', 'slipstack'}
    >>> candidates['W_nd_r W_m_n']
    {'Winder Woman', 'Wander Women', 'Wonder Woman'}

    >>> bloopers('wheeloffortune.txt', length=13)
    {'B_tm_n _nd R_b_n': {'Batman and Robin', 'Batmen and Reban'}}
    >>> bloopers('wheeloffortune.txt', occurrences=3)
    {'W_nd_r W_m_n': {'Wander Women', 'Winder Woman', 'Wonder Woman'}}
    >>> bloopers('wheeloffortune.txt', occurrences=2, length=12)
    {'W_nd_r W_m_n': {'Wander Women', 'Winder Woman', 'Wonder Woman'}, 'B_tm_n _nd R_b_n': {'Batman and Robin', 'Batmen and Reban'}}
    '''
    reader = open(textfile, 'r')
