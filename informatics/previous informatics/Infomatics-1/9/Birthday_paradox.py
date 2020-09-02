'''
Created on 2015. 12. 3.

@author: User
'''
def birthdays(filename):
"""
>>> born = birthdays(¡¯france.txt¡¯)
>>> born[¡¯02-13¡¯]
{¡¯Mamadou Sakho¡¯, ¡¯Eliaquim Mangala¡¯}
>>> born[¡¯03-08¡¯]
{¡¯Rio Mavuba¡¯, ¡¯R¢¥emy Cabella¡¯}
"""
# construct dictionary that maps birhtdays onto the set of players that are
# born on that day
birthdays = {}
for line in open(filename, ¡¯r¡¯, encoding=¡¯utf-8¡¯):
45
# player en zijn birthday ophalen uit line
field = line.rstrip(¡¯\n¡¯).split(¡¯,¡¯)
player = field[0]
birthday = field[4][5:]
# player toevoegen aan verzameling waarop birthday wordt afgebeeld
if birthday not in birthdays:
birthdays[birthday] = set()
birthdays[birthday].add(player)
# return constructured dictionary of birthdays
return birthdays
def birthdayparadox(filename):
"""
>>> birthdayparadox(¡¯france.txt¡¯)
True
>>> birthdayparadox(¡¯belgium.txt¡¯)
False
"""
# check whether there is a shared birthday
return any(
born
for born in birthdays(filename).values()
if len(born) > 1
)
def testparadox(teams):
"""
>>> testparadox([(¡¯Algeria¡¯, ¡¯algeria.txt¡¯), (¡¯Belgium¡¯, ¡¯belgium.txt¡¯), (¡¯France¡¯, ¡¯
france.txt¡¯)])
{¡¯Algeria¡¯, ¡¯France¡¯}
"""
# return set of teams that have shared birthdays
return {
team for team, filename in teams
if birthdayparadox(filename)
}
if __name__ == ¡¯__main__¡¯:
import doctest
doctest.testmod()
