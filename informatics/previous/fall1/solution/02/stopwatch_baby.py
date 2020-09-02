# read date
day = int(input()) # day
month = input() # month name
year = int(input()) # year
# determine stopwatch baby's age in months from month name
if month == 'january':
    age_months = 1
elif month == 'february':
    age_months == 2
elif month =='march':
    age_months = 3
elif month == 'april':
    age_months = 4
elif month == 'may':
    age_months = 5
elif month == 'june':
    age_months = 6
elif month == 'july':
    age_months = 7
elif month == 'august':
    age_months = 8
elif month == 'september':
    age_months = 9
elif month == 'october':
    age_months = 10
elif month == 'november':
    age_months = 11
elif month == 'december':
    age_months = 0
"""
alternative way to convert month name into age in months of stopwatch baby:
age_months = 'january,february,march,april,may,june,july,'
age_months += 'august,september,october,november,december'
age_months = (age_months.split(',').index(month.lower()) + 1) % 12
"""
# determine age in years from year
age_years = year - 2000 + int(not age_months)
# generate singular or plural version of time units
days = 'day' if day == 1 else 'days'
months = 'month' if age_months == 1 else 'months'
years = 'year' if age_years == 1 else 'years'
# print formatted age of stopwatch baby
template = 'Stopwatch babies are {{0}} {0}, {{1}} {1} and {{2}} {2} old on {{0}} {{3}} {{4}}.'
template = template.format(days, months, years)
template = template.format(day, age_months, age_years, month, year)
print(template)