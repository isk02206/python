'''
Created on 2015. 12. 3.

@author: User
'''
def copolymer(shorthand):
"""
>>> copolymer(¡¯(AB)_18¡¯)
¡¯ABABABABABABABABABABABABABABABABABAB¡¯
>>> copolymer(¡¯(ABBA)_9¡¯)
¡¯ABBAABBAABBAABBAABBAABBAABBAABBAABBA¡¯
>>> copolymer(¡¯(ABABBAAAABBB)_3¡¯)
¡¯ABABBAAAABBBABABBAAAABBBABABBAAAABBB¡¯
32
>>> copolymer(¡¯ABABBAAAABBBABABBAAAABBBBBABBAAAABBB¡¯)
¡¯ABABBAAAABBBABABBAAAABBBBBABBAAAABBB¡¯
"""
if shorthand.isalpha():
# polymer was not given in shorthand notation, so the polymer itself may
# be returned
return shorthand
else:
# split shorthand notation in period and number of repetitions
period, repetitions = shorthand.split(¡¯_¡¯)
# return the repeated period
return period[1:-1] * int(repetitions)
def is_periodic(copolymer, period):
"""
>>> is_periodic(¡¯ABABABABABABABABABABABABABABABABABAB¡¯, ¡¯AB¡¯)
True
>>> is_periodic(¡¯ABABABABABABABABABABABABABABABABABAB¡¯, ¡¯ABA¡¯)
False
>>> is_periodic(¡¯ABABABABABABABABABABABABABABABABABAB¡¯, ¡¯ABAB¡¯)
True
>>> is_periodic(¡¯ABABBAAAABBBABABBAAAABBBABABBAAAABBB¡¯, ¡¯ABABBAAAABBB¡¯)
True
"""
# check whether copolymer is constructed as repetition of period
return copolymer == period * (len(copolymer) // len(period))
def period(copolymer, minimal_repetition=1):
"""
>>> period(¡¯ABABABABABABABABABABABABABABABABABAB¡¯)
¡¯AB¡¯
>>> period(¡¯ABABABABABABABABABABABABABABABABABAB¡¯, minimal_repetition=10)
¡¯AB¡¯
>>> period(¡¯ABABABABABABABABABABABABABABABABABAB¡¯, 20)
¡¯¡¯
>>> period(¡¯ABBAABBAABBAABBAABBAABBAABBAABBAABBA¡¯)
¡¯ABBA¡¯
>>> period(¡¯ABABBAAAABBBABABBAAAABBBABABBAAAABBB¡¯)
¡¯ABABBAAAABBB¡¯
>>> period(¡¯ABABBAAAABBBABABBAAAABBBBBABBAAAABBB¡¯)
¡¯ABABBAAAABBBABABBAAAABBBBBABBAAAABBB¡¯
>>> period(¡¯ABABBAAAABBBABABBAAAABBBBBABBAAAABBB¡¯, 2)
¡¯¡¯
"""
# check all possible periods, starting with the shortest one
for length in range(1, len(copolymer) // minimal_repetition + 1):
period = copolymer[:length]
if is_periodic(copolymer, period):
return period
# no possible period found
return ¡¯¡¯
def shorthand(copolymer):
"""
>>> shorthand(¡¯ABABABABABABABABABABABABABABABABABAB¡¯)
¡¯(AB)_18¡¯
>>> shorthand(¡¯ABBAABBAABBAABBAABBAABBAABBAABBAABBA¡¯)
¡¯(ABBA)_9¡¯
>>> shorthand(¡¯ABABBAAAABBBABABBAAAABBBABABBAAAABBB¡¯)
¡¯(ABABBAAAABBB)_3¡¯
>>> shorthand(¡¯ABABBAAAABBBABABBAAAABBBBBABBAAAABBB¡¯)
33
¡¯ABABBAAAABBBABABBAAAABBBBBABBAAAABBB¡¯
"""
# determine period of the copolymer
p = period(copolymer)
if len(p) < len(copolymer):
# construct shorthand notation if period differs from copolymer itself
return ¡¯({})_{}¡¯.format(p, len(copolymer) // len(p))
else:
# return the copolymer itself if it is not periodic
return copolymer
if __name__ == ¡¯__main__¡¯:
import doctest
doctest.testmod()

