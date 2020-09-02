'''
Created on 2018. 1. 2.

@author: TaeWoo
'''

import datetime

day = int(input())
month = input()
year = int(input())

month_convert = {'january': 1, 'february' : 2, 'march': 3, 'april' : 4, 'may': 5, 'june': 6, 'july': 7, 'august': 8, 
                 'september': 9, 'october': 10, 'november': 11, 'december': 12}

final_year = year - 2000
final_month = month_convert[month]
final_days = day

if final_month == 12:
    final_year += 1
    final_month = 0
    
if final_year == 1:
    final_year = str(final_year) + ' year'

else:
    final_year = str(final_year) + ' years'
    
if final_month == 1:
    final_month = str(final_month) + ' month'

else:
    final_month = str(final_month) + ' months'
    
if final_days <= 1:
    final_days = str(final_days) + ' day'

else:
    final_days = str(final_days) + ' days'
    
print('Stopwatch babies are {}, {} and {} old on {} {} {}.'.format(final_days, final_month, final_year, day, month, year))
