'''
Created on 2015. 12. 3.

@author: User
'''
5.3 Reductio ad absurdum
def equivalentFraction(numerator1, denominator1, numerator2, denominator2):
"""
>>> equivalentFraction(19, 95, 1, 5)
True
>>> equivalentFraction(532, 931, 52, 91)
True
>>> equivalentFraction(12, 13, 2, 3)
False
"""
# compare numerators after given both fractions a common denominator
return numerator1 * denominator2 == numerator2 * denominator1
def reduction(numerator, denominator):
"""
>>> reduction(19, 95)
(1, 5)
>>> reduction(532, 931)
(52, 91)
>>> reduction(2349, 9396)
(24, 96)
>>> reduction(12, 13)
(2, 3)
>>> reduction(11, 10)
(1, 0)
>>> reduction(123, 3214)
(-1, 4)
"""
# convert numerator and denominator into string of digits
numerator, denominator = str(numerator), str(denominator)
14
# for each common digit, cancel its leftmost occurrence in both the
# numerator and denominator
reduced_numerator = ¡¯¡¯
for digit in numerator:
if digit in denominator:
position = denominator.index(digit)
denominator = denominator[:position] + denominator[position + 1:]
else:
reduced_numerator += digit
# convert reduced numerator and denominator into integers
return (
int(reduced_numerator) if reduced_numerator else -1,
int(denominator) if denominator else -1
)
def validReduction(numerator, denominator):
"""
>>> validReduction(19, 95)
(1, 5)
>>> validReduction(532, 931)
(52, 91)
>>> validReduction(2349, 9396)
(24, 96)
>>> validReduction(12, 13)
(12, 13)
>>> validReduction(11, 10)
(11, 10)
>>> validReduction(123, 3214)
(123, 3214)
"""
# determine the reduced numerator and denominator
reduced_numerator, reduced_denominator = reduction(numerator, denominator)
if (
reduced_numerator >= 0 and
reduced_denominator > 0 and
equivalentFraction(numerator, denominator, reduced_numerator, reduced_denominator)
):
# return reduced fraction if it is equivalent to the original fraction
return reduced_numerator, reduced_denominator
else:
# otherwise return the original fraction
return numerator, denominator
if __name__ == ¡¯__main__¡¯:
import doctest
doctest.testmod()
5.4 Pigpen cipher
def pigpenletter(letter):
"""
>>> print(pigpenletter(¡¯A¡¯))
|
|
--+
>>> print(pigpenletter(¡¯m¡¯))
--+
.|
--+
>>> print(pigpenletter(¡¯U¡¯))
|
|:
15
+--
"""
# optional: represent white space as three empty columns
if letter.isspace():
return ¡¯ \n \n ¡¯
# if argument is no whitespace, it must be a letter
assert letter.isalpha(), ¡¯argument must be a letter¡¯
# determine row, column and number of points in center
letter = letter.upper()
value = (ord(letter) - ord(¡¯A¡¯)) % 9
row = value // 3
col = value % 3
points = (ord(letter) - ord(¡¯A¡¯)) // 9
# determine whether there¡¯s a line to the left, to the right, on top and
# below
left = col != 0
right = col != 2
top = row != 0
bottom = row != 2
# compose letter according to pigpen cipher
return ¡¯{}{}{}\n{}{}{}\n{}{}{}¡¯.format(
# top left
¡¯+¡¯ if left and top else ¡¯-¡¯ if top else ¡¯|¡¯ if left else ¡¯ ¡¯,
# top center
¡¯-¡¯ if top else ¡¯ ¡¯,
# top right
¡¯+¡¯ if right and top else ¡¯-¡¯ if top else ¡¯|¡¯ if right else ¡¯ ¡¯,
# center left
¡¯|¡¯ if left else ¡¯ ¡¯,
# center center (points)
¡¯.¡¯ if points == 1 else ¡¯:¡¯ if points == 2 else ¡¯ ¡¯,
# center right
¡¯|¡¯ if right else ¡¯ ¡¯,
# bottom left
¡¯+¡¯ if left and bottom else ¡¯-¡¯ if bottom else ¡¯|¡¯ if left else ¡¯ ¡¯,
# bottom center
¡¯-¡¯ if bottom else ¡¯ ¡¯,
# bottom right
¡¯+¡¯ if right and bottom else ¡¯-¡¯ if bottom else ¡¯|¡¯ if right else ¡¯ ¡¯
)
def pigpen(text):
"""
>>> print(pigpen(¡¯python¡¯))
--+ --+ | | +-+ +-- +-+
.| :| |:| | | |. |.|
| | +-+ | | +-- +-+
>>> print(pigpen(¡¯Rosenkreutz¡¯))
+-- +-- | +-+ +-+ | | +-- +-+ | | | +-+
|. |. :| | | |.| |.| |. | | |: |:| |:|
| +-- --+ +-+ +-+ +-+ | +-+ +-- +-+ | |
"""
# intialize three empty lines
rows = [¡¯¡¯, ¡¯¡¯, ¡¯¡¯]
# split pigpen representation of each letter into three separate lines and
# add append those with an additional space between the pigpen letters
for letter in text:
for index, row in enumerate(pigpenletter(letter).split(¡¯\n¡¯)):
rows[index] += row + ¡¯ ¡¯
# compose rows and remove final space
16
return ¡¯\n¡¯.join(row[:-1] for row in rows)
if __name__ == ¡¯__main__¡¯:
import doctest
doctest.testmod()
