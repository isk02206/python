'''
Created on 2015. 12. 3.

@author: User
'''
6.4 Doomsday clock
def clock(minutes):
"""
>>> clock(0)
¡¯00:00¡¯
>>> clock(7)
¡¯23:53¡¯
>>> clock(123)
¡¯21:57¡¯
"""
# convert minutes before midnight into minutes since midnight
minutes = (24 * 60 - int(minutes)) % (24 * 60)
# convert minutes since midnight into hours and minutes on 24-hour clock
hours, minutes = minutes // 60, minutes % 60
# representation on 24-hour clock in format hh:mm
return ¡¯{:>02d}:{:>02d}¡¯.format(hours, minutes)
def progress(adjustments):
"""
>>> adjustments = ¡¯1947 7,1949 3,1953 2,1960 7,1963 12,1968 7,1969 10,1972 12,1974 9,1980
7,1981 4,1983 3,1984 3¡¯
>>> progress(adjustments)
((1947, ¡¯23:53¡¯), (1949, ¡¯23:57¡¯), (1953, ¡¯23:58¡¯), (1960, ¡¯23:53¡¯), (1963, ¡¯23:48¡¯),
(1968, ¡¯23:53¡¯), (1969, ¡¯23:50¡¯), (1972, ¡¯23:48¡¯), (1974, ¡¯23:51¡¯), (1980, ¡¯23:53¡¯),
(1981, ¡¯23:56¡¯), (1983, ¡¯23:57¡¯), (1984, ¡¯23:57¡¯))
"""
# intialize list
progress = []
# split string into list of adjustments and process individual adjustments
for adjustment in adjustments.split(¡¯,¡¯):
# split adjustment into year and number of minutes before midnight
year, minutes = adjustment.split()
# append year and representation on 24-hour clock to list
progress.append((int(year), clock(int(minutes))))
# convert list into tuple
return tuple(progress)
def threat(year, clock):
"""
>>> adjustments = ¡¯1947 7,1949 3,1953 2,1960 7,1963 12,1968 7,1969 10,1972 12,1974 9,1980
7,1981 4,1983 3,1984 3¡¯
>>> doomsdayclock = progress(adjustments)
>>> threat(1974, doomsdayclock)
¡¯23:51¡¯
22
>>> threat(1950, doomsdayclock)
¡¯23:57¡¯
>>> threat(1965, doomsdayclock)
¡¯23:48¡¯
"""
# find latest adjustment preceding or equal to the given year
index = -1
while clock[index][0] > year:
index -= 1
# return time set at latest adjustment
return clock[index][1]
if __name__ == ¡¯__main__¡¯:
import doctest
doctest.testmod(