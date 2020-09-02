day = int(input())
month = str(input())

if month == 'March':
    if 21 <= day <= 31:
        print('It is spring on', month, str(day)+'.')
    elif 1 <= day <= 20:
        print('It is winter on', month, str(day)+'.')
elif month == 'June':
    if 1 <= day <= 20:
        print('It is spring on', month, str(day)+'.')
    elif 21 <= day <= 31:
        print('It is summer on', month, str(day)+'.')
elif month == 'April' or month == 'May':
    print('It is spring on', month, str(day)+'.')


elif month == 'July' or month == 'August':
    print('It is summer on', month, str(day)+'.')
elif month == 'September':
    if 1 <= day <= 22:
        print('It is summer on', month, str(day)+'.')
    elif 23 <= day <= 31:
        print('It is autumn on', month, str(day)+'.')

elif month == 'October' or month == 'November':
    print('It is autumn on', month, str(day) + '.')
elif month == 'December':
    if 1 <= day <= 20:
        print('It is autumn on', month, str(day) + '.')
    elif 21 <= day <= 31:
        print('It is winter on', month, str(day) + '.')
elif month == 'January' or month == 'February':
    print('It is winter on', month, str(day) + '.')