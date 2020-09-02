# read ten digits of an ISBN-10 code (each on a separate line)
x1 = int(input())
x2 = int(input())
x3 = int(input())
x4 = int(input())
x5 = int(input())
x6 = int(input())
x7 = int(input())
x8 = int(input())
x9 = int(input())
x10 = int(input())
# compute check digit
checkdigit = (
    x1 + 2 * x2 + 3 * x3 + 4 * x4 + 5 * x5 + 6 * x6 + 7 * x7 + 8 * x8 + 9 * x9
) % 11

# check correctness of the check digit
print('OK' if x10 == checkdigit else 'WRONG')
"""
alternative solution:

if x10 == checkdigit:
    print(¡¯OK¡¯)
else:
    print(¡¯WRONG¡¯)
"""