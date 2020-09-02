'''
Created on 2015. 12. 3.

@author: User
'''
def digit2letters(digit, first=True):
"""
>>> digit2letters(3)
¡¯i¡¯
>>> digit2letters(7, False)
¡¯n¡¯
>>> digit2letters(0, first=False)
¡¯t¡¯
"""
# determine row in which letters must be selected
row = ¡¯ou,a,e,i,o,u,y,ee,ei,ie¡¯ if first else ¡¯t,b,d,f,k,l,m,n,p,r¡¯
# select letters from row corresponding to given digit
    return row.split(¡¯,¡¯)[digit]
def coord2word(coordinate):
"""
>>> coord2word("38¡Æ11¡¯N")
¡¯Ipab¡¯
>>> coord2word("87¡Æ55¡¯W")
¡¯Veinul¡¯
"""
# determine first letter of word based on wind direction
    direction = coordinate[-1]
    if direction == ¡¯S¡¯:
        letters = ¡¯S¡¯
    elif direction == ¡¯W¡¯:
        letters = ¡¯V¡¯
    else:
        letters = ¡¯¡¯
# determine next letters of word by converting each digit round robin based
# on the first and the second row of the table
    first = True
    for digit in coordinate:
        if digit.isdigit():
            letters += digit2letters(int(digit), first)
            first = not first
# convert word to an uppercase letter followed by a series of lowercase
# letters and return the result
    return letters.capitalize()
def placename(latitude, longitude=None):
"""
>>> placename("38¡Æ11¡¯N", "87¡Æ55¡¯W") # New Harmony
¡¯Ipab Veinul¡¯
>>> placename("38¡Æ11¡¯N, 87¡Æ55¡¯W") # New Harmony
¡¯Ipab Veinul¡¯
>>> placename("38¡Æ90¡¯N", "77¡Æ04¡¯W") # Washington DC (USA)
¡¯Ipiet Veenouk¡¯
>>> placename("50¡Æ85¡¯N, 4¡Æ35¡¯E") # Brussels (Belgium)
¡¯Uteil Ofu¡¯
>>> placename("0¡Æ32¡¯N", "32¡Æ58¡¯E") # Kampala (Uganda)
30
¡¯Oufe Idup¡¯
>>> placename("34¡Æ61¡¯S, 58¡Æ38¡¯E") # Buenos Aires (Argentina)
¡¯Sikyb Upip¡¯
"""
# split into latitude and longitude if only a single argument is passed to
# the function
    if longitude is None:
        latitude, longitude = (x.strip() for x in latitude.split(¡¯,¡¯))
# convert each coordinate into its corresponding word
    return ¡¯{} {}¡¯.format(
        coord2word(latitude),
        coord2word(longitude)
    )
if __name__ == '__main__':
import doctest
doctest.testmod()