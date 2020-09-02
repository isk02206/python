sid = str(input())
bal = str(input())

if sid == 'balance':
    if bal == 'balance':
        count = 9
    if bal == 'left':
        count = 8
    if bal == 'right':
        count = 7
if sid == 'left':
    if bal == 'balance':
        count = 6
    if bal == 'left':
        count = 5
    if bal == 'right':
        count = 4
if sid == 'right':
    if bal == 'balance':
        count = 3
    if bal == 'left':
        count = 2
    if bal == 'right':
        count = 1

count = format(count)
print('coin #'+count,'is counterfeit')